"""Offline validator for human-scored, synthetic AI response reviews."""
import json
import sys

WEIGHTS = {"factual_support": .35, "relevance": .20, "coherence": .15,
           "instruction_following": .20, "completeness": .10}
LABELS = {"fact_error","irrelevant","ambiguous","incoherent",
          "instruction_failure","missing_evidence","acceptable"}

def assess(record):
    required = ("id","domain","rubric_version","source_context","scores","labels","feedback")
    if any(not record.get(k) for k in required):
        raise ValueError("missing required field")
    scores = record["scores"]
    if set(scores) != set(WEIGHTS) or any(type(scores[k]) is not int or not 0 <= scores[k] <= 4 for k in WEIGHTS):
        raise ValueError("invalid rubric scores")
    if not set(record["labels"]).issubset(LABELS):
        raise ValueError("unknown defect label")
    total = round(sum(scores[k] * weight for k,weight in WEIGHTS.items()), 2)
    return {"id": record["id"], "weighted_score_of_4": total,
            "disposition": "human_escalation" if scores["factual_support"] == 0
               else ("accept" if total >= 3.25 else "revise"),
            "feedback": record["feedback"]}

if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf-8") as f:
        data = json.load(f)
    print(json.dumps([assess(r) for r in data], indent=2))
