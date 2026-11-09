"""Human–AI Workforce Redesign Decision Lab (synthetic).

Computes traceable *scenario capacity*, not actual time saved or planned layoffs.
Human decision rights and grade/ER approvals are never automated.
"""
from __future__ import annotations
import json
from pathlib import Path

DATA_PATH=Path(__file__).resolve().parents[2]/"data"/"synthetic_workforce_redesign.json"
RESERVED={"reserved_decision"}

def load_design(path=DATA_PATH):
    with Path(path).open(encoding="utf-8") as stream:
        case=json.load(stream)
    validate(case)
    return case

def validate(case):
    if case.get("meta",{}).get("fictional") is not True:
        raise ValueError("Only synthetic, explicitly labelled design cases are accepted")
    hours=case["meta"].get("productive_hours_per_fte")
    if not isinstance(hours,(int,float)) or hours<=0:
        raise ValueError("Productive hours must be positive")
    activity_ids=[a["id"] for a in case["activities"]]
    if not activity_ids or len(set(activity_ids))!=len(activity_ids):
        raise ValueError("Unique activity keys required")
    jobs={j["role"] for j in case["job_architecture"]}
    units={unit["unit"] for unit in case["future_structure"]}
    if len(jobs)!=len(case["job_architecture"]) or len(units)!=len(case["future_structure"]):
        raise ValueError("Duplicated job or organisational unit")
    for row in case["activities"]:
        if row["future_role"] not in jobs:
            raise ValueError("Activity has no accountable future human role")
        if not row.get("decision_right"):
            raise ValueError("Decision rights must be explicitly documented")
        if row["annual_units"]<0 or row["minutes_per_unit"]<0:
            raise ValueError("Workload cannot be negative")
        eligible=row["eligible_share"]
        if not 0<=eligible<=1:
            raise ValueError("Eligible work share must fall between 0 and 1")
        if row["risk"] in RESERVED and eligible!=0:
            raise ValueError("Reserved people decisions cannot be automatable")
        for key in ("adoption","rework_share"):
            val=row.get(key,0)
            if not 0<=val<=1: raise ValueError("Unreasonable "+key)
        if row.get("review_minutes_per_assisted_unit",0)<0:
            raise ValueError("Oversight effort cannot be negative")
    if abs(sum(x["weight"] for x in case["redistribution_weights"])-1)>1e-9:
        raise ValueError("Redistribution weights must sum to one")
    if any(not 0<=row["weight"]<=1 for row in case["redistribution_weights"]):
        raise ValueError("Redistribution weights must be nonnegative")
    for unit in case["future_structure"]:
        if unit["reports_to"] is not None and unit["reports_to"] not in units:
            raise ValueError("Orphan reporting line")
    for unit in case["future_structure"]:
        seen={unit["unit"]}; node=unit
        while node["reports_to"] is not None:
            parent=node["reports_to"]
            if parent in seen: raise ValueError("Circular reporting line")
            seen.add(parent)
            node=next(x for x in case["future_structure"] if x["unit"]==parent)

def model_capacity(case,adoption_multiplier=1.0):
    validate(case)
    if not 0<=adoption_multiplier<=1.25:
        raise ValueError("Adoption multiplier outside scenario limits")
    rows=[];sum_baseline=0;sum_net=0;sum_gross=0;sum_oversight=0
    for a in case["activities"]:
        baseline=a["annual_units"]*a["minutes_per_unit"]/60
        adoption=min(1.0,a.get("adoption",0)*adoption_multiplier)
        eligible=a["eligible_share"] if a["risk"] not in RESERVED else 0
        assisted_units=a["annual_units"]*eligible*adoption
        gross=baseline*eligible*adoption*(1-a.get("rework_share",0))
        oversight=assisted_units*a.get("review_minutes_per_assisted_unit",0)/60
        net=max(0.0,gross-oversight)
        sum_baseline+=baseline;sum_net+=net;sum_gross+=gross;sum_oversight+=oversight
        rows.append({
            "task_id":a["id"],"work":a["work"],"human_role_before":a["source_role"],
            "accountable_human_role_after":a["future_role"],"decision_right":a["decision_right"],
            "risk":a["risk"],"baseline_hours":round(baseline,2),
            "gross_candidate_hours":round(gross,2),"review_hours":round(oversight,2),
            "net_redeployable_hours_hypothesis":round(net,2),
            "retained_human_hours":round(baseline-net,2),
            "agent_may_approve_people_decisions":False
        })
    fte=case["meta"]["productive_hours_per_fte"]
    redistribution=[]
    for row in case["redistribution_weights"]:
        amount=sum_net*row["weight"]
        redistribution.append({"investment":row["investment"],"owner":row["owner"],
                               "hours_reinvested":round(amount,2),
                               "fte_equivalent":round(amount/fte,3)})
    return {
        "synthetic":True,"scenario_adoption_multiplier":adoption_multiplier,
        "baseline_hours":round(sum_baseline,2),"gross_candidate_hours":round(sum_gross,2),
        "oversight_hours":round(sum_oversight,2),
        "net_redeployable_hours_hypothesis":round(sum_net,2),
        "workload_fte_equivalent_before":round(sum_baseline/fte,3),
        "remaining_workload_fte_equivalent":round((sum_baseline-sum_net)/fte,3),
        "potential_capacity_to_redeploy_fte_equivalent":round(sum_net/fte,3),
        "authorized_headcount_changes":0,
        "cash_savings_evidenced_aed":0,
        "activities":rows,"capacity_reinvestment":redistribution
    }

def assess_redesign(case=None,adoption_multiplier=1.0):
    case=case if case is not None else load_design()
    cap=model_capacity(case,adoption_multiplier)
    jobs=[{"role":j["role"],"family":j["family"],"stream":j["stream"],
           "proposed_band":j["proposed_band"],"skills":j["skills"],
           "human_accountability":j["accountable_for"]} for j in case["job_architecture"]]
    return {
        "capability":"human_ai_workforce_redesign",
        "status":"SIMULATED_DECISION_SUPPORT_NOT_AN_APPROVED_ORG_REDESIGN",
        "case":case["meta"]["project"],
        "capacity":cap,
        "job_architecture":jobs,
        "current_structure":case["current_structure"],
        "future_structure":case["future_structure"],
        "implementation_gates":case["gates"],
        "decision":"PROPOSED_FOR_HUMAN_REVIEW",
        "evidence":{"source":"synthetic_workforce_redesign.json",
                    "model":"task-level activity/capacity ledger with explicit oversight and rework",
                    "synthetic":True},
        "limitations":[
            "Task volumes, adoption, review burden, grades and capacity assumptions are fictional",
            "FTE equivalents denote potential redeployment capacity, NOT actual reductions in headcount",
            "Job families and bands are unapproved illustrative designs, not licensed grading",
            "The future organisation is a proposal; real implementation needs CFO/CPO/ER/Legal approval"
        ],
        "write_actions_executed":0
    }

if __name__=="__main__":
    print(json.dumps(assess_redesign(),indent=2))
