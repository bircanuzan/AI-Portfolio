"""Illustrative people KPI calculations for invented data, NOT SAP extraction."""
import csv
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
INT_FIELDS = ("opening_headcount","hires","exits","closing_headcount","approved_open_reqs","unique_trained","eligible_employees")

def ratio(n,d):
    return n/d if d else 0.0

def load_rows(path):
    with open(path,encoding="utf-8",newline="") as stream:
        rows=list(csv.DictReader(stream))
    if not rows: raise ValueError("No synthetic data")
    result=[]
    for r in rows:
        for f in INT_FIELDS:
            r[f]=int(r[f])
            if r[f]<0: raise ValueError("Negative "+f)
        if r["opening_headcount"]+r["hires"]-r["exits"] != r["closing_headcount"]:
            raise ValueError("Headcount reconciliation failed: "+r["business_unit"])
        if r["unique_trained"]>r["eligible_employees"]:
            raise ValueError("Trained count exceeds eligible population")
        result.append(r)
    return result

def calculate(row):
    avg=(row["opening_headcount"]+row["closing_headcount"])/2
    return {
        "business_unit":row["business_unit"], "period":row["period"],
        "avg_headcount":avg,
        "attrition_rate":ratio(row["exits"],avg),
        "vacancy_pressure_proxy":ratio(row["approved_open_reqs"],row["closing_headcount"]+row["approved_open_reqs"]),
        "learning_reach":ratio(row["unique_trained"],row["eligible_employees"])
    }

if __name__=="__main__":
    for row in load_rows(ROOT/"data/synthetic_workforce.csv"):
        print(calculate(row))
