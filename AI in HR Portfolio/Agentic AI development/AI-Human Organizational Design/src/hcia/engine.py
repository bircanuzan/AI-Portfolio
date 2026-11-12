"""Bounded six-tool agentic analyst with transparent arithmetic and provenance.

Only synthetic aggregate fixtures; no HRIS actions, candidate scoring, pay
decisions, employee profiles or external connections occur in this module.
"""
import json
from pathlib import Path

DATA_PATH=Path(__file__).resolve().parents[2]/"data"/"synthetic_hc_data.json"
TOOLS=("talent_acquisition","employer_brand","human_capital_operations",
       "talent_management","total_rewards","workforce_intelligence")
CAPABILITIES=TOOLS+("executive_brief","workforce_redesign")

def load_data(path=DATA_PATH):
    with open(path,encoding="utf-8") as handle:
        data=json.load(handle)
    validate(data)
    return data

def validate(data):
    if data["metadata"].get("fictional") is not True:
        raise ValueError("This lab accepts only synthetic fixtures")
    ids=[x["id"] for x in data["entities"]]
    if not ids or len(ids)!=len(set(ids)):
        raise ValueError("Invalid entity keys")
    for e in data["entities"]:
        if not (0<=e["filled"]<=e["approved"]) or min(e["budget"],e["people_cost"])<0:
            raise ValueError("Invalid workforce position or cost values")
    for section in ("recruitment","brand","operations","talent","rewards"):
        for row in data[section]:
            if row["entity"] not in ids or any(v<0 for v in row.values() if isinstance(v,(float,int))):
                raise ValueError("Invalid "+section+" values")
    for r in data["recruitment"]:
        if not (r["hires"]<=r["offers"]<=r["interviews"]<=r["qualified"]<=r["applicants"]):
            raise ValueError("Invalid funnel")
    for r in data["operations"]:
        if r["on_time"]>r["cases"] or r["exceptions"]>r["cases"]:
            raise ValueError("Invalid SLA data")

def rate(a,b):
    return round(100*a/b,2) if b else None
def ratio(a,b):
    return round(a/b,3) if b else None
def rows(data,section,entity):
    return [r for r in data[section] if entity=="ALL" or r.get("entity",r.get("id"))==entity]
def total(rs,key):
    return sum(r[key] for r in rs)
def result(tool,entity,metrics,source,notes,flags=()):
    return {"tool":tool,"entity":entity,"metrics":metrics,"evidence":{
        "source":"synthetic_hc_data.json","section":source,"synthetic":True},
        "limitations":notes,"risk_flags":list(flags),
        "human_review_required":True,"write_actions_executed":0}
def talent_acquisition(d,e):
    rs=rows(d,"recruitment",e)
    m={k:total(rs,k) for k in ("applicants","qualified","interviews","offers","hires","cost")}
    m.update(cost_per_hire_aed=ratio(m["cost"],m["hires"]),
             applicant_to_hire_pct=rate(m["hires"],m["applicants"]),
             offer_to_hire_pct=rate(m["hires"],m["offers"]),
             channel_mix=[{"entity":r["entity"],"channel":r["channel"],"hires":r["hires"],
                           "cost_per_hire_aed":ratio(r["cost"],r["hires"])} for r in rs])
    return result("talent_acquisition",e,m,"recruitment",["Group funnel aggregates; never screen or rank individual applicants."])
def employer_brand(d,e):
    rs=rows(d,"brand",e)
    m={k:total(rs,k) for k in ("impressions","clicks","applications","favourable","mentions","cost")}
    m.update(ctr_pct=rate(m["clicks"],m["impressions"]),
             click_to_application_pct=rate(m["applications"],m["clicks"]),
             favourable_share_pct=rate(m["favourable"],m["mentions"]),
             cost_per_application_aed=ratio(m["cost"],m["applications"]))
    return result("employer_brand",e,m,"brand",["Campaign attribution and sentiment samples are fictional."])
def human_capital_operations(d,e):
    rs=rows(d,"operations",e); n=total(rs,"cases"); on=total(rs,"on_time"); x=total(rs,"exceptions")
    m={"cases":n,"within_sla":on,"exceptions":x,"sla_pct":rate(on,n),"exception_pct":rate(x,n)}
    return result("human_capital_operations",e,m,"operations",
                  ["Escalation must be performed by authorised case owners."],
                  ["SLA_BREACH"] if m["sla_pct"] is not None and m["sla_pct"]<90 else [])
def talent_management(d,e):
    rs=rows(d,"talent",e); ents=rows(d,"entities",e)
    due=total(rs,"review_due"); done=total(rs,"review_done")
    crit=total(ents,"critical"); ready=total(ents,"successors_ready")
    m={"review_due":due,"reviews_completed":done,"review_completion_pct":rate(done,due),
       "skills_gaps_open":total(rs,"skills_gaps"),
       "critical_roles":crit,"successors_ready":ready,
       "succession_readiness_pct":rate(ready,crit),
       "learning_completion_pct":rate(total(rs,"learning_done"),total(rs,"learning_planned"))}
    return result("talent_management",e,m,"talent",["No employee-level performance or succession decisions."])
def total_rewards(d,e):
    rs=rows(d,"rewards",e); minimum=d["metadata"]["min_group"]
    allowed=[{"entity":r["entity"],"grade":r["grade"],"population":r["population"],
              "illustrative_market_ratio":ratio(r["internal_median"],r["illustrative_external_median"])}
             for r in rs if r["population"]>=minimum and r["illustrative_external_median"]>0]
    return result("total_rewards",e,{"cohorts":allowed,
                "suppressed_cohorts":len(rs)-len(allowed)},"rewards",
                  ["Market comparators are invented, not vendor salary surveys.",
                   "No employee salaries, grading decisions or pay equity inference."])
def workforce_intelligence(d,e):
    rs=rows(d,"entities",e)
    approved=total(rs,"approved"); filled=total(rs,"filled")
    budget=total(rs,"budget"); cost=total(rs,"people_cost")
    m={"approved_positions":approved,"filled_positions":filled,
       "vacancies":approved-filled,"contingent_workers":total(rs,"contractors"),
       "fill_pct":rate(filled,approved),"budget_aed":budget,
       "planned_cost_aed":cost,"headroom_aed":budget-cost}
    return result("workforce_intelligence",e,m,"entities",
                  ["Estimated synthetic budget, not real Finance or payroll figures."],
                  ["OVER_BUDGET"] if cost>budget else [])
FUNCTIONS=dict(zip(TOOLS,(talent_acquisition,employer_brand,human_capital_operations,
                          talent_management,total_rewards,workforce_intelligence)))
def execute(data,capability,entity):
    if capability not in CAPABILITIES:
        raise ValueError("Tool not allowlisted")
    if entity not in {x["id"] for x in data["entities"]}|{"ALL"}:
        raise ValueError("Unknown entity")
    if capability=="workforce_redesign":
        # A group-scoped scenario; do not misrepresent the pilot as a particular entity study.
        if entity!="ALL":
            raise ValueError("Workforce redesign pilot is only available as group-wide fictional case")
        from .workforce_design import assess_redesign
        return assess_redesign()
    if capability=="executive_brief":
        components=[FUNCTIONS[k](data,entity) for k in TOOLS]
        return {"tool":"executive_brief","entity":entity,"plan":list(TOOLS),
                "components":components,"risk_flags":sorted({f for c in components for f in c["risk_flags"]}),
                "evidence":{"source":"synthetic_hc_data.json","synthetic":True},
                "human_review_required":True,"write_actions_executed":0}
    return FUNCTIONS[capability](data,entity)
