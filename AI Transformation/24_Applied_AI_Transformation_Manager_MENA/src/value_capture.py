"""Synthetic coding-agent enterprise adoption model: hypotheses, NOT realized savings."""
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
COUNTS=("eligible_engineers","activated_engineers","eligible_tasks_per_engineer_week")
NUMS=("baseline_minutes","assisted_minutes","quality_factor","realization_factor","loaded_rate_usd_hour","monthly_agent_cost_usd")
def load_accounts(path):
    with open(path,encoding="utf-8",newline="") as f: data=list(csv.DictReader(f))
    if not data: raise ValueError("No customer cohorts")
    out=[]
    for row in data:
        for k in COUNTS: row[k]=int(row[k])
        for k in NUMS: row[k]=float(row[k])
        if any(row[k]<0 for k in (*COUNTS,*NUMS)):raise ValueError("Negative inputs")
        if row["activated_engineers"]>row["eligible_engineers"]:raise ValueError("Activation exceeds eligible population")
        if any(row[k]>1 for k in ("quality_factor","realization_factor")):raise ValueError("Factors must be 0..1")
        if row["assisted_minutes"]>row["baseline_minutes"]:raise ValueError("Increased handling time needs separate negative impact model")
        out.append(row)
    return out
def model(row,weeks_per_month=4.33):
    if weeks_per_month <= 0 or any(row[k] < 0 for k in (*COUNTS, *NUMS)):
        raise ValueError("Negative fields or invalid weeks-per-month")
    if row["activated_engineers"] > row["eligible_engineers"]:
        raise ValueError("Activation cannot exceed eligible engineers")
    if any(row[k] > 1 for k in ("quality_factor", "realization_factor")):
        raise ValueError("Quality and realization factors must be 0..1")
    if row["assisted_minutes"] > row["baseline_minutes"]:
        raise ValueError("Assisted time cannot exceed baseline in this positive-only model")
    active=row["activated_engineers"]
    activation=active/row["eligible_engineers"] if row["eligible_engineers"] else 0.0
    raw_hours=active*row["eligible_tasks_per_engineer_week"]*weeks_per_month*(row["baseline_minutes"]-row["assisted_minutes"])/60
    risk_adjusted=raw_hours*row["quality_factor"]*row["realization_factor"]
    gross=risk_adjusted*row["loaded_rate_usd_hour"]
    return {"account":row["account"],"activation_rate":round(activation,4),
        "raw_time_delta_hours_hypothesis":round(raw_hours,2),
        "risk_adjusted_capacity_hours_hypothesis":round(risk_adjusted,2),
        "monthly_capacity_value_hypothesis_usd":round(gross,2),
        "net_capacity_value_hypothesis_after_agent_cost_usd":round(gross-row["monthly_agent_cost_usd"],2),
        "realized_savings_claim":"None. Requires independent baseline and finance certification."}
if __name__=="__main__":
    for x in load_accounts(ROOT/"data/synthetic_accounts.csv"):print(model(x))
