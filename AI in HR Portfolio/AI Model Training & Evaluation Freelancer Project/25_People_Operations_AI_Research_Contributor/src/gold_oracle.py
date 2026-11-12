"""Synthetic workforce-planning answer checker; no actual Excel/HRIS access."""
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MONTHS=["2026-11","2026-12","2027-01","2027-02","2027-03","2027-04"]
DEPTS=["Operations","Analytics","Engineering","Sales"]
BENEFITS_BURDEN=.22
CAPS={"Operations":85000,"Analytics":75000,"Engineering":100000,"Sales":65000}

def csvrows(filename):
    with open(ROOT/"data"/filename,encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f))

def plan():
    roster=csvrows("synthetic_roster.csv")
    hires=csvrows("synthetic_hiring_plan.csv")
    exits=csvrows("synthetic_exit_plan.csv")
    result=[]
    for dept in DEPTS:
        people=[r for r in roster if r["Department"]==dept]
        starting_fte=sum(float(r["FTE"]) for r in people)
        base_annual=sum(float(r["Annual_Base_AED"])*float(r["FTE"]) for r in people)
        opening=starting_fte
        for month in MONTHS:
            h=[r for r in hires if r["Department"]==dept and r["Approval"]=="Approved" and r["Start_Month"]==month]
            x=[r for r in exits if r["Department"]==dept and r["Approval"]=="Approved" and r["End_Month"]==month]
            hired=sum(float(r["FTE"]) for r in h)
            left=sum(float(r["FTE"]) for r in x)
            closing=opening+hired-left
            approved_hire_cost=sum(float(r["Annual_Base_AED"])*float(r["FTE"]) for r in hires if
                r["Department"]==dept and r["Approval"]=="Approved" and r["Start_Month"]<=month)
            approved_exit_cost=sum(float(r["Annual_Base_AED"])*float(r["FTE"]) for r in exits if
                r["Department"]==dept and r["Approval"]=="Approved" and r["End_Month"]<=month)
            monthly_base=(base_annual+approved_hire_cost-approved_exit_cost)/12
            loaded=monthly_base*(1+BENEFITS_BURDEN)
            result.append({"department":dept,"month":month,"opening_fte":opening,
                 "approved_hires":hired,"approved_exits":left,"closing_fte":closing,
                 "monthly_base_aed":round(monthly_base,2),
                 "loaded_cost_aed":round(loaded,2),
                 "budget_variance_aed":round(CAPS[dept]-loaded,2)})
            opening=closing
    return result

if __name__=="__main__":
    for x in plan(): print(x)
