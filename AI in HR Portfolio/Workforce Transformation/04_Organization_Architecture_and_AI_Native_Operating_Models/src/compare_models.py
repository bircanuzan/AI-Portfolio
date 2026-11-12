"""Illustrative organizational option screening. Synthetic only; not a workforce decision engine."""
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "organization_options.csv"

def score_option(row):
    required = ("option", "handoffs", "accountability_gaps", "unmitigated_high_risks",
                "learning_pathways", "coordination_cost_index")
    if any(k not in row for k in required):
        raise ValueError("missing schema field")
    vals = {k: int(row[k]) for k in required[1:]}
    if any(v < 0 for v in vals.values()) or vals["learning_pathways"] not in (0, 1):
        raise ValueError("invalid synthetic input")
    if vals["accountability_gaps"] > 0 or vals["unmitigated_high_risks"] > 0:
        return {"option": row["option"], "status": "HOLD", "score": None}
    if vals["learning_pathways"] != 1:
        return {"option": row["option"], "status": "HOLD_NO_LEARNING", "score": None}
    score = 100 - 5 * vals["handoffs"] - 3 * vals["coordination_cost_index"]
    return {"option": row["option"], "status": "DISCUSS", "score": score}

def load_options(path=DATA):
    with open(path, newline="", encoding="utf-8") as f:
        return [score_option(row) for row in csv.DictReader(f)]

if __name__ == "__main__":
    for option in load_options():
        print(option)
    print("DISCUSSION AID ONLY: human executive approval always required.")