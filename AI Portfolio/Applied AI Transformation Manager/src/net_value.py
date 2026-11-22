"""Synthetic enterprise AI coding agent economics. Not a live Devin/model integration."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "synthetic_engineering_cohorts.csv"
INTS = ("eligible_engineers","activated_engineers","tasks_per_active_engineer_week")
NUMS = ("baseline_minutes_per_task","human_minutes_after_success","task_success_share",
        "review_minutes_per_attempt","rework_share_of_successful_tasks",
        "rework_minutes_per_reworked_task","exception_share","exception_minutes_per_exception",
        "oversight_hours_month","monthly_agent_license_usd",
        "monthly_enablement_support_usd","loaded_hourly_rate_usd")
FRACTIONS = ("task_success_share","rework_share_of_successful_tasks","exception_share")
GATES = ("baseline_measured","independent_quality_gate","security_signoff","executive_approval")

def parse(row):
    result = {"account": row["account"]}
    if not result["account"].strip():
        raise ValueError("Account is required")
    for k in INTS:
        result[k] = int(row[k])
        if result[k] < 0:
            raise ValueError(k + " cannot be negative")
    for k in NUMS:
        result[k] = float(row[k])
        if result[k] < 0:
            raise ValueError(k + " cannot be negative")
    for k in FRACTIONS:
        if result[k] > 1:
            raise ValueError(k + " must be <= 1")
    if result["activated_engineers"] > result["eligible_engineers"]:
        raise ValueError("Activated engineers exceed eligible engineers")
    if result["baseline_minutes_per_task"] <= 0:
        raise ValueError("Baseline minutes must be positive")
    for k in GATES:
        v = row[k].strip().lower()
        if v not in ("true", "false"):
            raise ValueError("Invalid boolean: " + k)
        result[k] = v == "true"
    return result

def load(path=DATA):
    with open(path, newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    if not rows:
        raise ValueError("No scenario data")
    return [parse(row) for row in rows]

def calculate(r, scenario="base", weeks_per_month=4.33):
    if scenario not in ("base","conservative") or weeks_per_month <= 0:
        raise ValueError("Invalid scenario or period")
    success = r["task_success_share"]
    review = r["review_minutes_per_attempt"]
    exception = r["exception_share"]
    oversight = r["oversight_hours_month"]
    if scenario == "conservative":
        success = max(0, success - 0.20)
        review += 5
        exception = min(1, exception + 0.10)
        oversight *= 1.30
    attempts = r["activated_engineers"] * r["tasks_per_active_engineer_week"] * weeks_per_month
    successes = attempts * success
    failures = attempts - successes
    baseline = attempts * r["baseline_minutes_per_task"] / 60
    human_exec = (successes * r["human_minutes_after_success"] +
                  failures * r["baseline_minutes_per_task"]) / 60
    human_review = attempts * review / 60
    rework = (successes * r["rework_share_of_successful_tasks"] *
              r["rework_minutes_per_reworked_task"]) / 60
    exceptions = attempts * exception * r["exception_minutes_per_exception"] / 60
    net = baseline - human_exec - human_review - rework - exceptions - oversight
    costs = r["monthly_agent_license_usd"] + r["monthly_enablement_support_usd"]
    missing = [k for k in GATES if not r[k]]
    return {
        "account": r["account"], "scenario": scenario,
        "eligible_engineers": r["eligible_engineers"],
        "activated_engineers": r["activated_engineers"],
        "activation_rate": round(r["activated_engineers"] / r["eligible_engineers"],4)
             if r["eligible_engineers"] else 0.0,
        "task_attempts_hypothesis": round(attempts,1),
        "baseline_human_hours_hypothesis": round(baseline,2),
        "future_human_execution_hours_hypothesis": round(human_exec,2),
        "review_hours_hypothesis": round(human_review,2),
        "rework_hours_hypothesis": round(rework,2),
        "exception_hours_hypothesis": round(exceptions,2),
        "oversight_hours_hypothesis": round(oversight,2),
        "net_capacity_hours_hypothesis": round(net,2),
        "monthly_agent_and_support_cost_usd": round(costs,2),
        "net_shadow_value_proxy_usd_not_savings": round(net * r["loaded_hourly_rate_usd"] - costs,2),
        "release_state": "HOLD_UNVERIFIED_EVIDENCE" if missing else "HUMAN_REVIEW_REQUIRED",
        "missing_evidence": missing,
        "actual_cash_savings_usd": None,
        "actual_roi": None,
        "headcount_reduction_authorized": False,
        "live_agent_integrated": False
    }

def report():
    return {"basis":"SYNTHETIC_OFFLINE_MODEL","production_deployed":False,
            "cases":[calculate(row,scenario=s) for row in load()
                     for s in ("base","conservative")]}

if __name__ == "__main__":
    print(json.dumps(report(),indent=2))
