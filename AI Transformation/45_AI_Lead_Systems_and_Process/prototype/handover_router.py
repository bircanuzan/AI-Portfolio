"""Synthetic handover intake rule demonstrator; NOT AI, OCR, or production software."""
from __future__ import annotations
from typing import Mapping, Any

RULE_VERSION = "handover-routing-demo-v1.0"
REQUIRED_IDENTIFIERS = ("case_id", "unit_id", "customer_ref")
REQUIRED_DOCUMENT_FLAGS = ("has_id_proof", "has_contract", "has_payment_clearance_doc")


def route_case(case: Mapping[str, Any]) -> dict:
    """Return intake routing recommendation, never a legal/financial approval."""
    missing = [field for field in REQUIRED_IDENTIFIERS if not str(case.get(field, "")).strip()]
    missing += [field for field in REQUIRED_DOCUMENT_FLAGS if case.get(field) is not True]
    if missing:
        return {
            "decision": "NEEDS_DOCUMENTS",
            "reasons": [f"missing_or_invalid:{field}" for field in missing],
            "needs_human": True,
            "rule_version": RULE_VERSION,
        }

    flags = []
    if case.get("duplicate_flag") is True:
        flags.append("duplicate_case_review")
    if case.get("mismatch_flag") is True:
        flags.append("identity_or_contract_mismatch_review")
    if case.get("payment_cleared") != "YES":
        flags.append("finance_clearance_review")
    if case.get("project_ready") != "YES":
        flags.append("project_readiness_review")
    if flags:
        return {
            "decision": "HUMAN_REVIEW",
            "reasons": flags,
            "needs_human": True,
            "rule_version": RULE_VERSION,
        }
    return {
        "decision": "READY_FOR_HUMAN_APPROVAL",
        "reasons": ["intake_checks_completed_human_signoff_required"],
        "needs_human": True,
        "rule_version": RULE_VERSION,
    }


def normalize_csv_row(row: Mapping[str, str]) -> dict:
    """Normalize *fictional* CSV fixture fields only. Not suitable for user uploads."""
    value = dict(row)
    for key in (*REQUIRED_DOCUMENT_FLAGS, "duplicate_flag", "mismatch_flag"):
        value[key] = row[key].strip().lower() == "true"
    for key in ("payment_cleared", "project_ready"):
        value[key] = row[key].strip().upper()
    return value
