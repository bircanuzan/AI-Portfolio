"""Synthetic KYB case validation and human-review routing (not a live AI model)."""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any, Dict, List


REQUIRED_FIELDS = ("legal_name", "registry_number", "jurisdiction")


def evaluate_case(case: Dict[str, Any], as_of: date | None = None) -> Dict[str, Any]:
    """Return review flags and evidence hash using only synthetic structured fields."""
    as_of = as_of or date(2026, 11, 4)
    case_id = str(case.get("case_id", "unknown"))
    declared = case.get("declared") or {}
    doc = case.get("mock_extracted_document") or {}
    flags: List[str] = []

    for field in REQUIRED_FIELDS:
        if not declared.get(field):
            flags.append(f"missing_declared_{field}")
        if not doc.get(field):
            flags.append(f"missing_document_{field}")
        if declared.get(field) and doc.get(field):
            if str(declared[field]).strip().casefold() != str(doc[field]).strip().casefold():
                flags.append(f"mismatch_{field}")

    expiry = doc.get("expiry_date")
    if expiry:
        try:
            if date.fromisoformat(str(expiry)) < as_of:
                flags.append("expired_document")
        except ValueError:
            flags.append("invalid_expiry_date")

    owners = declared.get("beneficial_owners")
    if not isinstance(owners, list) or not owners:
        flags.append("missing_beneficial_owners")
    else:
        try:
            total = sum(float(o["ownership_pct"]) for o in owners)
            if not 99.9 <= total <= 100.1:
                flags.append("ownership_total_not_100")
            if any(float(o["ownership_pct"]) < 0 or float(o["ownership_pct"]) > 100 for o in owners):
                flags.append("invalid_owner_percentage")
        except (KeyError, TypeError, ValueError):
            flags.append("invalid_owner_record")

    evidence_hash = hashlib.sha256(
        json.dumps(doc, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    ).hexdigest()
    flags = sorted(set(flags))
    return {
        "case_id": case_id,
        "status": "priority_human_review" if flags else "standard_human_review",
        "flags": flags,
        "human_decision_required": True,
        "evidence_sha256": evidence_hash,
        "prototype_scope": "deterministic_validation_mock_extraction",
    }


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python regtech_demo.py data/synthetic_cases.json")
    cases = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    if not isinstance(cases, list):
        raise SystemExit("Expected a JSON array of synthetic cases")
    print(json.dumps([evaluate_case(case) for case in cases], indent=2))


if __name__ == "__main__":
    main()
