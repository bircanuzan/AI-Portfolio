"""KPI definitions over entirely synthetic case records."""
import csv
from pathlib import Path
from statistics import median
ROOT=Path(__file__).resolve().parents[1]

def summarize(path=None):
    p=Path(path) if path else ROOT/"data/synthetic_case_operations.csv"
    with open(p,encoding="utf-8",newline="") as stream:
        cases=list(csv.DictReader(stream))
    if not cases: raise ValueError("No cases")
    for c in cases:
        for col in ("cycle_hours","manual_touches","manual_minutes","sla_met","human_review","reopened"):
            c[col]=float(c[col])
            if c[col]<0: raise ValueError("Negative KPI input")
        for col in ("sla_met","human_review","reopened"):
            if c[col] not in (0.,1.): raise ValueError("Expected binary flag "+col)
    n=len(cases)
    low_risk=[x for x in cases if x["category"]=="generic_faq"]
    return {
        "cases": n,
        "median_cycle_hours": median(x["cycle_hours"] for x in cases),
        "sla_attainment": sum(x["sla_met"] for x in cases)/n,
        "human_review_rate":sum(x["human_review"] for x in cases)/n,
        "reopen_rate":sum(x["reopened"] for x in cases)/n,
        "manual_hours_observed_synthetic":round(sum(x["manual_minutes"] for x in cases)/60,2),
        "generic_faq_count":len(low_risk),
        "note":"Fictional baseline only; NOT verified time or cost savings."
    }

if __name__=="__main__":
    print(summarize())
