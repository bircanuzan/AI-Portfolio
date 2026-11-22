#!/usr/bin/env python3
"""Synthetic telecom commercial analytics — standard-library only."""
import csv
import json
from collections import defaultdict
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path

HERE = Path(__file__).resolve().parent

def analyse(path):
    with open(path, newline="", encoding="utf-8") as f:
        source = list(csv.DictReader(f))
    valid, issues, seen = [], [], set()
    for line, row in enumerate(source, 2):
        reasons = []
        ident = row.get("order_id", "").strip()
        if not ident: reasons.append("missing_id")
        elif ident in seen: reasons.append("duplicate_id")
        if not row.get("country", "").strip(): reasons.append("missing_country")
        try: date.fromisoformat(row.get("order_date", ""))
        except ValueError: reasons.append("invalid_date")
        try:
            for field in ("revenue_usd", "cost_usd", "data_gb"):
                row[field] = Decimal(row[field])
                if row[field] < 0: reasons.append("negative_" + field)
            row["units"] = int(row["units"])
            if row["units"] < 1: reasons.append("invalid_units")
        except (KeyError, InvalidOperation, ValueError):
            reasons.append("invalid_numeric")
        row["returning_customer"] = row.get("returning_customer", "").lower()
        if row["returning_customer"] not in ("true", "false"):
            reasons.append("invalid_returning_flag")
        if reasons: issues.append({"line": line, "order_id": ident, "reasons": ";".join(reasons)})
        else:
            seen.add(ident)
            valid.append(row)
    revenue = sum((r["revenue_usd"] for r in valid), Decimal(0))
    cost = sum((r["cost_usd"] for r in valid), Decimal(0))
    n = len(valid)
    pct = lambda a,b: round(100*a/b, 2) if b else None
    kpis = {
        "input_rows": len(source), "accepted_orders": n, "quarantined_rows": len(issues),
        "revenue_usd": str(revenue), "cost_usd": str(cost),
        "gross_profit_usd": str(revenue-cost),
        "gross_margin_pct": pct(revenue-cost, revenue),
        "avg_order_value_usd": str((revenue/n).quantize(Decimal(".01"))) if n else None,
        "units_sold": sum(r["units"] for r in valid),
        "data_gb": str(sum((r["data_gb"] for r in valid), Decimal(0))),
        "returning_order_share_pct": pct(sum(r["returning_customer"]=="true" for r in valid), n),
        "quarantine_rate_pct": pct(len(issues), len(source)),
    }
    segments = {}
    for field in ("country","channel","product"):
        group = defaultdict(lambda: {"orders":0, "revenue":Decimal(0), "cost":Decimal(0)})
        for row in valid:
            t=group[row[field]]; t["orders"]+=1; t["revenue"]+=row["revenue_usd"]; t["cost"]+=row["cost_usd"]
        segments[field]=[{"segment":key,"orders":v["orders"],"revenue_usd":str(v["revenue"]),"cost_usd":str(v["cost"])} for key,v in sorted(group.items())]
    group = defaultdict(lambda: {"orders":0,"revenue":Decimal(0),"cost":Decimal(0)})
    for row in valid:
        month=row["order_date"][:7]; t=group[month]; t["orders"]+=1; t["revenue"]+=row["revenue_usd"]; t["cost"]+=row["cost_usd"]
    segments["month"]=[{"segment":key,"orders":v["orders"],"revenue_usd":str(v["revenue"]),"cost_usd":str(v["cost"])} for key,v in sorted(group.items())]
    return {"kpis":kpis, "segments":segments, "issues":issues}

def write_outputs(report, dest):
    dest.mkdir(parents=True, exist_ok=True)
    (dest/"metrics.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    for name, rows in report["segments"].items():
        with (dest/("by_"+name+".csv")).open("w", newline="",encoding="utf-8") as f:
            wr=csv.DictWriter(f,fieldnames=["segment","orders","revenue_usd","cost_usd"])
            wr.writeheader(); wr.writerows(rows)
    with (dest/"quarantined_rows.csv").open("w",newline="",encoding="utf-8") as f:
        wr=csv.DictWriter(f,fieldnames=["line","order_id","reasons"])
        wr.writeheader();wr.writerows(report["issues"])
    k=report["kpis"]
    (dest/"stakeholder_summary.txt").write_text(
        "SYNTHETIC DEMONSTRATION — NOT CLIENT RESULTS\n"
        f"Accepted: {k['accepted_orders']} | Quarantined: {k['quarantined_rows']}\n"
        f"Revenue: USD {k['revenue_usd']} | Gross profit: USD {k['gross_profit_usd']}\n"
        f"Gross margin: {k['gross_margin_pct']}% | Human sign-off required before distribution.\n",encoding="utf-8")

if __name__ == "__main__":
    result=analyse(HERE/"data"/"synthetic_esim_orders.csv")
    write_outputs(result,HERE/"output")
    print(json.dumps(result["kpis"],indent=2))
