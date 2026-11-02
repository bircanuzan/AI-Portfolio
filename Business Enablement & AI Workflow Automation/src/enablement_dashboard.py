"""Offline MoonTech-inspired enablement metrics from SYNTHETIC campaign rows."""
from pathlib import Path
import csv
import json

def report(rows):
    rows=list(rows)
    if not rows:
        raise ValueError("At least one campaign is required")
    ids=[r["campaign_id"] for r in rows]
    if len(ids)!=len(set(ids)):
        raise ValueError("Duplicate campaign_id")
    required={"complete","pending","awaiting_approval"}
    if any(r["status"] not in required for r in rows):
        raise ValueError("Invalid campaign status")
    completed=[r for r in rows if r["status"]=="complete"]
    # This is not realized savings; the before/after data are fictional examples.
    gross_illustrative_minutes=sum(int(r["minutes_before"])-int(r["minutes_after"]) for r in completed)
    return {
        "sample_count":len(rows),
        "completed_count":len(completed),
        "completion_rate":round(len(completed)/len(rows),3),
        "intake_validation_rate":round(sum(r["validated"].lower()=="true" for r in rows)/len(rows),3),
        "approved_count":sum(r["approved"].lower()=="true" for r in rows),
        "illustrative_completed_time_difference_minutes":gross_illustrative_minutes,
        "status":"synthetic illustration; not measured company results",
    }

if __name__=="__main__":
    source=Path(__file__).resolve().parents[1]/"data"/"synthetic_campaigns.csv"
    with source.open(newline="",encoding="utf-8") as f:
        print(json.dumps(report(csv.DictReader(f)),indent=2))
