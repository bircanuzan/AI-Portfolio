"""AI-Human Organizational Design | governed synthetic design workbench.

This integrates existing tested synthetic workforce calculators with task, role,
organization, skills and candidate digital-agent design. No client data, live
model session, employment action, enterprise integration or production use.
"""
from __future__ import annotations
import json
from .workforce_design import load_design, validate as validate_design, model_capacity
from .engine import load_data, workforce_intelligence

PRODUCT = "AI-Human Organizational Design"
FEATURE_STATUS = {
    "Orgvue-style org analysis, job families and scenario design": "SYNTHETIC_EXECUTABLE",
    "Nakisa-style workforce plan, approvals and HCM sync": "SCENARIOS_ONLY_NO_HCM_SYNC",
    "Reejig-style map, analyze, build, run, measure, log, update": "MAP_AND_SCENARIO_ONLY",
    "TechWolf-style task, role and skills intelligence": "SYNTHETIC_ROLE_SKILLS_ONLY",
    "Visier-style governed people analytics": "SYNTHETIC_AGGREGATES_ONLY",
    "Agent role, lifecycle, supervision and evaluation": "DRAFT_DESIGN_ONLY",
    "G42 sovereign LLM and enterprise platform integration": "NOT_CONNECTED",
}
CONNECTORS = {
    "Oracle Fusion HCM": "NOT_CONNECTED",
    "Workday": "NOT_CONNECTED",
    "SAP SuccessFactors": "NOT_CONNECTED",
    "ATS and LMS": "NOT_CONNECTED",
    "Core42 Compass": "NOT_CONNECTED",
    "Azure AI Foundry": "NOT_CONNECTED",
    "Inception42 Catalyst": "ACCESS_NOT_VERIFIED",
}
APPROVALS = ["Business owner", "CHRO/CPO", "Finance", "HR Legal/ER", "CISO/Responsible AI"]

def _nonnegative(name, value):
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (float, int)):
        raise ValueError(name + ": expected nonnegative numeric scenario assumption")
    if not 0 <= value <= 1000000000:
        raise ValueError(name + ": assumption outside bounds")
    return float(value)

def _org_tree(case):
    units = case["future_structure"]
    names = {r["unit"]: r for r in units}
    if sum(u["reports_to"] is None for u in units) != 1:
        raise ValueError("Org architecture requires one root")
    result = []
    for unit in units:
        visited = {unit["unit"]}
        parent = unit["reports_to"]
        depth = 0
        while parent is not None:
            if parent not in names or parent in visited:
                raise ValueError("Invalid or circular reporting line")
            visited.add(parent)
            depth += 1
            parent = names[parent]["reports_to"]
        if not unit.get("human_accountability"):
            raise ValueError("All units need a human owner")
        result.append({
            "unit": unit["unit"],
            "reports_to": unit["reports_to"],
            "depth": depth,
            "span_of_control": sum(u["reports_to"] == unit["unit"] for u in units),
            "accountable_human": unit["human_accountability"],
            "status": "DRAFT_NOT_APPROVED",
        })
    return result

def blueprint(adoption_multiplier=1.0, value_per_hour_aed=None,
              yearly_agent_cost_aed=None, startup_cost_aed=None, case=None):
    """Draft an explainable organization design; NEVER authorize employment changes."""
    case = load_design() if case is None else case
    validate_design(case)
    if isinstance(adoption_multiplier, bool) or not isinstance(adoption_multiplier, (int, float)):
        raise ValueError("Adoption multiplier must be numeric")
    value = _nonnegative("value_per_hour_aed", value_per_hour_aed)
    yearly = _nonnegative("yearly_agent_cost_aed", yearly_agent_cost_aed)
    startup = _nonnegative("startup_cost_aed", startup_cost_aed)
    capacity = model_capacity(case, adoption_multiplier)
    computed = {row["task_id"]: row for row in capacity["activities"]}
    tasks = []
    for item in case["activities"]:
        reserved = item["risk"] == "reserved_decision"
        derived = computed[item["id"]]
        candidate = item["eligible_share"] > 0 and not reserved
        tasks.append({
            "id": item["id"], "work": item["work"],
            "allocation": ("HUMAN_ONLY" if reserved else
                           "AGENT_CANDIDATE_WITH_HUMAN_REVIEW" if candidate else "HUMAN_LED"),
            "accountable_human": item["future_role"],
            "decision_rights": item["decision_right"],
            "risk": item["risk"],
            "baseline_hours": derived["baseline_hours"],
            "gross_candidate_hours": derived["gross_candidate_hours"],
            "review_hours": derived["review_hours"],
            "net_candidate_hours": derived["net_redeployable_hours_hypothesis"],
            "fallback": "Manual human-owned workflow",
            "agent_can_approve_people_decisions": False,
        })
    roles = [{
        "role": job["role"],
        "family": job["family"],
        "skills": list(job["skills"]),
        "illustrative_band": job["proposed_band"],
        "accountability": job["accountable_for"],
        "tasks": [t["id"] for t in tasks if t["accountable_human"] == job["role"]],
        "individual_skill_assessment": "NOT_PERFORMED",
        "employee_action": "NOT_AUTHORIZED",
    } for job in case["job_architecture"]]
    agent_register = [{
        "agent_id": "DESIGN-" + t["id"],
        "mission": "Assist with " + t["work"],
        "human_manager": t["accountable_human"],
        "lifecycle": "DRAFT_NOT_DEPLOYED",
        "access_scope": "NO_REAL_DATA",
        "decision_authority": "RECOMMEND_ONLY",
        "review_cadence": "MONTHLY_IF_PILOTED",
        "performance_dimensions": ["accuracy", "reliability", "cost", "escalation",
                                   "correction effort", "privacy and safety"],
        "suspension_authority": "Named human service owner and IT security",
        "pilot_evaluation": "NOT_RUN",
    } for t in tasks if t["allocation"] == "AGENT_CANDIDATE_WITH_HUMAN_REVIEW"]
    economics = {
        "baseline_workload_hours": capacity["baseline_hours"],
        "gross_candidate_hours": capacity["gross_candidate_hours"],
        "review_oversight_hours": capacity["oversight_hours"],
        "net_candidate_hours": capacity["net_redeployable_hours_hypothesis"],
        "potential_workload_fte_equivalent": capacity["potential_capacity_to_redeploy_fte_equivalent"],
        "annual_agent_cost_hypothesis_aed": yearly,
        "one_time_cost_hypothesis_aed": startup,
        "value_per_hour_hypothesis_aed": value,
        "actual_cash_savings": None,
        "validated_roi": None,
        "finance_approval": "NOT_OBTAINED",
    }
    if value is not None and yearly is not None and startup is not None:
        opportunity = round(capacity["net_redeployable_hours_hypothesis"] * value, 2)
        economics.update({
            "hypothetical_capacity_opportunity_aed": opportunity,
            "hypothetical_first_year_difference_aed": round(opportunity - yearly - startup, 2),
            "this_is_not_cash_saving": True,
        })
    return {
        "product": PRODUCT, "version": "0.3.0-lab",
        "state": "HOLD_FOR_HUMAN_APPROVAL_NOT_PRODUCTION",
        "source": {"work_design": "synthetic_workforce_redesign.json",
                   "analytics": "separate synthetic_hc_data.json",
                   "fictional": True, "hosted_model_runs": 0},
        "feature_status": dict(FEATURE_STATUS),
        "work_task_intelligence": tasks,
        "role_and_skills_architecture": roles,
        "organizational_digital_twin": _org_tree(case),
        "digital_agent_candidates": agent_register,
        "net_capacity_scenario": capacity,
        "workforce_analytics_separate_case": workforce_intelligence(load_data(), "ALL"),
        "workforce_economics": economics,
        "enterprise_connector_status": dict(CONNECTORS),
        "required_approvals": list(APPROVALS),
        "write_actions_executed": 0,
        "blocked": ["hiring", "termination", "grade_change", "pay_change", "HRIS_write",
                    "agent_deployment", "grant_agent_permissions", "approve_restructure"],
    }

def compare_scenarios(multipliers=(0.0, 0.6, 1.0)):
    out = []
    for factor in multipliers:
        r = blueprint(factor)
        cap = r["net_capacity_scenario"]
        out.append({"adoption_multiplier": factor,
                    "net_candidate_hours": cap["net_redeployable_hours_hypothesis"],
                    "review_hours": cap["oversight_hours"],
                    "potential_workload_fte_equivalent": cap["potential_capacity_to_redeploy_fte_equivalent"],
                    "approval": "HOLD"})
    return {"product": PRODUCT, "status": "SYNTHETIC_COMPARISON", "scenarios": out}

if __name__ == "__main__":
    print(json.dumps(blueprint(), indent=2, ensure_ascii=False))
