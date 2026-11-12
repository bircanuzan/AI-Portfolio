"""Scenario arithmetic on invented aggregate inputs; not AI prediction."""
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "synthetic_workforce_outlook.csv"

def estimate(row, demand_multiplier=1.0, enable_assistance=True):
    n = float(row["monthly_cases"])
    minutes = float(row["minutes_per_case"])
    eligible = float(row["assistable_share"]) if enable_assistance else 0.0
    success = float(row.get("assistance_success_rate", "1.0"))
    saved = float(row["minutes_saved_per_assisted_case"])
    review = float(row["review_minutes_per_assisted_case"])
    productive = float(row["productive_hours_per_fte"])
    supply = float(row["available_fte"])
    if n < 0 or minutes < 0 or not 0 <= eligible <= 1 or not 0 <= success <= 1:
        raise ValueError("invalid demand/eligibility")
    if not 0 <= saved <= minutes or review < 0 or productive <= 0 or supply < 0:
        raise ValueError("invalid inputs")
    if demand_multiplier <= 0:
        raise ValueError("invalid multiplier")
    baseline_hours = n * demand_multiplier * minutes / 60
    # Only successful assisted cases save draft time. Every eligible attempt incurs review.
    # A zero success rate can INCREASE human effort (AI review overhead).
    assisted_hours = n * demand_multiplier * (minutes - eligible * success * saved + eligible * review) / 60
    return {"year": row["year"], "function": row["function"],
            "baseline_fte": round(baseline_hours / productive, 2),
            "scenario_fte": round(assisted_hours / productive, 2),
            "available_fte": supply,
            "supply_gap_fte": round(assisted_hours / productive - supply, 2)}

def run(path=DATA):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return [{"reference": estimate(row, enable_assistance=False),
             "guarded_assist": estimate(row),
             "demand_shock": estimate(row, demand_multiplier=1.2)} for row in rows]

if __name__ == "__main__":
    for r in run():
        print(r)
    print("SYNTHETIC assumptions: NOT a production forecast, staffing recommendation, or observed AI improvement.")