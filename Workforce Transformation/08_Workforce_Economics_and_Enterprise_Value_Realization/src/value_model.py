"""Synthetic task economics. Released capacity is NOT realized cash savings."""
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "synthetic_task_costs.csv"

def calculate(row):
    volume = float(row["monthly_volume"])
    minutes = float(row["minutes_per_task"])
    eligible = float(row["assistable_share"])
    saved = float(row["minutes_saved_per_assisted_task"])
    review = float(row["review_minutes_per_assisted_task"])
    cost = float(row["loaded_hourly_cost_aed"])
    platform = float(row["monthly_platform_cost_aed"])
    if any(v < 0 for v in (volume, minutes, saved, review, cost, platform)):
        raise ValueError("negative effort or cost not permitted")
    if not 0 <= eligible <= 1 or saved > minutes:
        raise ValueError("invalid eligibility or saved minutes")
    baseline_hours = volume * minutes / 60
    released_hours = volume * eligible * (saved - review) / 60
    labor_equivalent = released_hours * cost
    opportunity = labor_equivalent - platform
    return {
        "task": row.get("task", "Unspecified"),
        "baseline_hours_per_month": round(baseline_hours, 2),
        "modeled_net_hours_released_per_month": round(released_hours, 2),
        "modeled_labor_equivalent_aed_per_month": round(labor_equivalent, 2),
        "modeled_net_opportunity_aed_per_month": round(opportunity, 2),
        "verified_cash_savings_aed": 0,
        "actual_roi_verified": False,
        "decision": "HUMAN_FINANCE_AND_WORKFORCE_REVIEW_REQUIRED"
    }

def run(path=DATA):
    with open(path, newline="", encoding="utf-8") as f:
        return [calculate(row) for row in csv.DictReader(f)]

if __name__ == "__main__":
    for result in run():
        print(result)
    print("FICTIONAL DATA. Modeled opportunity is not realized ROI or budget savings.")