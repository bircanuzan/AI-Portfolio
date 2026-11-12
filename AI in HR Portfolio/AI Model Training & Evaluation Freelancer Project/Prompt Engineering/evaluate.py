"""Simple lexical regression harness. Not a semantic or safety guarantee."""
import argparse
import json
from pathlib import Path
def grade(cases, responses):
    lookup = {r["id"]:r for r in responses}
    if len(lookup) != len(responses):
        raise ValueError("duplicate ID")
    rows=[]
    for c in cases:
        r=lookup.get(c["id"], {})
        msg=str(r.get("message","")).casefold()
        reasons=[]
        if r.get("decision") != c["expected"]: reasons.append("wrong/missing decision")
        for token in c.get("required",[]):
            if token.casefold() not in msg: reasons.append("missing: "+token)
        for token in c.get("forbidden",[]):
            if token.casefold() in msg: reasons.append("forbidden: "+token)
        rows.append({"id":c["id"],"category":c["category"],"pass":not reasons,"issues":reasons})
    return {"passed":sum(r["pass"] for r in rows),"total":len(rows),"rows":rows}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--responses",required=True,type=Path)
    args=p.parse_args()
    root=Path(__file__).resolve().parent
    result=grade(json.loads((root/"eval_set.json").read_text()),json.loads(args.responses.read_text()))
    print(json.dumps(result,indent=2))
    raise SystemExit(0 if result["total"]==result["passed"] else 1)
