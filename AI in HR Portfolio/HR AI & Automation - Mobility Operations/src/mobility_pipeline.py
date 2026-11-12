"""Deterministic, privacy-conscious mobility case triage prototype.

This reference implementation uses ONLY synthetic cases and performs no external writes.
It is not a production HRIS, payroll, immigration or employment decision system.

Run: python -m src.mobility_pipeline --input sample_data/cases.json
"""
from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from typing import Any

POLICY_VERSION = "v0.1"
JURISDICTIONS = {"AE", "SA", "GB", "DE", "FR", "US"}
CATEGORIES = {
    "immigration_document": ("request_documents", "high"),
    "payroll_mismatch": ("create_discrepancy_ticket", "critical"),
    "identity_change": ("manual_identity_verification", "critical"),
    "document_check": ("request_documents", "high"),
    "policy_question": ("draft_policy_response", "medium"),
    "case_routing": ("route_to_team", "low"),
}
MUST_REVIEW = {
    "immigration_document", "payroll_mismatch",
    "identity_change", "document_check"
}
KNOWN_POLICIES = {"POLICY-GEN-001"}
ALLOWED_KEYS = {
    "event_id", "case_id", "tenant_id", "category", "jurisdiction", "source",
    "contains_sensitive_data", "document_complete",
    "effective_date_mismatch", "approved_policy_id"
}


@dataclass(frozen=True)
class Decision:
    event_id: str
    case_id: str
    category: str
    jurisdiction: str
    proposed_action: str
    risk: str
    checker_passed: bool
    disposition: str
    reason_code: str
    policy_version: str = POLICY_VERSION


def validate(event: dict[str, Any]) -> None:
    """Fail closed, rather than silently ingesting unexpected personal fields."""
    if not isinstance(event, dict):
        raise ValueError("invalid_event_shape")
    extra = set(event) - ALLOWED_KEYS
    if extra:
        raise ValueError("unapproved_fields_present")
    for key in ("event_id", "case_id", "tenant_id", "category", "jurisdiction", "source"):
        if not isinstance(event.get(key), str) or not 1 <= len(event[key]) <= 90:
            raise ValueError("invalid_required_field")
    if type(event.get("contains_sensitive_data")) is not bool:
        raise ValueError("invalid_sensitivity_flag")
    for key in ("document_complete", "effective_date_mismatch"):
        if key in event and type(event[key]) is not bool:
            raise ValueError("invalid_boolean_field")
    if "approved_policy_id" in event and not isinstance(event["approved_policy_id"], str):
        raise ValueError("invalid_policy_id")


def maker(event: dict[str, Any]) -> tuple[str, str]:
    """Specialist/routing layer: recommends a *proposal*, never an action execution."""
    pair = CATEGORIES.get(event["category"])
    if pair is None:
        return "manual_review", "high"
    action, risk = pair
    if event["category"] == "immigration_document" and event.get("document_complete", False):
        return "send_to_mobility_review", "high"
    return action, risk


def checker(event: dict[str, Any], proposed_action: str) -> tuple[bool, str, str]:
    """Independent, rule-based checker enforces guardrails and approval needs."""
    if event["contains_sensitive_data"]:
        return False, "human_approval_required", "sensitive_data_quarantine"
    if event["jurisdiction"] not in JURISDICTIONS:
        return False, "manual_escalation", "jurisdiction_not_validated"
    pair = CATEGORIES.get(event["category"])
    if pair is None:
        return False, "manual_escalation", "unsupported_case_type"
    if event["category"] == "immigration_document":
        permitted = {"request_documents", "send_to_mobility_review"}
    else:
        permitted = {pair[0]}
    if proposed_action not in permitted:
        return False, "manual_escalation", "maker_checker_disagreement"
    if event["category"] == "policy_question" and event.get("approved_policy_id") not in KNOWN_POLICIES:
        return False, "manual_escalation", "missing_approved_policy_evidence"
    if event["category"] in MUST_REVIEW:
        return True, "human_approval_required", "regulated_or_high_risk"
    if event["category"] == "policy_question":
        return True, "draft_only", "approved_policy_reference"
    return True, "internal_routing_only", "low_risk_routing"


def sanitize_error_reason(exc: ValueError) -> str:
    """Never echo raw exception input or unapproved field names to audit logs."""
    allowed_reasons = {
        "invalid_event_shape", "unapproved_fields_present", "invalid_required_field",
        "invalid_sensitivity_flag", "invalid_boolean_field", "invalid_policy_id"
    }
    value = str(exc)
    return value if value in allowed_reasons else "validation_error"


class MobilityPipeline:
    """In-memory single-process demonstration of idempotency and audit semantics.

    Production event deduplication must use a transactional, tenant-partitioned store.
    """

    def __init__(self) -> None:
        self.seen_event_keys: set[tuple[str, str]] = set()
        self.audit: list[dict[str, Any]] = []

    def process(self, event: dict[str, Any]) -> Decision:
        validate(event)
        event_key = (event["tenant_id"], event["event_id"])
        if event_key in self.seen_event_keys:
            return Decision(
                event_id=event["event_id"], case_id=event["case_id"],
                category=event["category"], jurisdiction=event["jurisdiction"],
                proposed_action="none", risk="none", checker_passed=False,
                disposition="duplicate_event", reason_code="idempotency_replay"
            )
        self.seen_event_keys.add(event_key)
        action, risk = maker(event)
        passed, disposition, reason = checker(event, action)
        decision = Decision(
            event_id=event["event_id"], case_id=event["case_id"],
            category=event["category"], jurisdiction=event["jurisdiction"],
            proposed_action=action, risk=risk,
            checker_passed=passed, disposition=disposition, reason_code=reason
        )
        trace_id = hashlib.sha256(
            (event["tenant_id"] + ":" + event["event_id"]).encode("utf-8")
        ).hexdigest()[:16]
        # Data-minimized audit: NO names, documents, salary, emails, IDs or payloads.
        self.audit.append({
            "trace_id": trace_id,
            "tenant_ref": hashlib.sha256(event["tenant_id"].encode()).hexdigest()[:12],
            "event_ref": hashlib.sha256(event["event_id"].encode()).hexdigest()[:12],
            "case_category": decision.category,
            "jurisdiction": decision.jurisdiction,
            "proposed_action": decision.proposed_action,
            "checker_passed": decision.checker_passed,
            "disposition": decision.disposition,
            "reason_code": decision.reason_code,
            "risk": decision.risk,
            "policy_version": decision.policy_version,
            "timestamp_utc": datetime.now(timezone.utc).isoformat()
        })
        return decision


def run_fixture(path: Path) -> dict[str, Any]:
    cases = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(cases, list):
        raise ValueError("fixtures_must_be_list")
    pipeline = MobilityPipeline()
    results = []
    for case in cases:
        try:
            result = pipeline.process(case)
            results.append(asdict(result))
        except ValueError as exc:
            # Do not echo untrusted input or personal fields.
            results.append({
                "disposition": "manual_escalation",
                "reason_code": sanitize_error_reason(exc),
                "checker_passed": False
            })
    summary: dict[str, int] = {}
    for result in results:
        key = result["disposition"]
        summary[key] = summary.get(key, 0) + 1
    return {"status": "synthetic_demo", "policy_version": POLICY_VERSION,
            "summary": summary, "decisions": results, "audit": pipeline.audit}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="sample_data/cases.json")
    args = parser.parse_args()
    print(json.dumps(run_fixture(Path(args.input)), indent=2))


if __name__ == "__main__":
    main()
