"""Independent synthetic monthly workforce forecaster + scenarios; NOT employee risk modelling."""
import argparse
import csv
import json
from datetime import date
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"data"/"synthetic_monthly_workforce.csv"

def next_month(ym):
    year,mon=map(int,ym.split("-"))
    return f"{year+ (mon==12):04d}-{1 if mon==12 else mon+1:02d}"

def validate(rows):
    if len(rows)<12:raise ValueError("Need at least 12 chronological synthetic months")
    expected={"month","start_headcount","hires","exits","end_headcount"}
    previous=None
    for i,row in enumerate(rows):
        if set(row)!=expected:raise ValueError("Missing or extra fields")
        try:
            year,month=map(int,row["month"].split("-"))
            if date(year,month,1).strftime("%Y-%m")!=row["month"]:
                raise ValueError
        except (ValueError,KeyError) as exc:
            raise ValueError("Invalid month") from exc
        for col in ("start_headcount","hires","exits","end_headcount"):
            if type(row[col]) is not int or row[col]<0:raise ValueError(f"Bad {col}")
        if row["exits"]>row["start_headcount"]:
            raise ValueError("Exits greater than opening headcount")
        if row["end_headcount"]!=row["start_headcount"]+row["hires"]-row["exits"]:
            raise ValueError("Workforce balance mismatch")
        if previous is not None:
            if row["month"]!=next_month(previous["month"]):
                raise ValueError("Months missing, repeated or unsorted")
            if row["start_headcount"]!=previous["end_headcount"]:
                raise ValueError("Opening workforce does not match prior close")
        previous=row
    return True

def predict_exits(history,method):
    if not history:raise ValueError("No historical observations")
    if method=="last":return history[-1]
    if method=="mean3":return round(sum(history[-3:])/min(3,len(history)))
    raise ValueError("Unknown method")

def backtest(rows,holdout=6):
    validate(rows)
    if holdout<1 or len(rows)-holdout<6:raise ValueError("Insufficient training history")
    evaluated=[]
    for method in ("last","mean3"):
        errors=[]
        for i in range(len(rows)-holdout,len(rows)):
            # Every forecast uses actual history strictly BEFORE the scored month.
            predicted=predict_exits([r["exits"] for r in rows[:i]],method)
            errors.append(abs(rows[i]["exits"]-predicted))
        evaluated.append({"method":method,"holdout_months":holdout,
                          "mae_exits":round(sum(errors)/len(errors),1)})
    return sorted(evaluated,key=lambda x:(x["mae_exits"],x["method"]))

def project(rows,method,horizon=6,hires=7,target=220,capacity_factor=0.92):
    validate(rows)
    if not 1<=horizon<=24 or hires<0 or target<0 or not 0<capacity_factor<=1:
        raise ValueError("Invalid scenario assumptions")
    obs=[r["exits"] for r in rows]
    baseline_forecast=[]
    for _ in range(horizon):
        value=predict_exits(obs,method)
        baseline_forecast.append(value)
        obs.append(value)  # recursive *baseline forecasts*, not future actuals
    scenarios=[]
    for name,mult in (("baseline",1.0),("retention_hypothesis",0.85),("stress",1.2)):
        hc=rows[-1]["end_headcount"]
        month=rows[-1]["month"]
        steps=[]
        for base in baseline_forecast:
            month=next_month(month)
            exits=min(hc,max(0,round(base*mult)))
            start=hc
            hc+=hires-exits
            steps.append({"month":month,"start_headcount":start,"planned_hires":hires,
                          "model_baseline_exits":base,"assumed_exits":exits,"end_headcount":hc})
        scenarios.append({"name":name,"exit_multiplier":mult,"months":steps,
            "final_headcount":hc,"gap_to_hypothetical_target_220":target-hc,
            "capacity_fte_if_0_92_availability":round(hc*capacity_factor,1)})
    return baseline_forecast,scenarios

def report(rows):
    validation=backtest(rows)
    selected=validation[0]["method"]
    projected,scenarios=project(rows,selected)
    return {
      "disclosure":"All monthly history, forecasts, scenarios, target and capacity assumptions are invented. Illustrative backtest scores cannot establish real-world predictive performance.",
      "source":"54_Attrition_Analysis_200_Employee_Synthetic_Case/data/synthetic_monthly_workforce.csv",
      "distinct_from_200_employee_quarterly_cohort":True,
      "history_months":len(rows),"last_observed_month":rows[-1]["month"],
      "start_of_projection_headcount":rows[-1]["end_headcount"],
      "validation":{"type":"expanding-origin six-month retrospective holdout",
        "candidates":validation,"chosen_method":selected,"metric":"monthly exit count mean absolute error",
        "limits":"single synthetic trajectory, six holdout months, no external validation"},
      "assumptions":{"planned_monthly_hires":7,"projection_horizon_months":6,
                     "target_headcount":220,"capacity_factor":0.92,"human_review_required":True},
      "baseline_exit_forecast_by_month":projected,
      "scenarios":scenarios
    }

def read_source(path):
    with Path(path).open(encoding="utf-8-sig",newline="") as f:
        inp=csv.DictReader(f)
        rows=[]
        for raw in inp:
            if set(raw)!={"month","start_headcount","hires","exits","end_headcount"}:
                raise ValueError("Unexpected CSV columns")
            try:
                row={"month":raw["month"],**{c:int(raw[c]) for c in
                     ("start_headcount","hires","exits","end_headcount")}}
            except (TypeError,ValueError) as exc:
                raise ValueError("Invalid non-integer count") from exc
            rows.append(row)
        return rows

def main():
    cli=argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--csv",default=str(SOURCE))
    cli.add_argument("--out",default="")
    args=cli.parse_args()
    content=json.dumps(report(read_source(args.csv)),indent=2)+"\n"
    if args.out:Path(args.out).write_text(content,encoding="utf-8")
    print(content,end="")

if __name__=="__main__":main()
