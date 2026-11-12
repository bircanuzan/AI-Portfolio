"""Synthetic descriptive cohort summary; NOT a psychometric scoring or selection system."""
import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean
from decimal import Decimal, ROUND_HALF_UP

HERE = Path(__file__).resolve().parent
DATA = HERE / "03_Synthetic_Assessment_Results.csv"
FIELDS = [
    "numerical_index", "verbal_index", "abstract_index",
    "structured_interview_index", "work_sample_index"
]

def summarize():
    with DATA.open(newline="", encoding="utf-8") as f:
        items = list(csv.DictReader(f))
    assert len(items) == 12, "Expected twelve fictional cases"
    assert len({r["case_id"] for r in items}) == len(items), "Duplicate case_id"
    groups = defaultdict(list)
    for row in items:
        assert row["purpose"] in {"Hiring", "Promotion", "Succession"}
        assert row["administration"] in {"Remote", "Onsite"}
        for field in FIELDS + ["planning_style", "collaboration_style", "adaptability_style"]:
            value = float(row[field])
            assert 0 <= value <= 100, f"Value outside demo range: {field}"
        groups[row["purpose"]].append(row)
    assert all(len(group) == 4 for group in groups.values())
    return {name: {"n": len(group), **{
        field: float(Decimal(str(mean(float(r[field]) for r in group))).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))
        for field in FIELDS
    }} for name, group in sorted(groups.items())}

if __name__ == "__main__":
    print("FICTIONAL DATA — NOT VALIDATED PSYCHOMETRICS / NOT FOR EMPLOYMENT DECISIONS")
    for group, summary in summarize().items():
        print(group, summary)
