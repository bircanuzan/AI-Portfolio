"""Deterministic mathematical cross-checks for synthetic finance AI test cases."""
import json
import sys
from decimal import Decimal

def money(x):
    return Decimal(str(x))

def check(case):
    kind=case["type"]
    if kind=="profit_margin":
        revenue=money(case["revenue"])
        if revenue==0:raise ValueError("revenue cannot be zero")
        expected=money(case["net_income"])/revenue*100
        return {"id":case["id"],"check":"margin","expected_percent":float(expected),
                "claim_matches":abs(expected-money(case["claimed_margin_percent"]))<=Decimal("0.01")}
    if kind=="balance_sheet":
        difference=money(case["assets"])-money(case["liabilities"])-money(case["equity"])
        return {"id":case["id"],"check":"accounting_equation","difference":float(difference),
                "balanced":abs(difference)<=Decimal("0.01")}
    if kind=="reconciliation":
        remainder=money(case["invoice_amount"])-money(case["bank_receipt_amount"])
        return {"id":case["id"],"check":"receipt_reconciliation","outstanding":float(remainder),
                "expected_matches":abs(remainder-money(case["expected_outstanding"]))<=Decimal("0.01")}
    if kind=="entity_mismatch":
        return {"id":case["id"],"check":"entity_cross_reference",
                "ids_match":case["invoice_candidate_id"]==case["bank_receipt_candidate_id"]}
    raise ValueError("unsupported case type")

if __name__=="__main__":
    with open(sys.argv[1],encoding="utf-8") as f:data=json.load(f)
    print(json.dumps([check(case) for case in data],indent=2))
