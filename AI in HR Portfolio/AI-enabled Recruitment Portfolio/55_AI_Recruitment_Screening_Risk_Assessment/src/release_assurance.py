"""Portfolio evidence gate: never authorize real candidate decisions or ATS deployment."""
import argparse,csv,json
from pathlib import Path
from screening_audit import audit
from catalog_integrity import check
ROOT=Path(__file__).resolve().parents[1]
def evaluate(result,risks,catalog):
    blockers=[]
    if result["unjustified_flawed_flips"]>0:blockers.append("UNJUSTIFIED_FLAWED_SCREENING_FLIPS")
    if not catalog["valid"]:blockers.append("CLAUDE_WORKFLOW_INTEGRITY")
    blockers += ["NO_REAL_SELECTION_VALIDITY_OR_FAIRNESS_STUDY",
                 "NO_APPLICABLE_LEGAL_PRIVACY_ACCESSIBILITY_APPROVAL",
                 "NO_HUMAN_SIGNOFF_OR_ATS_INTEGRATION_EVIDENCE"]
    return {"classification":"SYNTHETIC_RECRUITMENT_ASSURANCE",
      "paired_tests":result["pairs"],"unjustified_flawed_flips":result["unjustified_flawed_flips"],
      "unjustified_controlled_reference_flips":result["unjustified_controlled_flips"],
      "risk_items":len(risks),"critical_risks":sum(r.get("severity")=="CRITICAL" for r in risks),
      "claude_designs":catalog["claude_workflows"],"claude_integrity_pass":catalog["valid"],
      "production_release":"HOLD","controlled_reference_approved":False,
      "human_hiring_decision_required":True,"external_actions_performed":False,
      "release_blockers":blockers,
      "disclosure":"Synthetic offline testing only; no real ATS, LLM, candidate or client work"}
def report():
    cases=json.loads((ROOT/"data/paired_synthetic_candidate_tests.json").read_text())["conditions"]
    with (ROOT/"data/risk_register.csv").open(encoding="utf-8",newline="") as f:
        risks=list(csv.DictReader(f))
    catalog=check(json.loads((ROOT/"workflow_catalog.json").read_text()))
    return evaluate(audit(cases),risks,catalog)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--out",default="")
    a=p.parse_args();s=json.dumps(report(),indent=2)+"\n"
    if a.out:Path(a.out).write_text(s)
    print(s,end="")
