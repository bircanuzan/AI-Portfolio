"""Synthetic Copilot business adoption KPI illustration — NOT a tenant analytics export.

No employee-level monitoring, external dependencies, real telemetry or actual value claim.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NUMERIC = ("week", "licensed_users", "active_users", "trained_users",
           "reviewed_outputs", "correct_outputs", "verified_minutes_released")

def load(path=None):
    p = Path(path) if path else ROOT / "data" / "synthetic_adoption_metrics.csv"
    with open(p, encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    if not rows:
        raise ValueError("No adoption data")
    seen = set()
    for row in rows:
        for key in NUMERIC:
            row[key] = int(row[key])
            if row[key] < 0:
                raise ValueError("Negative field " + key)
        if row["week"] < 1:
            raise ValueError("Invalid week")
        if row["active_users"] > row["licensed_users"]:
            raise ValueError("Active cannot exceed licensed")
        if row["trained_users"] > row["licensed_users"]:
            raise ValueError("Trained cannot exceed licensed")
        if row["correct_outputs"] > row["reviewed_outputs"]:
            raise ValueError("Correct cannot exceed reviewed")
        key = (row["cohort"], row["week"])
        if key in seen:
            raise ValueError("Duplicate cohort-week")
        seen.add(key)
    return rows

def report(rows, week=4):
    period = [r for r in rows if r["week"] == week]
    if not period:
        raise ValueError("No rows for requested week")
    for row in period:
        if (row["active_users"] > row["licensed_users"] or
                row["trained_users"] > row["licensed_users"] or
                row["correct_outputs"] > row["reviewed_outputs"]):
            raise ValueError("Inconsistent active, training or quality counts")
    licensed = sum(r["licensed_users"] for r in period)
    active = sum(r["active_users"] for r in period)
    trained = sum(r["trained_users"] for r in period)
    reviewed = sum(r["reviewed_outputs"] for r in period)
    correct = sum(r["correct_outputs"] for r in period)
    minutes = sum(r["verified_minutes_released"] for r in period)
    return {
        "week": week,
        "licensed": licensed,
        "active": active,
        "adoption_rate": round(active / licensed, 4) if licensed else None,
        "training_coverage": round(trained / licensed, 4) if licensed else None,
        "reviewed_outputs": reviewed,
        "quality_pass_rate": round(correct / reviewed, 4) if reviewed else None,
        "hypothetical_hours_released": round(minutes / 60, 2),
        "limitation": "Fictional measurements, not real telemetry, controlled outcomes or cash savings."
    }

if __name__ == "__main__":
    for w in (1, 2, 3, 4):
        print(report(load(), week=w))
