"""Adoption KPI illustration using fictional accounts. Not actual provider analytics."""
import csv
from pathlib import Path

FIELDS = ("onboarded", "activated", "conversations", "successful", "failed", "unknown", "handed_off")

def load_accounts(path):
    with open(path, "r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError("No account records")
    output = []
    for row in rows:
        item = {k: row[k] for k in ("account", "market", "segment")}
        for key in FIELDS:
            item[key] = int(row[key])
            if item[key] < 0:
                raise ValueError(f"Negative value in {key}")
        item["total_cost_aed"] = float(row["total_cost_aed"])
        if item["total_cost_aed"] < 0:
            raise ValueError("Negative cost")
        if item["successful"] + item["failed"] + item["unknown"] != item["conversations"]:
            raise ValueError(f"Outcome totals do not match conversations: {item['account']}")
        if item["activated"] > item["onboarded"]:
            raise ValueError("Activated accounts exceed onboarded")
        if item["handed_off"] > item["conversations"]:
            raise ValueError("Handoffs exceed conversations")
        output.append(item)
    return output

def divide(numerator, denominator):
    return numerator / denominator if denominator else 0.0

def summarize(accounts):
    if not accounts:
        raise ValueError("No accounts")
    totals = {key: sum(a[key] for a in accounts) for key in FIELDS}
    cost = sum(a["total_cost_aed"] for a in accounts)
    conversations = totals["conversations"]
    return {
        "accounts_onboarded": totals["onboarded"],
        "accounts_activated": totals["activated"],
        "activation_rate": divide(totals["activated"], totals["onboarded"]),
        "conversations": conversations,
        "success_rate": divide(totals["successful"], conversations),
        "failure_rate": divide(totals["failed"], conversations),
        "unknown_rate": divide(totals["unknown"], conversations),
        "handoff_rate": divide(totals["handed_off"], conversations),
        "avg_cost_per_conversation_aed": divide(cost, conversations),
        "total_cost_aed": cost,
        "at_risk_accounts": [a["account"] for a in accounts if
            a["onboarded"] and (not a["activated"] or
            (a["conversations"] >= 20 and divide(a["successful"], a["conversations"]) < .60))],
    }

if __name__ == "__main__":
    rows = load_accounts(Path(__file__).resolve().parents[1] / "synthetic_data/accounts.csv")
    report = summarize(rows)
    for key, value in report.items():
        print(key, ":", round(value, 4) if isinstance(value, float) else value)
