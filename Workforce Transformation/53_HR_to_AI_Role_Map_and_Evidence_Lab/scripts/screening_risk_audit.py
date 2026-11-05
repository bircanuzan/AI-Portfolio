"""Risk-register audit: not a model fairness test or live ATS measurement."""
import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/screening_risk_cases.csv"

def main():
    with DATA.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 12
    counts = Counter(row["severity"] for row in rows)
    unresolved = [r for r in rows if r["status"] != "CONTROLLED"
                  and r["severity"] in ("HIGH", "CRITICAL")]
    print("Synthetic risk scenarios:", len(rows), "; by severity:", dict(counts))
    print("Unresolved high/critical issues:", len(unresolved))
    print("Proposed release gate:", "HOLD" if unresolved else "REVIEW")
    for r in unresolved:
        print(f"  {r['case_id']} {r['severity']}: {r['failure_mode']}")
    print("No vendor algorithm was executed, audited, certified or found noncompliant.")

if __name__ == "__main__":
    main()
