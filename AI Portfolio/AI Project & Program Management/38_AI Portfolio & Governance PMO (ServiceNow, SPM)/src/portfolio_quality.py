"""Synthetic AI portfolio controls and executive PMO report.

Uses no ServiceNow API, no AI models and no external Python dependencies.
Run: python src/portfolio_quality.py
"""
from __future__ import annotations

import csv
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AS_OF = date(2026, 10, 29)  # Fixed to reproduce October 2026 scenario.


def load(name: str) -> list[dict[str, str]]:
    with (ROOT / "data" / name).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def evaluate() -> dict:
    demands = load("demands.csv")
    projects = load("projects.csv")
    products = load("products.csv")
    finance = load("funding_cost.csv")
    approvals = load("approval_evidence.csv")
    raid = load("raid.csv")
    benefits = load("benefits.csv")

    issues = []
    ids = [d["demand_id"] for d in demands]
    if len(ids) != len(set(ids)):
        issues.append("Duplicate demand IDs")

    required = ("demand_id", "title", "category", "domain", "owner", "sponsor",
                "stage", "disposition", "business_case_ref", "last_updated")
    missing = []
    for d in demands:
        for key in required:
            if not d.get(key, "").strip():
                missing.append(f"{d['demand_id']} missing {key}")
    issues.extend(missing)

    disposition_counts = {
        state: sum(d["disposition"] == state for d in demands)
        for state in ("Approved", "Deferred", "Rejected", "Pending")
    }
    # Prioritisation scores are proposed design values, not real SPM ranking.
    weights = {"strategy_fit": .30, "value": .25, "feasibility": .20,
               "responsible_ai_readiness": .15, "capacity": .10}
    ranked = []
    for d in demands:
        score = round(sum(float(d[k]) * v for k, v in weights.items()), 2)
        ranked.append((d["demand_id"], score))
    ranked.sort(key=lambda x: x[1], reverse=True)

    approved_demand_ids = {d["demand_id"] for d in demands if d["disposition"] == "Approved"}
    g3_approved = {a["record_key"] for a in approvals
                   if a["gate"] == "G3 Funding Approval" and a["status"] == "Approved"}
    # This sample explicitly flags approved demand conversions lacking gate evidence.
    ungated_conversions = [
        d["demand_id"] for d in demands
        if d["disposition"] == "Approved"
        and d["conversion_type"] == "Project"
        and d["demand_id"] not in g3_approved
    ]

    # Financials: budget allocations and cost forecasts are distinct.
    shortfalls = {}
    approved_total = 0
    forecast_total = 0
    finance_unapproved = []
    for f in finance:
        budget = float(f["approved_funding"])
        forecast = float(f["forecast_cost"])
        approved_total += budget
        forecast_total += forecast
        if forecast > budget:
            shortfalls[f["project_id"]] = round(forecast - budget, 2)
        if f["finance_approved"] != "Yes":
            finance_unapproved.append(f["project_id"])
    overdue = [p["project_id"] for p in projects
               if p["state"] != "Closed"
               and date.fromisoformat(p["milestone_due"]) < AS_OF]
    stale = [p["project_id"] for p in projects
             if (AS_OF - date.fromisoformat(p["last_update"])).days > 7]
    high_raid = [r["raid_id"] for r in raid
                 if r["severity"] == "High" and r["status"] == "Open"]
    security_pending = [
        p["project_id"] for p in projects if p["security_review"] != "Approved"
    ] + [
        p["product_id"] for p in products if p["security_review"] != "Approved"
    ]
    conversions = {d["conversion_id"] for d in demands if d["conversion_id"]}
    orphan = [
        p["project_id"] for p in projects if p["project_id"] not in conversions
    ] + [
        p["product_id"] for p in products if p["product_id"] not in conversions
    ]
    # A possible release gate; in real life the VP and governance forum decide.
    gate = "HOLD_FOR_REVIEW" if (ungated_conversions or finance_unapproved
                               or high_raid or security_pending) else "REVIEW_FOR_APPROVAL"
    return {
        "as_of": AS_OF.isoformat(),
        "demand_count": len(demands),
        "project_count": len(projects),
        "product_count": len(products),
        "disposition": disposition_counts,
        "ranked": ranked,
        "data_quality_issues": issues,
        "ungated_conversions": ungated_conversions,
        "funding_total": approved_total,
        "forecast_total": forecast_total,
        "funding_shortfalls": shortfalls,
        "finance_unapproved": finance_unapproved,
        "overdue_milestones": overdue,
        "stale_updates": stale,
        "open_high_raid": high_raid,
        "security_pending": security_pending,
        "orphan_conversions": orphan,
        "benefit_hypotheses": len(benefits),
        "verified_realised_benefits": sum(bool(b["measured_actual"]) for b in benefits),
        "release_gate": gate,
    }


def report(m: dict) -> str:
    fmt = lambda s: ", ".join(s) if s else "None"
    d = m["disposition"]
    return "\n".join([
        "# AI Portfolio CoE — VP Governance Board Pack (SIMULATED)",
        "",
        f"**As of: {m['as_of']} | Gate recommendation: {m['release_gate']}**",
        "",
        "> All records are fictional. This is an SPM-aligned CSV demonstration, not a report from a ServiceNow tenant.",
        "",
        "## Portfolio pipeline",
        "| Demand records | Approved | Deferred | Rejected | Pending | Projects | Product transitions |",
        "|---:|---:|---:|---:|---:|---:|---:|",
        f"| {m['demand_count']} | {d['Approved']} | {d['Deferred']} | {d['Rejected']} | {d['Pending']} | {m['project_count']} | {m['product_count']} |",
        "",
        "## Cost and funding controls (synthetic AED)",
        f"- Recorded funding allocations: **AED {m['funding_total']:,.0f}**. These fields require finance validation.",
        f"- Estimated cost forecasts: **AED {m['forecast_total']:,.0f}**.",
        f"- Project-level forecast gaps (not actual overspend): **{m['funding_shortfalls']}**.",
        f"- Missing finance approval: **{fmt(m['finance_unapproved'])}**.",
        "",
        "## Governance exceptions",
        f"- Converted projects missing G3 approved evidence: **{fmt(m['ungated_conversions'])}**.",
        f"- Overdue project milestones: **{fmt(m['overdue_milestones'])}**.",
        f"- Project status not updated within 7 days: **{fmt(m['stale_updates'])}**.",
        f"- Open high-severity RAID items: **{fmt(m['open_high_raid'])}**.",
        f"- Security review incomplete: **{fmt(m['security_pending'])}**.",
        f"- Orphan conversion references: **{fmt(m['orphan_conversions'])}**.",
        f"- Required-field issues: **{fmt(m['data_quality_issues'])}**.",
        "",
        "## Prioritisation (weighted design score out of 5)",
        "| Demand | Score |",
        "|---|---:|",
        *[f"| {demand} | {score:.2f} |" for demand, score in m["ranked"]],
        "",
        "## Benefits and closure",
        f"- Benefit hypotheses tracked: **{m['benefit_hypotheses']}**.",
        f"- Verified realised benefits: **{m['verified_realised_benefits']}**. No production benefits have been claimed.",
        "",
        "## Suggested VP forum decisions (not actual approvals)",
        "1. Seek funding clarification for PRJ-002 and require formal G3 approval for originating DMD-004.",
        "2. Resolve high-severity RAID before release and rebaseline overdue milestones.",
        "3. Require security and UAT sign-offs before accepting pilot-to-product transition.",
        "4. Preserve rejected/deferred demand records and agree benefits measurement owners.",
        "",
        "## Method and limitations",
        "Portfolio checks are deterministic, based on synthetic CSVs and a fixed date. No ServiceNow SPM platform, model, live AI service, real business expenditure or independent audit was tested.",
        "",
    ])


if __name__ == "__main__":
    metrics = evaluate()
    destination = ROOT / "reports" / "PORTFOLIO_HEALTH_REPORT.md"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(report(metrics), encoding="utf-8")
    print(f"Generated {destination} | {metrics['release_gate']}")
