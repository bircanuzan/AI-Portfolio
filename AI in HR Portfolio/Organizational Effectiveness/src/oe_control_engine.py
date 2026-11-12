"""Fictional Group OE decision support — offline, deterministic, no external calls.

Run: python "Organizational Effectiveness/src/oe_control_engine.py"
Never automatically approve vacancies, regrade employees or change an HRIS.
"""
import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "synthetic_group_case.json"

def load_case(path=DATA_FILE):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def loaded_cost(base_salary, assumptions):
    return round(base_salary * assumptions["loaded_cost_multiplier"], 2)

def evaluate_role(factors, assumptions):
    weights = assumptions["grade_factor_weights"]
    if set(factors) != set(weights) or any(not isinstance(x, int) or not (0 <= x <= 5) for x in factors.values()):
        raise ValueError("Four integer factor scores from 0 to 5 are required")
    points = round(sum(factors[k] * weights[k] for k in weights) * 2)
    grade = next(item["grade"] for item in assumptions["grade_thresholds"] if points >= item["min"])
    return {"points": points, "illustrative_grade": grade}

def validate_case(case):
    issues = []
    positions = case["positions"]
    people = case["employees"]
    entities = {e["id"] for e in case["entities"]}
    for label, rows, key in [("position", positions, "id"), ("employee", people, "id")]:
        ids = [r[key] for r in rows]
        if len(ids) != len(set(ids)):
            issues.append("duplicate_" + label + "_id")
    active_ids = {p["id"] for p in positions}
    for p in positions:
        if p["entity_id"] not in entities:
            issues.append("unknown_entity:" + p["id"])
        if p["base_salary_aed"] < 0:
            issues.append("negative_salary:" + p["id"])
        if evaluate_role(p["factors"], case["assumptions"])["illustrative_grade"] != p["grade"]:
            issues.append("illustrative_grade_mismatch:" + p["id"])
    occupied = set()
    for person in people:
        pid = person["position_id"]
        if pid not in active_ids:
            issues.append("orphan_position:" + person["id"])
        if pid in occupied:
            issues.append("double_occupied_position:" + pid)
        occupied.add(pid)
    return sorted(set(issues))

def workforce_summary(case):
    assumptions = case["assumptions"]
    filled = {e["position_id"] for e in case["employees"]}
    by_entity = []
    for entity in case["entities"]:
        posts = [p for p in case["positions"] if p["entity_id"] == entity["id"]]
        run_rate = round(sum(loaded_cost(p["base_salary_aed"], assumptions) for p in posts), 2)
        by_entity.append({
            "entity": entity["id"], "approved_cap": entity["approved_positions"],
            "position_records": len(posts),
            "occupied": sum(1 for p in posts if p["id"] in filled),
            "vacant": sum(1 for p in posts if p["id"] not in filled),
            "annual_committed_position_run_rate_aed": run_rate,
            "annual_people_budget_aed": entity["annual_people_budget_aed"],
            "budget_remaining_aed": round(entity["annual_people_budget_aed"] - run_rate, 2),
            "control_breach": len(posts) > entity["approved_positions"] or run_rate > entity["annual_people_budget_aed"]
        })
    return {
        "total_approved_position_records": len(case["positions"]),
        "total_occupied": len(case["employees"]),
        "vacant_position_ids": sorted(p["id"] for p in case["positions"] if p["id"] not in filled),
        "entities": by_entity
    }

def reconcile_payroll(case):
    payroll = {p["employee_id"]: p for p in case["payroll"]}
    current = {p["id"]: p for p in case["employees"]}
    findings = []
    for eid, employee in current.items():
        if eid not in payroll:
            findings.append({"employee": eid, "issue": "missing_from_payroll"})
        elif employee["annual_base_aed"] != payroll[eid]["annual_base_aed"]:
            findings.append({
                "employee": eid, "issue": "base_salary_difference",
                "annual_difference_aed": round(employee["annual_base_aed"] - payroll[eid]["annual_base_aed"], 2)
            })
    for eid in payroll:
        if eid not in current:
            findings.append({"employee": eid, "issue": "payroll_without_hris_employee"})
    return sorted(findings, key=lambda x: (x["employee"], x["issue"]))

def review_hiring_requests(case):
    positions = {p["id"]: p for p in case["positions"]}
    filled = {p["position_id"] for p in case["employees"]}
    vendors = {v["id"]: v for v in case["vendors"]}
    reviewed = []
    for request in case["requests"]:
        reason = ""
        if request["kind"] == "contingent":
            vendor = vendors.get(request.get("vendor_id"))
            if not vendor or not vendor["due_diligence_complete"] or not vendor["classification_review_complete"]:
                route, reason = "HOLD_VENDOR", "Supplier and employment classification controls incomplete"
            elif not request["budgeted"]:
                route, reason = "ESCALATE_HCC", "Contingent spend not budgeted"
            else:
                route, reason = "RECOMMEND_FOR_APPROVAL", "Procurement and Finance must sign"
        elif not request["budgeted"]:
            route, reason = "ESCALATE_HCC", "Unbudgeted position is a reserved matter"
        elif request["position_id"] not in positions:
            route, reason = "HOLD_MASTER_DATA", "Position not in approved ledger"
        elif request["legal_hold"]:
            route, reason = "HOLD_LEGAL", "Rehire requires independent Legal/ER clearance"
        elif request["hiring_freeze_exception"]:
            route, reason = "ESCALATE_CPO", "Hiring freeze exception requires senior decision"
        elif request["position_id"] in filled:
            route, reason = "HOLD_MASTER_DATA", "Position already occupied"
        else:
            position = positions[request["position_id"]]
            cost = loaded_cost(position["base_salary_aed"], case["assumptions"])
            if cost > case["assumptions"]["delegated_people_cost_annual_limit_aed"]:
                route, reason = "ESCALATE_CPO", "Annual loaded cost above fictional delegated limit"
            else:
                route, reason = "RECOMMEND_FOR_APPROVAL", "Human OE and Finance approval still required"
        reviewed.append({"request": request["id"], "recommendation": route, "reason": reason, "automatic_approval": False})
    return reviewed

def automation_impact(case):
    a = case["assumptions"]
    findings = []
    for activity in case["work_activities"]:
        excluded = activity["impact"] == "high"
        hours = 0.0 if excluded else (activity["annual_hours"] * activity["automation_eligible_fraction"] *
                 a["automation_realisation_factor"] * (1 - a["automation_rework_rate"]))
        findings.append({
            "activity": activity["id"], "risk": activity["impact"],
            "excluded_from_capacity_claim": excluded, "theoretical_hours_only": round(hours, 2),
            "human_review_required": True
        })
    return findings

def strategy_scorecard(case):
    entries = case["strategy_deliverables"]
    return {
        "all": len(entries),
        "complete": sum(1 for e in entries if e["status"] == "complete"),
        "at_risk": [e["id"] for e in entries if e["status"] == "at_risk"]
    }

def build_report(case):
    return {
        "case_name": case["case_name"],
        "synthetic": True,
        "issues": validate_case(case),
        "workforce": workforce_summary(case),
        "payroll_reconciliation": reconcile_payroll(case),
        "job_architecture": {p["id"]: evaluate_role(p["factors"], case["assumptions"]) for p in case["positions"]},
        "hiring_decision_support": review_hiring_requests(case),
        "ai_scenario": automation_impact(case),
        "people_strategy_scorecard": strategy_scorecard(case),
        "action": "NONE — human approvals required"
    }

if __name__ == "__main__":
    print(json.dumps(build_report(load_case()), indent=2, ensure_ascii=False))
