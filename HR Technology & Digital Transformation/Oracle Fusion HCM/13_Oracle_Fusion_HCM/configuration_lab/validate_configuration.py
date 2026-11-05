"""Synthetic Oracle HCM workforce-configuration dependency checker; NOT tenant configuration."""
import json
from datetime import date
from pathlib import Path
from collections import Counter

ROOT=Path(__file__).resolve().parent
COLLECTIONS=("legal_employers","business_units","departments","jobs","grades","locations","positions")
def validate(payload):
    errors=[]
    if not isinstance(payload,dict) or payload.get("model_status")!="SYNTHETIC_NONPRODUCTION":
        return {"valid":False,"errors":["NOT_SYNTHETIC_NONPRODUCTION"],"oracle_configured":False}
    idx={}
    for table in COLLECTIONS:
        rows=payload.get(table,[])
        if not isinstance(rows,list):
            errors.append(table+":NOT_LIST");rows=[]
        valid=[r for r in rows if isinstance(r,dict) and isinstance(r.get("code"),str) and r["code"].strip()]
        if len(valid)!=len(rows):errors.append(table+":INVALID_RECORD")
        duplicates=[code for code,n in Counter(r["code"] for r in valid).items() if n>1]
        errors.extend(table+":DUPLICATE:"+code for code in duplicates)
        idx[table]={r["code"]:r for r in valid}
    le,bu,dept=idx["legal_employers"],idx["business_units"],idx["departments"]
    for code,r in bu.items():
        if r.get("legal_employer") not in le:errors.append(code+":UNKNOWN_LEGAL_EMPLOYER")
        if not isinstance(r.get("set"),str) or not r["set"]:errors.append(code+":MISSING_BU_SET")
    for code,r in dept.items():
        owner=bu.get(r.get("business_unit"))
        if not owner:errors.append(code+":UNKNOWN_DEPARTMENT_BU")
        elif r.get("set") not in ("COMMON",owner.get("set")):errors.append(code+":DEPARTMENT_SET_MISMATCH")
    for code,r in idx["positions"].items():
        owner=bu.get(r.get("business_unit"))
        if not owner:errors.append(code+":UNKNOWN_POSITION_BU")
        d=dept.get(r.get("department"))
        if not d or d.get("business_unit")!=r.get("business_unit"):
            errors.append(code+":POSITION_DEPARTMENT_MISMATCH")
        for table,field in (("jobs","job"),("grades","grade"),("locations","location")):
            referenced=idx[table].get(r.get(field))
            if not referenced:errors.append(code+":UNKNOWN_"+table.upper())
            elif owner and referenced.get("set") not in ("COMMON",owner.get("set")):
                errors.append(code+":INACCESSIBLE_SET_"+table.upper())
        fte=r.get("fte")
        if isinstance(fte,bool) or not isinstance(fte,(int,float)) or not (0<fte<=1):
            errors.append(code+":INVALID_FTE")
        try:
            value=r["effective_start"]
            if not isinstance(value,str) or date.fromisoformat(value).isoformat()!=value:raise ValueError
        except (KeyError,TypeError,ValueError):
            errors.append(code+":INVALID_EFFECTIVE_DATE")
    changes=payload.get("changes",[])
    if not isinstance(changes,list):errors.append("CHANGES_NOT_LIST");changes=[]
    for i,r in enumerate(changes):
        if not isinstance(r,dict):errors.append("CHANGE_INVALID_RECORD");continue
        if r.get("position") not in idx["positions"]:errors.append("CHANGE_UNKNOWN_POSITION")
        maker,approver=r.get("maker"),r.get("approver")
        if not isinstance(maker,str) or not maker or not isinstance(approver,str) or not approver:
            errors.append("CHANGE_MISSING_REVIEWER")
        elif maker==approver:errors.append("CHANGE_SELF_APPROVAL")
    return {"valid":not errors,"errors":errors,"oracle_configured":False,
            "objects_checked":{name:len(idx[name]) for name in COLLECTIONS}}

if __name__=="__main__":
    data=json.loads((ROOT/"configuration_synthetic.json").read_text(encoding="utf-8"))
    print(json.dumps(validate(data),indent=2))
