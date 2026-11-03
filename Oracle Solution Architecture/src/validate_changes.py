"""Synthetic HCM-to-Finance staging validator; no Oracle SDK/API or live data.

Run: python 'Oracle Solution Architecture/src/validate_changes.py'
Tests: python -m unittest discover -s 'Oracle Solution Architecture/tests' -v
"""
from datetime import date

ALLOWED_EVENTS = {"HIRE", "TRANSFER", "TERMINATION", "LEAVE"}
MANDATORY = ("event_id", "worker_id", "event_type", "effective_date", "subsidiary")
SUBSIDIARIES = {"SUB-A", "SUB-B"}
COST_CENTERS = {"CC-100", "CC-200"}


def validate_event(event: dict, seen: set[str] | None = None) -> tuple[bool, str]:
    """Gate a synthetic change before any downstream integration could occur."""
    if any(not event.get(field) for field in MANDATORY):
        return False, "MISSING_REQUIRED_FIELD"
    if event["event_type"] not in ALLOWED_EVENTS:
        return False, "UNSUPPORTED_EVENT"
    try:
        date.fromisoformat(event["effective_date"])
    except (ValueError, TypeError):
        return False, "INVALID_EFFECTIVE_DATE"
    if event["subsidiary"] not in SUBSIDIARIES:
        return False, "UNKNOWN_SUBSIDIARY"
    if not event.get("approved_by"):
        return False, "MISSING_HR_APPROVAL"
    if event["event_type"] in {"HIRE", "TRANSFER"}:
        if event.get("cost_center") not in COST_CENTERS:
            return False, "INVALID_FINANCE_COST_CENTER"
        if not event.get("finance_reference_valid", False):
            return False, "FINANCE_REFERENCE_NOT_APPROVED"
    if seen is not None and event["event_id"] in seen:
        return False, "DUPLICATE_EVENT"
    if seen is not None:
        seen.add(event["event_id"])
    return True, "ACCEPTED_FOR_STAGING_ONLY"


def demo():
    events = [
        dict(event_id="EVT-001", worker_id="W-001", event_type="TRANSFER",
             effective_date="2026-11-03", subsidiary="SUB-A", cost_center="CC-100",
             approved_by="HR-MGR-1", finance_reference_valid=True),
        dict(event_id="EVT-002", worker_id="W-002", event_type="TRANSFER",
             effective_date="2026-11-03", subsidiary="SUB-A", cost_center="BAD",
             approved_by="HR-MGR-1", finance_reference_valid=True),
        dict(event_id="EVT-003", worker_id="W-003", event_type="HIRE",
             effective_date="2026-11-03", subsidiary="SUB-B", cost_center="CC-200",
             approved_by="", finance_reference_valid=True),
    ]
    seen = set()
    for event in events:
        print(event["event_id"], validate_event(event, seen))


if __name__ == "__main__":
    demo()
