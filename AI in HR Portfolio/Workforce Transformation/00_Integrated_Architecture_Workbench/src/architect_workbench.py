"""Eight-module synthetic workforce architecture decision workbench.

No LLM inference, external API, live HRIS access, production deployment, or
automated employee decision. Links existing data and model logic to an executive
decision pack and offline interactive dashboard. Python stdlib only.
"""
import argparse
import csv
import html
import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = Path(__file__).resolve().parents[1] / "output"

SOURCES = {
    "capacity": "01_Capacity_and_Headcount_Decision_Lab",
    "roles": "02_Role_Architecture_Skills_and_Redeployment",
    "transition": "03_Workforce_Transition_and_Performance_Model",
    "organization": "04_Organization_Architecture_and_AI_Native_Operating_Models",
    "orchestration": "05_Human_AI_Workforce_Orchestration_and_Digital_Worker_Management",
    "intelligence": "06_Strategic_Workforce_Intelligence_and_Future_Workforce_Scenarios",
    "product": "07_Workforce_Intelligence_Product_and_Solution_Architecture",
    "economics": "08_Workforce_Economics_and_Enterprise_Value_Realization",
}

def load_module(alias, folder, relative):
    name = "workbench_" + alias
    filename = ROOT / folder / relative
    if not filename.is_file():
        raise FileNotFoundError(filename)
    spec = importlib.util.spec_from_file_location(name, filename)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load " + str(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def read_csv(relative):
    with (ROOT / relative).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def read_json(relative):
    with (ROOT / relative).open(encoding="utf-8") as f:
        return json.load(f)

def build_evidence():
    a = SOURCES
    # This is a real code-level composition: import and call the maintained
    # project-specific models rather than transcribe their results or fork logic.
    capacity = load_module("capacity", a["capacity"], "src/workforce_capacity.py").load()
    roles = read_csv(a["roles"] + "/role_architecture.csv")
    transition = read_csv(a["transition"] + "/metrics.csv")
    org_module = load_module("organization", a["organization"], "src/compare_models.py")
    organizations = org_module.load_options()
    router = load_module("orchestration", a["orchestration"], "src/work_router.py")
    routing_rows, routing_matches = router.evaluate()
    request_inputs = read_json(a["orchestration"] + "/data/request_scenarios.json")
    for row, source in zip(routing_rows, request_inputs):
        row["task"] = source["task"]
        row["agent_status"] = source["agent_status"]
    intelligence = load_module("intelligence", a["intelligence"], "src/forecast_scenarios.py")
    workforce_forecasts = intelligence.run()
    skills_module = load_module("skills", a["intelligence"], "src/skills_gap.py")
    skill_gaps = skills_module.run()
    product = load_module("product", a["product"], "src/product_slice.py")
    product_cards = product.run()
    economics = load_module("economics", a["economics"], "src/value_model.py")
    values = economics.run()

    if len(roles) < 1 or len(transition) < 1:
        raise ValueError("Missing workforce architecture or transition evidence")
    if len(routing_rows) != len(request_inputs):
        raise ValueError("Routing inputs and evidence not aligned")
    if any(r["expected"] != r["actual"] for r in routing_rows):
        raise ValueError("Guardrail routing regression; executive report withheld")
    if any(v["verified_cash_savings_aed"] != 0 or v["actual_roi_verified"]
           for v in values):
        raise ValueError("Unverified monetary claims must be blocked")
    if any(not c["triage"]["human_approval_required"] or c["triage"]["action_executed"]
           for c in product_cards):
        raise ValueError("Product intake must remain human-approved and non-executing")
    if any(r["actual"] != "HUMAN_REVIEW" for r in routing_rows
           if r["task"] == "termination_decision"):
        raise ValueError("Employment decisions cannot be routed to agents")

    return {
        "metadata": {
            "title": "Human–AI Workforce Architecture | Integrated Evidence Workbench",
            "case": "Atlas UAE Shared Services — entirely fictional",
            "created_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "status": "SYNTHETIC_OFFLINE_EVIDENCE_ONLY",
            "source": "Eight maintained modules inside Workforce Transformation",
            "real_customer_data": False, "live_llm": False,
            "production_hris_connected": False, "verified_roi": False,
            "employment_decision_executed": False,
        },
        "executive_gate": "HOLD: client data, platform, security and finance validation needed",
        "01_capacity": capacity,
        "02_role_architecture": roles,
        "03_transition_metrics": transition,
        "04_org_options": organizations,
        "05_agent_routing": routing_rows,
        "05_routing_matches": {"matched": routing_matches, "total": len(routing_rows)},
        "06_forecasts": workforce_forecasts,
        "06_skill_gaps": skill_gaps,
        "07_product_backlog": product_cards,
        "08_economics": values,
        "metrics": {
            "role_families": len(roles),
            "transition_kpis": len(transition),
            "org_options_on_hold": sum(o["status"] != "DISCUSS" for o in organizations),
            "human_routed_cases": sum(r["actual"] == "HUMAN_REVIEW" for r in routing_rows),
            "held_product_use_cases": sum(c["triage"]["decision"] == "HOLD" for c in product_cards),
            "forecast_records": len(workforce_forecasts),
            "economic_model_net_hours": round(sum(v["modeled_net_hours_released_per_month"] for v in values), 2),
            "economic_model_net_opportunity_aed": round(sum(v["modeled_net_opportunity_aed_per_month"] for v in values), 2),
            "verified_cash_savings_aed": 0,
        },
        "evidence_links": {
            "research": "../00_LEADERSHIP_RESEARCH_TO_EVIDENCE_MAP.md",
            "governance": "../00_EXECUTIVE_CASE_AND_PILOT_PLAN.md",
            "sources": ["../" + folder + "/" for folder in a.values()],
        }
    }

def markdown_report(data):
    m = data["metrics"]
    lines = [
        "# Human–AI Workforce Architecture — executive evidence pack",
        "",
        "**Fictional Atlas UAE Shared Services; generated from code; NOT an enterprise outcome.**",
        "",
        "**Release status:** " + data["executive_gate"],
        "",
        "## Executive scorecard (invented inputs)",
        "",
        "| Control or planning signal | Generated result | Meaning |",
        "|---|---:|---|",
        "| Existing role families | " + str(m["role_families"]) + " | Module 02 role architecture |",
        "| Transition KPIs | " + str(m["transition_kpis"]) + " | Module 03 proposed definitions, not measured |",
        "| Organization options held | " + str(m["org_options_on_hold"]) + " | Module 04 accountability/risk gating |",
        "| Human-routed service requests | " + str(m["human_routed_cases"]) + " | Module 05 offline routing, no actual escalation |",
        "| Blocked use-case proposals | " + str(m["held_product_use_cases"]) + " | Module 07 synthetic intake risk gate |",
        "| Forecast scenario records | " + str(m["forecast_records"]) + " | Module 06 synthetic 2027–29 scenarios |",
        "| Modeled net task hours/month | " + str(m["economic_model_net_hours"]) + " | Module 08 distinct synthetic task data |",
        "| Modeled net opportunity (AED/month) | " + str(m["economic_model_net_opportunity_aed"]) + " | NOT cash savings or ROI |",
        "| Verified cash savings (AED) | 0 | None evidenced, not an audited result |",
        "",
        "## 01 — Current task capacity",
        "| Team | Baseline human hours | Assisted human hours | Current FTE | Modeled FTE gap |",
        "|---|---:|---:|---:|---:|"
    ]
    for c in data["01_capacity"]:
        lines.append("| {team} | {baseline_hours} | {assisted_human_hours} | {current_fte} | {modelled_fte_gap} |".format(**c))
    lines += ["", "## 02–03 — Future roles, capability and transition", ""]
    for r in data["02_role_architecture"]:
        lines.append("- **" + r["role"] + ":** retained human work: " +
                     r["human_retained_work"] + "; decision owner: " + r["human_decision_owner"])
    lines += ["", "**Transition metrics:** " + ", ".join(r["metric"] for r in data["03_transition_metrics"]), "",
              "## 04 — Organization option screen", "",
              "| Option | Status | Illustration score |", "|---|---|---:|"]
    for v in data["04_org_options"]:
        lines.append("| {} | {} | {} |".format(v["option"], v["status"],
                                               "—" if v["score"] is None else v["score"]))
    lines += ["", "## 05 — Agent routing negative and access tests", "",
              "| Request | Task | Agent status | Actual route | Expected route |",
              "|---|---|---|---|---|"]
    for v in data["05_agent_routing"]:
        lines.append("| {} | {} | {} | {} | {} |".format(
            v["id"], v["task"], v["agent_status"], v["actual"], v["expected"]))
    lines += ["", "## 06 — Workforce scenario projections (fictional)",
              "", "| Year | Function | Reference FTE | Assisted FTE | Demand-shock FTE | Available FTE |",
              "|---|---|---:|---:|---:|---:|"]
    for f in data["06_forecasts"]:
        b, a, s = f["reference"], f["guarded_assist"], f["demand_shock"]
        lines.append("| {} | {} | {} | {} | {} | {} |".format(
            a["year"], a["function"], b["scenario_fte"], a["scenario_fte"],
            s["scenario_fte"], a["available_fte"]))
    lines += ["", "## 07 — Product backlog intake and gated prioritization", "",
              "| Use case | Triage | Score (hypothetical) | Human approval |",
              "|---|---|---:|---|"]
    for c in data["07_product_backlog"]:
        t = c["triage"]
        lines.append("| {} | {} | {} | {} |".format(
            c["user_problem"], t["decision"], "—" if t["score"] is None else t["score"],
            "REQUIRED"))
    lines += ["", "## 08 — Task-level economics (separate invented dataset)", "",
              "| Task | Net task hours/month | Opportunity AED/month | Verified cash savings |",
              "|---|---:|---:|---:|"]
    for v in data["08_economics"]:
        lines.append("| {} | {} | {} | 0 / unverified |".format(
            v["task"], v["modeled_net_hours_released_per_month"],
            v["modeled_net_opportunity_aed_per_month"]))
    lines += ["", "## Executive decisions still required", "",
              "1. Validate real workflows, ownership, worker consultation and quality baseline.",
              "2. Establish secure source rights, HRIS and agent identity integration, DPIA/privacy and security signoff.",
              "3. Commission independent model/risk/acceptance evaluation before any live pilot.",
              "4. Confirm learning impact, skills supply and manager accountability.",
              "5. Obtain Finance-approved benefit definition and measure real before/after outcomes.",
              "6. Record a human go/no-go and rollback owner; the current decision is **HOLD**.",
              "",
              "**Evidence classification:** Code executed against synthetic data only. No live AI agent, "
              "production HRIS, employment action, real enterprise rollout or validated cash ROI.",
              ""]
    return "\n".join(lines)

def html_dashboard(data):
    # Self-contained: no libraries, remote assets, live calls or API keys.
    payload = json.dumps(data, ensure_ascii=True).replace("<", "\\u003c")
    page = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Human–AI Workforce Architecture | Synthetic Executive Dashboard</title>
<style>
:root{color-scheme:dark;font-family:Inter,system-ui,Segoe UI,sans-serif}
*{box-sizing:border-box}body{background:#0d1117;color:#e9eef5;margin:0;line-height:1.5}
header{padding:32px max(18px,calc((100vw - 1100px)/2));border-bottom:1px solid #32383e}
small,.muted{color:#aab4c4}.gold{color:#c6a052}h1{margin:0;font-size:clamp(24px,4vw,36px)}h2{font-size:19px;margin:0 0 14px}
main{max-width:1140px;margin:auto;padding:22px 18px 80px}
.alert{border:1px solid #a88a48;padding:14px 18px;border-radius:9px;background:#201b14}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:13px;margin:18px 0}
.kpi,.panel{padding:20px;border:1px solid #303844;background:#151b23;border-radius:11px}
.kpi strong{font-size:27px;display:block;color:#e6bf73}.kpi span{font-size:13px;color:#aab4c4}
.panel{margin:16px 0}.panel p{color:#b8c0cc}
label{font-size:14px;margin-right:10px}select{color:#e9eef5;background:#252d38;border:1px solid #566171;border-radius:6px;padding:9px}
table{border-collapse:collapse;width:100%;font-size:13px}th,td{padding:9px 7px;border-bottom:1px solid #2e3540;text-align:left}th{color:#e3bb70}
.scroller{overflow-x:auto}.bar{background:#263648;height:13px;border-radius:3px;min-width:90px}
.bar>i{display:block;background:#c6a052;height:100%;border-radius:3px}
code{color:#d4e5ff}.tag{color:#e5bf77;font-weight:650}
footer{margin-top:30px;color:#aab4c4;font-size:12px}@media print{body{background:#fff;color:#111} .panel,.kpi,.alert{color:#111;background:#fff} .bar{background:#ddd} select{display:none}}
</style></head>
<body><header><small>HUMANEVOX | INDEPENDENT PORTFOLIO DEMONSTRATION</small><h1>Human–AI Workforce <span class="gold">Architecture</span></h1>
<p class="muted">One fictional enterprise · eight connected decisions · no live deployments</p></header>
<main><p class="alert"><b class="gold">DECISION: HOLD.</b> Synthetic evidence only. Requires client baselines, privacy/security approvals, actual integration testing and CFO validation before any deployment. No automated employee decisions.</p>
<section class="grid" id="kpis"></section>
<section class="panel"><h2>Workforce scenarios: 2027–2029</h2>
<p>Independent arithmetic on invented workload projections. Not real UAE labor market forecasts or verified AI savings.</p>
<label for="year">Planning year</label><select id="year" aria-label="Planning year"><option>2027</option><option>2028</option><option>2029</option></select>
<label for="scenario">Scenario</label><select id="scenario" aria-label="Scenario"><option value="reference">Reference / no assistance</option><option value="guarded_assist">Guarded AI assistance</option><option value="demand_shock">Demand +20% stress test</option></select>
<div class="scroller"><table><thead><tr><th>Function</th><th>Modeled FTE</th><th>Supply FTE</th><th>Relative demand</th></tr></thead><tbody id="forecast"></tbody></table></div></section>
<section class="panel"><h2>Organization design alternatives</h2><div class="scroller"><table><thead><tr><th>Option</th><th>Decision gate</th><th>Illustrative score</th></tr></thead><tbody id="org"></tbody></table></div><p>Scores are not deployment recommendations. Accountability gaps and unmitigated risks block an option.</p></section>
<section class="panel"><h2>Digital workforce control routing</h2><div class="scroller"><table><thead><tr><th>Request</th><th>Task</th><th>Agent state</th><th>Route</th></tr></thead><tbody id="routing"></tbody></table></div><p>Every route is a locally simulated policy choice, not a live AI call or a completed human case.</p></section>
<section class="panel"><h2>Product roadmap intake</h2><div class="scroller"><table><thead><tr><th>Use case</th><th>Control outcome</th><th>Illustrative score</th></tr></thead><tbody id="product"></tbody></table></div></section>
<section class="panel"><h2>Task economics — synthetic only</h2><div class="scroller"><table><thead><tr><th>Work item</th><th>Modeled net hours / month</th><th>Net opportunity AED / month</th></tr></thead><tbody id="economics"></tbody></table></div><p><b>No actual cash savings or ROI have been verified.</b> Time released and monetary value must be approved separately by Finance.</p></section>
<footer>Built from the maintained Modules 01–08 in Workforce Transformation, using deterministic Python and synthetic fixtures. No external network, analytics or live employee data.</footer></main>
<script>const D = __PAYLOAD__;
const cell=(tr,v)=>{const td=document.createElement("td");td.textContent=String(v);tr.append(td);};
const add=(id,arr)=>{const root=document.getElementById(id);root.replaceChildren();arr.forEach(values=>{const tr=document.createElement("tr");values.forEach(v=>cell(tr,v));root.append(tr);});};
const kpis=[["Role families",D.metrics.role_families],["Agent requests routed to humans",D.metrics.human_routed_cases],["Product ideas on HOLD",D.metrics.held_product_use_cases],["Organization models held",D.metrics.org_options_on_hold],["Verified cash savings","None evidenced"]];
kpis.forEach(pair=>{const el=document.createElement("article");el.className="kpi";const n=document.createElement("strong");n.textContent=pair[1];const l=document.createElement("span");l.textContent=pair[0];el.append(n,l);document.getElementById("kpis").append(el);});
const rows=D["06_forecasts"];function drawForecast(){const y=document.getElementById("year").value,s=document.getElementById("scenario").value;const available=rows.filter(x=>x[s].year===y);const max=Math.max(...available.map(x=>x[s].scenario_fte),1);const tbody=document.getElementById("forecast");tbody.replaceChildren();available.forEach(x=>{const record=x[s],tr=document.createElement("tr");cell(tr,record.function);cell(tr,record.scenario_fte);cell(tr,record.available_fte);const td=document.createElement("td"),outer=document.createElement("div"),bar=document.createElement("i");outer.className="bar";bar.style.width=Math.round(100*record.scenario_fte/max)+"%";outer.append(bar);td.append(outer);tr.append(td);tbody.append(tr);});}
document.getElementById("year").addEventListener("change",drawForecast);document.getElementById("scenario").addEventListener("change",drawForecast);drawForecast();
add("org",D["04_org_options"].map(x=>[x.option,x.status,x.score===null?"—":x.score]));
add("routing",D["05_agent_routing"].map(x=>[x.id,x.task,x.agent_status,x.actual]));
add("product",D["07_product_backlog"].map(x=>[x.user_problem,x.triage.decision,x.triage.score===null?"—":x.triage.score]));
add("economics",D["08_economics"].map(x=>[x.task,x.modeled_net_hours_released_per_month,x.modeled_net_opportunity_aed_per_month]));
</script></body></html>'''
    return page.replace("__PAYLOAD__", payload)

def write_outputs(data, target):
    target = Path(target)
    target.mkdir(parents=True, exist_ok=True)
    paths = {
        "json": target / "architecture_evidence.json",
        "markdown": target / "executive_decision_pack.md",
        "html": target / "executive_dashboard.html",
    }
    paths["json"].write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    paths["markdown"].write_text(markdown_report(data), encoding="utf-8")
    paths["html"].write_text(html_dashboard(data), encoding="utf-8")
    return paths

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=OUTPUT, help="Directory for generated evidence files")
    args = parser.parse_args()
    evidence = build_evidence()
    for label, path in write_outputs(evidence, args.out).items():
        print(label + ": " + str(path))
    print("Release decision: HOLD; fictional inputs, no live agents, HRIS, ROI or HR action.")

if __name__ == "__main__":
    main()
