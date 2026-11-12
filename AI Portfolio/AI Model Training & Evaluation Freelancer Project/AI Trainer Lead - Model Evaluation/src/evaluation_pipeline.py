"""Deterministic aggregation of *human-entered* AI evaluation ratings."""
import json
import sys
from collections import defaultdict

WEIGHTS = {"factual_accuracy": .30,"relevance": .15,"reasoning_coherence": .20,
           "instruction_adherence": .15,"domain_safety": .10,"completeness": .10}
SENSITIVE = {"finance","healthcare","legal"}

def evaluate(review):
    for k in ("task_id","domain","reviewer","rubric_version","feedback"):
        if not review.get(k):raise ValueError("missing "+k)
    scores=review.get("scores",{})
    if set(scores)!=set(WEIGHTS):
        raise ValueError("incorrect criteria")
    if any(type(scores[k]) is not int or not 0<=scores[k]<=4 for k in WEIGHTS):
        raise ValueError("ratings must be integers in [0,4]")
    score=round(sum(scores[k]*WEIGHTS[k] for k in WEIGHTS),2)
    escalation=(scores["factual_accuracy"]==0 or scores["domain_safety"]==0
        or (review["domain"] in SENSITIVE and
            min(scores["factual_accuracy"],scores["domain_safety"]) < 3))
    return {"task_id":review["task_id"],"domain":review["domain"],
            "rating_of_4":score,"escalation":escalation,
            "decision":"expert_review" if escalation else ("accept" if score>=3.25 else "revise"),
            "feedback":review["feedback"]}

def summary(reviews):
    results=[evaluate(x) for x in reviews]
    groups=defaultdict(list)
    for x in results:groups[x["domain"]].append(x)
    return {"records":results,"domain_metrics":{
        d:{"n":len(v),"average_rating_of_4":round(sum(x["rating_of_4"] for x in v)/len(v),2),
           "expert_review_count":sum(x["escalation"] for x in v)}
        for d,v in sorted(groups.items())}}

if __name__=="__main__":
    with open(sys.argv[1],encoding="utf-8") as f:data=json.load(f)
    print(json.dumps(summary(data),indent=2))
