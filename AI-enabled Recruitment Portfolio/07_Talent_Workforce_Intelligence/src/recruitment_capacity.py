"""Fictional TA review workload, not conversion forecasting or candidate ranking."""
import argparse,csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FIELDS={"requisition_id","market","role_family","hiring_demand","fictional_review_queue","review_hours_per_profile","reviewer_hours_available"}
def evaluate(rows):
    if not rows:raise ValueError("Empty requisition source")
    seen=set();result=[]
    for i,r in enumerate(rows,1):
        if set(r)!=FIELDS or any(not isinstance(v,str) or not v.strip() for v in r.values()):
            raise ValueError("Bad schema or blank values")
        rid=r["requisition_id"]
        if rid in seen:raise ValueError("Duplicate requisition id")
        seen.add(rid)
        try:
            demand=int(r["hiring_demand"]);queue=int(r["fictional_review_queue"])
            rate=float(r["review_hours_per_profile"]);hours=float(r["reviewer_hours_available"])
        except ValueError as exc:raise ValueError("Bad numeric input") from exc
        if str(demand)!=r["hiring_demand"] or str(queue)!=r["fictional_review_queue"]:
            raise ValueError("Demand and queue must be integers")
        if not(demand>0 and queue>=0 and 0<rate<=16 and 0<=hours<=1000):
            raise ValueError("Invalid workload assumptions")
        workload=round(queue*rate,2)
        result.append({"requisition_id":rid,"market":r["market"],"role_family":r["role_family"],
          "hiring_demand":demand,"fictional_review_queue":queue,
          "review_queue_coverage":round(queue/demand,2),
          "review_workload_hours":workload,"available_hours":round(hours,2),
          "review_hour_gap":round(max(0,workload-hours),2),
          "human_action":"REVIEW_REQUIREMENTS_AND_CAPACITY",
          "candidate_quality_or_hire_prediction":False})
    return {"classification":"SYNTHETIC_REVIEW_WORKLOAD_ONLY",
      "requisitions":len(result),"notional_hiring_demand":sum(r["hiring_demand"] for r in result),
      "fictional_queue_total":sum(r["fictional_review_queue"] for r in result),
      "review_capacity_gap_hours":round(sum(r["review_hour_gap"] for r in result),2),
      "records":result,"automated_hiring":False,
      "interpretation":"Queue counts are not qualified applicants, placement forecasts, actual talent market data or hiring probabilities"}
def read(path):
    with Path(path).open(encoding="utf-8-sig",newline="") as f:
        reader=csv.DictReader(f)
        if set(reader.fieldnames or [])!=FIELDS:raise ValueError("Invalid header")
        return list(reader)
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--out",default="")
    a=p.parse_args()
    data=json.dumps(evaluate(read(ROOT/"data/synthetic_recruitment_capacity.csv")),indent=2)+"\n"
    if a.out:Path(a.out).write_text(data)
    print(data,end="")
if __name__=="__main__":main()
