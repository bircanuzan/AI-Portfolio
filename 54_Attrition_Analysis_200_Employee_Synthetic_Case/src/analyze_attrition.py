"""Portfolio project 54: descriptive attrition analysis on fully synthetic employee data."""
import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DEFAULT_CSV = BASE / "data" / "synthetic_employee_cohort.csv"

def analyse(records):
    """Return fixed-cohort descriptive metrics. Raises on invalid synthetic input."""
    if not records:
        raise ValueError("Empty input")
    mandatory = {"employee_id", "cohort", "department", "exited", "engagement_score", "tenure_months"}
    if not mandatory.issubset(records[0]):
        raise ValueError("Missing required columns")
    if len({r["employee_id"] for r in records}) != len(records):
        raise ValueError("Duplicate employee IDs")
    by_department = defaultdict(lambda: [0, 0])
    exit_count = 0
    for row in records:
        if row["exited"] not in ("0", "1"):
            raise ValueError("Invalid departure flag")
        if not 1 <= int(row["engagement_score"]) <= 5 or int(row["tenure_months"]) < 0:
            raise ValueError("Invalid engagement/tenure")
        flag = int(row["exited"])
        exit_count += flag
        by_department[row["department"]][0] += 1
        by_department[row["department"]][1] += flag
    groups = [
        {"department": name, "employees": nums[0], "exits": nums[1],
         "exit_rate_pct": round(100 * nums[1] / nums[0], 1)}
        for name, nums in sorted(by_department.items())
    ]
    return {
        "is_synthetic": True, "records": len(records), "exits": exit_count,
        "exit_rate_pct": round(100 * exit_count / len(records), 1),
        "department_breakdown": groups,
        "caution": "Fixed cohort only; not a causal, predictive, or real company metric"
    }

def read_csv(path):
    with Path(path).open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", default=str(DEFAULT_CSV))
    parser.add_argument("--out", default="", help="Optional JSON output path")
    args = parser.parse_args()
    result = analyse(read_csv(args.csv))
    text = json.dumps(result, indent=2)
    print(text)
    if args.out:
        Path(args.out).write_text(text + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
