"""Synthetic evaluator calibration and adjudication queue."""
import json
from pathlib import Path

rows = [json.loads(s) for s in Path(__file__).with_name("cases.jsonl").read_text().splitlines() if s.strip()]
disagreements = []
for r in rows:
    for score in (r["reviewer_a"], r["reviewer_b"], r["adjudicated"]):
        if score not in (0, 1, 2):
            raise ValueError(f"Score outside 0/1/2 rubric in {r['id']}")
    if r["reviewer_a"] != r["reviewer_b"]:
        disagreements.append({"id": r["id"], "severity": r["severity"],
                              "reviewer_a": r["reviewer_a"], "reviewer_b": r["reviewer_b"],
                              "adjudicated": r["adjudicated"]})
print(json.dumps({"source": "fictional reviewer ratings, not real annotators",
                  "cases": len(rows),
                  "exact_reviewer_agreement": round((len(rows)-len(disagreements))/len(rows), 3),
                  "adjudication_queue": disagreements,
                  "critical_adjudications": sum(r["severity"]=="critical" for r in disagreements)}, indent=2))
