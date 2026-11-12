"""Synthetic organisational evidence gaps. Never grades employers or people."""
import argparse,json
from pathlib import Path
HERE=Path(__file__).resolve().parents[1]
FACTORS={"missing":3,"partial":2,"synthetic_documented":1}
def prioritise(source):
    if not isinstance(source,dict) or source.get("classification")!="SYNTHETIC_ORGANISATION_EVIDENCE_GAPS":
        raise ValueError("Synthetic provenance required")
    rows=source.get("domains")
    if not isinstance(rows,list) or not rows:raise ValueError("No domains")
    out=[];ids=set()
    for r in rows:
        if not isinstance(r,dict):raise ValueError("Bad domain")
        ident=r.get("id")
        if not isinstance(ident,str) or not ident or ident in ids:raise ValueError("Bad or duplicate domain ID")
        ids.add(ident)
        if any(not isinstance(r.get(k),str) or not r[k].strip() for k in ("domain","owner","question")):
            raise ValueError("Missing domain/owner/question")
        impact=r.get("impact_weight")
        if type(impact) is not int or impact not in range(1,6):raise ValueError("Impact must be 1-5")
        if r.get("evidence_status") not in FACTORS:raise ValueError("Unknown evidence status")
        out.append({
            "domain_id":ident,"domain":r["domain"],"human_owner":r["owner"],
            "investigation_priority_index":impact*FACTORS[r["evidence_status"]],
            "evidence_status":r["evidence_status"],"human_review":"PENDING",
            "performance_or_maturity_grade":None
        })
    out.sort(key=lambda x:(-x["investigation_priority_index"],x["domain_id"]))
    return {"classification":"SYNTHETIC_ORGANISATION_EVIDENCE_GAPS",
      "domains_checked":len(out),"evidence_review_queue":out,"release":"HOLD_FOR_HUMAN_VALIDATION",
      "individual_assessment_performed":False,"actual_organisation_maturity_assessed":False,
      "method_limit":"Impact weights and gap statuses are fictitious; index is investigation priority, NOT organisation capability or performance"}
def main():
    args=argparse.ArgumentParser(description=__doc__)
    args.add_argument("--out",default="")
    config=args.parse_args()
    result=json.dumps(prioritise(json.loads((HERE/"data/synthetic_organisational_evidence.json").read_text())),indent=2)+"\n"
    if config.out:Path(config.out).write_text(result,encoding="utf-8")
    print(result,end="")
if __name__=="__main__":main()
