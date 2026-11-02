#!/usr/bin/env python3
"""Fictional fintech integration TPM dashboard. Standard library only."""
import argparse
import csv
import json
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def records(filename):
    with (DATA / filename).open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def calculate(as_of, milestones, raid, features, capacity):
    """Produce a traceable scorecard without treating planned dates as actuals."""
    day = date.fromisoformat(as_of)
    clients = sorted({row["client"] for row in milestones})
    report = {"as_of": as_of, "disclosure": "Synthetic portfolio data only", "clients": {}}
    total_done = 0
    total_on_time = 0
    total_late_open = 0
    total_gap = 0
    for client in clients:
        ms = [m for m in milestones if m["client"] == client]
        issues = [r for r in raid if r["client"] == client and r["status"] == "Open"]
        reqs = [f for f in features if f["client"] == client]
        cap = [c for c in capacity if c["client"] == client and
               date.fromisoformat(c["period_start"]) <= day <= date.fromisoformat(c["period_end"])]
        completed = [m for m in ms if m["status"] == "Complete" and m["actual_date"] and
                     date.fromisoformat(m["actual_date"]) <= day]
        on_time = [m for m in completed if m["actual_date"] <= m["planned_date"]]
        overdue = [m["id"] for m in ms if m["status"] != "Complete" and
                   date.fromisoformat(m["planned_date"]) < day]
        p1 = [r["id"] for r in issues if r["priority"] == "P1"]
        high = [r["id"] for r in issues if r["priority"] == "High"]
        blocked = [r["id"] for r in reqs if r["status"] == "Blocked"]
        gap = sum(max(0, int(c["weekly_demand_hours"]) - int(c["weekly_capacity_hours"])) for c in cap)
        rag = "Red" if p1 or len(overdue) >= 2 else "Amber" if overdue or high or gap else "Green"
        report["clients"][client] = {
            "rag": rag, "milestones_total": len(ms), "completed": len(completed),
            "completed_on_time": len(on_time), "overdue_open_ids": overdue,
            "open_p1_ids": p1, "open_high_ids": high, "blocked_feature_ids": blocked,
            "capacity_gap_hours_per_week": gap,
            "note": "RAG is a coordination indicator, never a production launch authorization",
        }
        total_done += len(completed)
        total_on_time += len(on_time)
        total_late_open += len(overdue)
        total_gap += gap
    report["portfolio"] = {
        "milestones_total": len(milestones), "completed": total_done,
        "completed_on_time": total_on_time,
        "on_time_completion_pct": round(100 * total_on_time / total_done, 1) if total_done else None,
        "overdue_open": total_late_open,
        "open_p1_count": sum(len(c["open_p1_ids"]) for c in report["clients"].values()),
        "blocked_feature_count": sum(len(c["blocked_feature_ids"]) for c in report["clients"].values()),
        "capacity_gap_hours_per_week": total_gap,
    }
    return report


def main():
    parser = argparse.ArgumentParser(description="Synthetic enterprise integration TPM reporting")
    parser.add_argument("--as-of", default="2026-10-29", help="ISO date")
    parser.add_argument("--output", help="Optional JSON output file")
    args = parser.parse_args()
    results = calculate(args.as_of, records("milestones.csv"), records("raid_register.csv"),
                        records("feature_requests.csv"), records("capacity_plan.csv"))
    rendered = json.dumps(results, indent=2)
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
        print(f"Saved {args.output}")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
