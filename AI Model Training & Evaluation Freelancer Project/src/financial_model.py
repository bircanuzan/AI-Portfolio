"""Synthetic three-year business-case calculator; pure Python stdlib."""
import argparse
import json
from pathlib import Path

def calculate(a, adoption=1.0, cost_factor=1.0):
    horizon = int(a["horizon_years"])
    if horizon < 1 or a["discount_rate"] <= -1 or adoption < 0 or cost_factor < 0:
        raise ValueError("Invalid horizon, discount rate, or scenario multiplier")
    upfront = float(a["upfront_investment"])
    gross = float(a["annual_gross_benefit_base"]) * adoption
    operating = float(a["annual_operating_cost_base"]) * cost_factor
    if upfront < 0 or gross < 0 or operating < 0:
        raise ValueError("Costs and gross benefits must be nonnegative")
    rate = float(a["discount_rate"])
    annual_net = gross - operating
    flows = [-upfront] + [annual_net] * horizon
    npv = sum(flow / ((1 + rate) ** t) for t, flow in enumerate(flows))
    payback = round(upfront / annual_net, 4) if annual_net > 0 else None
    return {
        "adoption_factor": adoption, "cost_factor": cost_factor,
        "annual_gross_benefit": gross, "annual_operating_cost": operating,
        "annual_net_cash_flow": annual_net,
        "cash_flows": flows,
        "npv": round(npv, 2),
        "simple_payback_years": payback,
        "pays_back_within_horizon": bool(payback is not None and payback <= horizon),
    }

def scenarios(a):
    return [calculate(a, adoption, cost) for adoption in a["adoption_factors"] for cost in a["cost_factors"]]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--assumptions", default="data/business_case_assumptions.json")
    args = parser.parse_args()
    a = json.loads(Path(args.assumptions).read_text(encoding="utf-8"))
    print(json.dumps({
        "case": a["case_name"], "disclaimer": a["disclaimer"],
        "base": calculate(a), "sensitivity": scenarios(a)
    }, indent=2))

if __name__ == "__main__":
    main()

