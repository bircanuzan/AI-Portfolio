"""Transparent fictional business-case calculator; no observed or cash savings."""


def evaluate(volume=500, old_minutes=22, new_minutes=13, cost_per_hour=100,
             monthly_run_cost=2500, initial_cost=42000, realization=1.0):
    if min(volume, old_minutes, new_minutes, cost_per_hour, monthly_run_cost, initial_cost) < 0:
        raise ValueError("Inputs must be nonnegative")
    if not 0 <= realization <= 1:
        raise ValueError("Realization must be between 0 and 1")
    hours = volume * (old_minutes - new_minutes) / 60
    gross = hours * cost_per_hour * realization
    net = gross - monthly_run_cost
    return {
        "hours_released_monthly": round(hours, 2),
        "capacity_value_monthly_aed": round(gross, 2),
        "net_monthly_aed": round(net, 2),
        "simple_payback_months": round(initial_cost / net, 2) if net > 0 else None,
        "year_one_net_aed": round(net * 12 - initial_cost, 2),
        "year_one_roi_percent": round((net * 12 - initial_cost) / initial_cost * 100, 2) if initial_cost else None,
    }


if __name__ == "__main__":
    print("Base assumption:", evaluate())
    print("Conservative 60% realization:", evaluate(realization=0.60))
