"""Auditable descriptive analysis of an entirely fictional 200-employee dataset."""
import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/synthetic_200_employees.csv"

def pct(num, den):
    return round(100 * num / den, 1) if den else 0

def main():
    with DATA.open(newline="", encoding="utf-8") as fh:
        records = list(csv.DictReader(fh))
    assert len(records) == 200, "Expected exactly 200 fictional records"
    ids = [r["employee_id"] for r in records]
    assert len(ids) == len(set(ids)), "Duplicate employee IDs"
    assert all(r["attrited"] in ("0", "1") for r in records)
    totals = defaultdict(lambda: [0, 0])
    for r in records:
        group = r["department"]
        totals[group][0] += 1
        totals[group][1] += int(r["attrited"])
    exits = sum(int(r["attrited"]) for r in records)
    print(f"Employees: {len(records)}; fictional exits: {exits}; aggregate: {pct(exits, len(records))}%")
    for group, (n, left) in sorted(totals.items()):
        print(f"{group}: {left}/{n} = {pct(left, n)}%")
    print("DESCRIPTIVE ONLY: generated data, no causality, no model validation,")
    print("no employee ranking, no production insights or actual retention outcomes.")

if __name__ == "__main__":
    main()
