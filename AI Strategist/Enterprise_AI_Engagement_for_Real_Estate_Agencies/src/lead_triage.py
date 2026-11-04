"""Synthetic, consent-aware lead workflow baseline. No model calls or CRM access."""
import csv
import json
import sys
from datetime import datetime

SUPPORTED_LANGUAGES = {"en", "ar"}

def parse_ts(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00")) if value else None

def workflow_decision(row):
    """Deterministic routing only; no outbound message is created or sent."""
    if str(row.get("consent_to_contact", "")).strip().lower() != "true":
        return {"lead_id": row.get("lead_id"), "action": "hold_no_consent", "draft_allowed": False}
    if row.get("language") not in SUPPORTED_LANGUAGES:
        return {"lead_id": row.get("lead_id"), "action": "manual_language_review", "draft_allowed": False}
    if not row.get("listing_id"):
        return {"lead_id": row.get("lead_id"), "action": "manual_listing_check", "draft_allowed": False}
    if row.get("response_at"):
        return {"lead_id": row.get("lead_id"), "action": "already_answered", "draft_allowed": False}
    return {"lead_id": row.get("lead_id"), "action": "human_review_pending", "draft_allowed": True}

def summarize(rows):
    """Observational instrumentation, not causal AI impact."""
    eligible = [r for r in rows if str(r.get("consent_to_contact", "")).lower() == "true"]
    minutes = []
    for row in eligible:
        start, finish = parse_ts(row.get("received_at")), parse_ts(row.get("response_at"))
        if start and finish and finish >= start:
            minutes.append((finish - start).total_seconds()/60)
    minutes.sort()
    median = None
    if minutes:
        m=len(minutes)//2
        median = minutes[m] if len(minutes)%2 else (minutes[m-1]+minutes[m])/2
    return {
        "eligible_leads": len(eligible),
        "answered_leads": sum(bool(r.get("response_at")) for r in eligible),
        "booked_viewings": sum(str(r.get("booked_viewing", "")).lower() == "true" for r in eligible),
        "booking_rate": round(sum(str(r.get("booked_viewing", "")).lower() == "true" for r in eligible) / len(eligible), 4) if eligible else None,
        "median_response_minutes": median,
        "workflows": [workflow_decision(r) for r in rows]
    }

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv)>1 else "data/synthetic_leads.csv"
    with open(path, newline="", encoding="utf-8") as handle:
        rows=list(csv.DictReader(handle))
    print(json.dumps(summarize(rows), indent=2))
