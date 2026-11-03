"""Structural audit of 17 original Claude workflow skills, not an LLM execution."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FOLDER=ROOT.parent
STAGES={"Requisition and Role Design","Structured Selection","Candidate Coordination","Offer and Handoff","Cross-Border Risk"}
def check(manifest,base=FOLDER):
    if manifest.get("classification")!="SYNTHETIC_WORKFLOW_DESIGNS_ONLY":
        raise ValueError("Bad provenance")
    flows=manifest.get("flows")
    if not isinstance(flows,list) or len(flows)!=17 or manifest.get("count")!=17:
        raise ValueError("Missing or additional Claude workflow design")
    errors=[];seen=set()
    for flow in flows:
        name=flow.get("folder","")
        if not isinstance(name,str) or not name.startswith("Claude AI in HR - ") or "/" in name or ".." in name or name in seen:
            errors.append("INVALID_OR_DUPLICATE_FOLDER");continue
        seen.add(name)
        if flow.get("stage") not in STAGES or not flow.get("human_reviewer") or flow.get("source_required") is not True or flow.get("external_action")!="NONE":
            errors.append(name+":BAD_STAGE_OR_HUMAN_GATE")
        path=base/name
        for file in ("README.md","SKILL.md"):
            if not (path/file).is_file():errors.append(name+":MISSING_"+file)
        skill=path/"SKILL.md"
        if skill.is_file():
            txt=skill.read_text(encoding="utf-8")
            if "required_human_review" not in txt or "must NOT decide" not in txt:
                errors.append(name+":MISSING_REQUIRED_HUMAN_REVIEW")
    return {"claude_workflows":len(seen),"valid":not errors,"errors":errors,
            "claude_run_performed":False,"hiring_authorized":False}
if __name__=="__main__":
    print(json.dumps(check(json.loads((ROOT/"workflow_catalog.json").read_text())),indent=2))
