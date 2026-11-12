"""Aggregated fictional skills-gap prioritization; not individual people scoring."""
import csv
from pathlib import Path
DATA = Path(__file__).resolve().parents[1] / "data" / "synthetic_capability_gaps.csv"

def rank_gap(row):
    required, current, weight = (int(row[k]) for k in
        ("required_proficiency", "current_aggregate_proficiency", "priority_weight"))
    if not all(1 <= x <= 5 for x in (required, current, weight)):
        raise ValueError("proficiency and priority must be 1..5")
    return {"capability": row["capability"], "role_group": row["role_group"],
            "gap": max(0, required - current),
            "illustrative_priority": max(0, required - current) * weight}

def run(path=DATA):
    with open(path, newline="", encoding="utf-8") as f:
        rows = [rank_gap(row) for row in csv.DictReader(f)]
    return sorted(rows, key=lambda row: row["illustrative_priority"], reverse=True)

if __name__ == "__main__":
    for row in run():
        print(row)
    print("Aggregate learning priorities only; no individual assessment, employment selection or live HRIS.")