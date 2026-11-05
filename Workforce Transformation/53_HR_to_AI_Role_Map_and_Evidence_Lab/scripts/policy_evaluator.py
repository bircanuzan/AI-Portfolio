"""Deterministic fictional HR policy router and 20-case reproducible evaluation.

Not an LLM, Claude, Copilot Studio, live HRIS or legal advice.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/hr_policy_20_evaluation_cases.csv"

def route(prompt):
    q = prompt.lower()
    if any(term in q for term in
           ("colleague", "another employee", "another person", "emirates id",
            "passport details", "medical record")):
        return "REFUSE", "PRIVACY"
    if any(term in q for term in
           ("exception", "appeal", "harassment", "urgent", "dispute", "complaint",
            "accommodation", "legal")):
        return "ESCALATE", "HUMAN"
    for terms, rule in [
        (("annual leave", "vacation"), "LEAVE"),
        (("sick leave",), "SICK"),
        (("remote work",), "REMOTE"),
        (("payroll cycle",), "PAYROLL"),
        (("overtime",), "OVERTIME"),
    ]:
        if any(term in q for term in terms):
            return "ANSWER", rule
    return "UNKNOWN", "UNKNOWN"

def main():
    with DATA.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 20, "Expected 20 human-authored fictional cases"
    correct = 0
    for record in rows:
        actual = route(record["prompt"])
        expected = (record["expected_route"], record["expected_policy_id"])
        ok = actual == expected
        correct += ok
        print(f"{record['case_id']} {'PASS' if ok else 'FAIL'} "
              f"expected={expected} actual={actual}")
    print(f"{correct}/20 matches; {len(rows)-correct} mismatches.")
    print("This tests simple offline routing only, NOT AI accuracy or legal correctness.")

if __name__ == "__main__":
    main()
