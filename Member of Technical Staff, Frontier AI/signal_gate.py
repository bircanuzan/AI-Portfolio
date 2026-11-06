import json
from pathlib import Path

def gate(runs, minimum_coverage=.9, minimum_agreement=.8):
    planned=sum(r["planned_cases"] for r in runs)
    completed=sum(r["completed_cases"] for r in runs)
    agreed=sum(r["matched_reviews"] for r in runs)
    reviewed=sum(r["double_reviewed"] for r in runs)
    critical=sum(r["critical_defects"] for r in runs)
    coverage=completed/planned if planned else 0
    agreement=agreed/reviewed if reviewed else 0
    blockers=[]
    if coverage<minimum_coverage: blockers.append("insufficient_scenario_coverage")
    if agreement<minimum_agreement: blockers.append("low_reviewer_agreement")
    if critical: blockers.append("unresolved_critical_defects")
    return {"status":"HOLD" if blockers else "READY_FOR_HUMAN_REVIEW",
            "coverage":round(coverage,3),"agreement":round(agreement,3),
            "blockers":blockers,"note":"Synthetic proxy metrics only"}

if __name__=="__main__":
    data=json.loads(Path(__file__).with_name("synthetic_runs.json").read_text())
    print(json.dumps(gate(data),indent=2))
