"""Fictional human-data workflow reporting, no individual performance claims."""
import csv
import statistics
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_STATUS = {"accepted", "needs_review", "blocked"}

def load_events(path=None):
    p = Path(path) if path else ROOT / "data" / "operations_events.csv"
    with p.open(encoding="utf-8", newline="") as f:
        data = list(csv.DictReader(f))
    if not data:
        raise ValueError("No work records")
    seen = set()
    for row in data:
        if not row["case_id"] or row["case_id"] in seen:
            raise ValueError("Missing or duplicate case ID")
        seen.add(row["case_id"])
        row["processing_minutes"] = int(row["processing_minutes"])
        row["rework_flag"] = int(row["rework_flag"])
        if row["processing_minutes"] < 0 or row["rework_flag"] not in (0, 1):
            raise ValueError("Invalid time / rework flag")
        if row["status"] not in ALLOWED_STATUS:
            raise ValueError("Invalid case status")
    return data

def report(events):
    if not events:
        raise ValueError("Missing events")
    if any(row["status"] not in ALLOWED_STATUS for row in events):
        raise ValueError("Invalid case status")
    if any(row["rework_flag"] not in (0, 1) or row["processing_minutes"] < 0 for row in events):
        raise ValueError("Invalid time or rework flag")
    counts = Counter(row["status"] for row in events)
    n = len(events)
    total = sum(row["processing_minutes"] for row in events)
    return {
        "cases": n,
        "accepted": counts["accepted"],
        "needs_review": counts["needs_review"],
        "blocked": counts["blocked"],
        "acceptance_rate": round(counts["accepted"] / n, 4),
        "rework_rate": round(sum(row["rework_flag"] for row in events) / n, 4),
        "mean_handling_minutes": round(total / n, 2),
        "median_handling_minutes": statistics.median(row["processing_minutes"] for row in events),
        "days_covered": len({row["day"] for row in events}),
        "limitations": "Simulated work items and handling times, not actual annotator productivity."
    }

if __name__ == "__main__":
    import json
    print(json.dumps(report(load_events()), indent=2))
