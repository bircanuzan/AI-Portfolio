"""Synthetic learning outcomes analysis; standard-library-only. Run from this folder."""
from pathlib import Path
import csv
from statistics import mean

path = Path(__file__).with_name("synthetic_learning_results.csv")
with path.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
assert len(rows) > 0
complete = [r for r in rows if r["completed"] == "1"]
def num(r, key):
    return float(r[key].strip())
paired = [r for r in complete if r["pre_score"].strip() and r["post_score"].strip()]
proficient = [
    r for r in complete
    if r["capstone_rubric"].strip()
    and num(r, "capstone_rubric") >= 3.0
    and r["privacy_pass"] == "1"
]
responses = [num(r, "feedback_1to5") for r in complete if r["feedback_1to5"].strip()]
print("SOURCE: fictional learner scores; no actual LMS data")
print(f"Completion: {len(complete)}/{len(rows)} = {100 * len(complete) / len(rows):.1f}%")
print(f"Average pre/post uplift (paired, percentage points): {mean(num(r,'post_score') - num(r,'pre_score') for r in paired):.1f}")
print(f"Capstone readiness among completers: {len(proficient)}/{len(complete)} = {100 * len(proficient) / len(complete):.1f}%")
print(f"Average feedback score (1–5): {mean(responses):.2f}" if responses else "Feedback not collected")
