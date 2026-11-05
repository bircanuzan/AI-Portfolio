"""Deterministic, synthetic AI growth-agent QA gate; no Kraken or LLM integration."""
import json
import sys
from collections import Counter
from pathlib import Path

FIELDS = ("event_id", "requires_approval", "approved", "policy_ok", "output_checked")

def classify(event):
    if any(name not in event for name in FIELDS):
        raise ValueError("missing required event field")
    if not isinstance(event["event_id"], str) or not event["event_id"].strip():
        raise ValueError("invalid event id")
    if any(type(event[k]) is not bool for k in FIELDS[1:]):
        raise ValueError("approval/QA flags must be booleans")
    if not event["policy_ok"]:
        return "ESCALATE"
    if event["requires_approval"] and not event["approved"]:
        return "HOLD"
    if not event["output_checked"]:
        return "REVIEW"
    return "PASS"

def evaluate(events):
    seen = set()
    decisions = []
    for event in events:
        if event.get("event_id") in seen:
            raise ValueError("duplicate event id")
        decision = classify(event)
        seen.add(event["event_id"])
        decisions.append({"event_id": event["event_id"], "decision": decision})
    counts = dict(Counter(item["decision"] for item in decisions))
    return {"source": "synthetic_only", "count": len(decisions),
            "counts": counts, "decisions": decisions,
            "pass_rate": round(counts.get("PASS", 0) / len(decisions), 3) if decisions else None}

if __name__ == "__main__":
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("agent_events_synthetic.json")
    events = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(events, list):
        raise SystemExit("Expected a JSON array of synthetic events")
    print(json.dumps(evaluate(events), indent=2))
