"""Illustrative Modern Workplace commercial model, not a vendor quote."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load_rates(path=None):
    p = Path(path) if path else ROOT / "data" / "synthetic_service_towers.csv"
    with open(p, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows: raise ValueError("At least one service tower required")
    names = set()
    for row in rows:
        if row["service_tower"] in names: raise ValueError("Duplicate tower")
        names.add(row["service_tower"])
        row["base_monthly_aed_per_user"] = float(row["base_monthly_aed_per_user"])
        if row["base_monthly_aed_per_user"] < 0: raise ValueError("Negative cost")
    return rows

def estimate(users, monthly_tower_rates, fixed_annual_governance_aed=600000,
             one_time_transition_aed=1800000, years=3, contingency_rate=0.10):
    if users <= 0 or int(users) != users: raise ValueError("Users must be positive integer")
    if years <= 0 or int(years) != years: raise ValueError("Years must be positive integer")
    if any(x < 0 for x in (fixed_annual_governance_aed, one_time_transition_aed)):
        raise ValueError("Costs must be non-negative")
    if not 0 <= contingency_rate <= 1: raise ValueError("Contingency 0 to 1 required")
    if not monthly_tower_rates or any(x < 0 for x in monthly_tower_rates):
        raise ValueError("Invalid tower rates")
    monthly_per_user = sum(monthly_tower_rates)
    recurring_annual = users * monthly_per_user * 12 + fixed_annual_governance_aed
    transition_with_contingency = one_time_transition_aed * (1 + contingency_rate)
    return {
        "supported_users": int(users),
        "monthly_per_user_aed": round(monthly_per_user, 2),
        "annual_recurring_aed": round(recurring_annual, 2),
        "transition_with_contingency_aed": round(transition_with_contingency, 2),
        "total_term_cost_aed": round(years * recurring_annual + transition_with_contingency, 2),
        "excluded": "Microsoft, DaaS device purchase, AVD cloud usage, tax, client retained costs, incumbent exit",
        "integrity": "Synthetic planning scenario only, not a commercial quote."
    }

if __name__ == "__main__":
    rates = [x["base_monthly_aed_per_user"] for x in load_rates()]
    for u in (3600, 4500, 5400):
        print(estimate(u, rates))
