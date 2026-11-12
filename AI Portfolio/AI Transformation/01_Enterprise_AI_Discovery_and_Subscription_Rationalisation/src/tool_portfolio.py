"""Synthetic enterprise tool-spend diagnostic. Human owners decide all contracts."""
import csv
import json
from pathlib import Path

INVENTORY = Path(__file__).resolve().parents[1] / "data" / "synthetic_tool_inventory.csv"

def evaluate(row):
    paid = int(row["paid_seats"])
    active = int(row["active_seats"])
    price = float(row["monthly_cost_per_seat_usd"])
    if paid < 0 or active < 0 or active > paid or price < 0:
        raise ValueError("Invalid seats or price")
    risk = []
    if row["sensitive_data_approved"].lower() != "true":
        risk.append("REVIEW_DATA_APPROVAL")
    if row["security_owner_present"].lower() != "true":
        risk.append("ASSIGN_SECURITY_OWNER")
    utilization = round(active / paid, 3) if paid else 0
    if utilization < 0.5:
        risk.append("REVIEW_UNDERUSED_SEATS")
    if int(row["months_until_renewal"]) <= 3:
        risk.append("REVIEW_CONTRACT_TIMING")
    return {
        "tool_id": row["tool_id"],
        "product_family": row["product_family"],
        "annual_paid_license_run_rate_usd": round(paid * price * 12, 2),
        "annual_unassigned_seat_exposure_usd": round((paid - active) * price * 12, 2),
        "active_share": utilization,
        "decision": "HUMAN_PROCUREMENT_SECURITY_REVIEW",
        "review_flags": risk,
        "verified_savings_usd": 0,
    }

def audit(path=INVENTORY):
    with open(path, encoding="utf-8", newline="") as handle:
        rows = [evaluate(row) for row in csv.DictReader(handle)]
    return {
        "basis": "SYNTHETIC LICENSE DATA; exposure is NOT realizable savings",
        "annual_paid_license_run_rate_usd": round(sum(x["annual_paid_license_run_rate_usd"] for x in rows), 2),
        "potential_seat_exposure_usd": round(sum(x["annual_unassigned_seat_exposure_usd"] for x in rows), 2),
        "tools": rows,
    }

if __name__ == "__main__":
    print(json.dumps(audit(), indent=2))
