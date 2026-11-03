"""Fictional healthcare-requisition integrity check, never professional licensure clearance."""
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def assess(role):
    if not isinstance(role,dict):
        return {"role_id":"INVALID","status":"HOLD","gaps":["INVALID_ROLE"],"licence_verified":False,"hiring_authorized":False}
    gaps=[]
    for k in ("id","market","location","role","clinical_owner","hr_owner"):
        if not isinstance(role.get(k),str) or not role[k].strip():gaps.append(k)
    if not isinstance(role.get("skills"),list) or not role["skills"] or any(not isinstance(s,str) or not s.strip() for s in role["skills"]):
        gaps.append("skills")
    if type(role.get("licence_review_required")) is not bool:gaps.append("licence_review_required")
    if role.get("licence_review_required") is True:
        for k in ("official_rule_source","policy_version"):
            if not isinstance(role.get(k),str) or not role[k].strip():gaps.append(k)
        if role.get("official_rule_verified") is not True:gaps.append("OFFICIAL_RULE_NOT_VERIFIED")
    if role.get("role_brief_signed") is not True:gaps.append("HUMAN_ROLE_APPROVAL_PENDING")
    return {"role_id":role.get("id","UNKNOWN"),"status":"READY_FOR_FURTHER_HUMAN_VERIFICATION" if not gaps else "HOLD",
      "gaps":gaps,"licence_verified":False,"hiring_authorized":False}
def report(payload):
    if not isinstance(payload,dict) or payload.get("classification")!="SYNTHETIC_ONLY":
        raise ValueError("Only explicitly synthetic role briefs are accepted")
    rows=payload.get("roles")
    if not isinstance(rows,list) or not rows:raise ValueError("No role briefs")
    out=[assess(r) for r in rows]
    ids=[r["role_id"] for r in out]
    if len(ids)!=len(set(ids)):raise ValueError("Duplicate role ids")
    return {"classification":"SYNTHETIC_ONLY","role_count":len(out),"human_review_required":True,
      "production_release":"HOLD","results":out,
      "disclosure":"No real role licensure, regulations or candidate credentials verified"}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--out",default="")
    args=p.parse_args()
    out=json.dumps(report(json.loads((ROOT/"data/synthetic_healthcare_role_briefs.json").read_text())),indent=2)+"\n"
    if args.out:Path(args.out).write_text(out)
    print(out,end="")
if __name__=="__main__":main()
