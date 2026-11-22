"""Domain-expert AI training review on authored HR and business examples."""
import json
from collections import defaultdict
from pathlib import Path

rows = [json.loads(s) for s in Path(__file__).with_name("cases.jsonl").read_text().splitlines() if s.strip()]
dimensions = ("accuracy", "practicality", "safety")
scores = defaultdict(list)
flags = []
for r in rows:
    for name in dimensions:
        value = r[name]
        if not isinstance(value, int) or value not in (0, 1, 2):
            raise ValueError(f"{r['id']}: bad {name} rating")
        scores[name].append(value)
    if r["safety"] == 0:
        flags.append({"case": r["id"], "reason": r["rationale"], "domain": r["domain"]})
print(json.dumps({"dataset": "authored synthetic response fixtures",
                  "cases": len(rows),
                  "rating_scale": "0 poor, 1 partial, 2 meets rubric",
                  "average_scores": {k: round(sum(v)/len(v), 2) for k,v in scores.items()},
                  "unsafe_case_reviews": flags}, indent=2))
