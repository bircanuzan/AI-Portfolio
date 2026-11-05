"""Illustrative risk-sensitive prioritization of hypothetical AI opportunities.
No customer data, no ROI claim, no LLM calls.
"""
import csv
from pathlib import Path

def score(row):
    """Higher impact/feasibility/confidence and lower risk improve priority."""
    impact = int(row["impact_1to5"])
    feasibility = int(row["feasibility_1to5"])
    confidence = int(row["confidence_1to5"])
    risk = int(row["risk_1to5"])
    if not all(1 <= n <= 5 for n in (impact, feasibility, confidence, risk)):
        raise ValueError("All ratings must be from 1 to 5")
    # Risk >= 4 triggers an independent do-not-pilot gate.
    return {"use_case": row["use_case"], "priority_score": impact * feasibility * confidence / (5 * risk),
            "pilot_eligible": risk <= 3}

def prioritize(rows):
    return sorted((score(row) for row in rows), key=lambda x: (x["pilot_eligible"], x["priority_score"]), reverse=True)

if __name__ == "__main__":
    path = Path(__file__).resolve().parents[1] / "data" / "enterprise_crm_synthetic_opportunities.csv"
    with path.open(newline="", encoding="utf-8") as f:
        for result in prioritize(list(csv.DictReader(f))):
            print(f"{result['use_case']}: score={result['priority_score']:.2f}, "
                  f"pilot_eligible={result['pilot_eligible']}")
