"""Synthetic model-usage and budget ledger. Prices are hypothetical, not quotes."""
import argparse
import csv
import json
from collections import defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path

COLS = ["department", "model_tier", "requests", "successful_requests",
        "avg_input_tokens", "avg_output_tokens",
        "input_usd_per_million", "output_usd_per_million"]
MILLION = Decimal(1000000)


def estimate(records, budgets):
    costs = defaultdict(lambda: {"spend": Decimal("0"), "requests": 0, "successful": 0})
    details = []
    for row in records:
        try:
            department = row["department"].strip()
            tier = row["model_tier"].strip()
            requests = int(row["requests"])
            successful = int(row["successful_requests"])
            tokens_in = int(row["avg_input_tokens"])
            tokens_out = int(row["avg_output_tokens"])
            rate_in = Decimal(row["input_usd_per_million"])
            rate_out = Decimal(row["output_usd_per_million"])
        except (ValueError, KeyError, TypeError, InvalidOperation) as error:
            raise ValueError("Invalid usage record") from error
        if not department or not tier:
            raise ValueError("Missing department or model tier")
        if min(requests, successful, tokens_in, tokens_out) < 0 or successful > requests:
            raise ValueError("Inconsistent request or token counts")
        if not rate_in.is_finite() or not rate_out.is_finite() or min(rate_in, rate_out) < 0:
            raise ValueError("Invalid example price")
        spend = (Decimal(requests) *
                 (Decimal(tokens_in) * rate_in + Decimal(tokens_out) * rate_out) / MILLION)
        costs[department]["spend"] += spend
        costs[department]["requests"] += requests
        costs[department]["successful"] += successful
        details.append({"department": department, "model_tier": tier,
                        "estimated_spend_usd": str(spend.quantize(Decimal("0.000001")))})
    departments = []
    for department, values in sorted(costs.items()):
        budget = Decimal(str(budgets.get(department, "0")))
        if not budget.is_finite() or budget < 0:
            raise ValueError("Invalid departmental budget")
        spend = values["spend"]
        per_success = (spend / values["successful"]) if values["successful"] else None
        departments.append({
            "department": department, "requests": values["requests"],
            "successful_requests": values["successful"],
            "modelled_spend_usd": str(spend.quantize(Decimal("0.000001"))),
            "example_budget_usd": str(budget),
            "over_example_budget": spend > budget,
            "spend_per_success_usd": str(per_success.quantize(Decimal("0.000001")))
                if per_success is not None else None
        })
    return {"evidence_type": "synthetic_illustrative_not_actual",
            "currency": "USD", "department_summary": departments, "model_details": details}


def run(input_csv, budget_json, output_json):
    with Path(input_csv).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != COLS:
            raise ValueError("Usage CSV column contract mismatch")
        records = list(reader)
    budgets = json.loads(Path(budget_json).read_text(encoding="utf-8"))
    if not isinstance(budgets, dict):
        raise ValueError("Budget JSON must be an object")
    report = estimate(records, budgets)
    Path(output_json).write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--budgets", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.input, args.budgets, args.output), indent=2))
