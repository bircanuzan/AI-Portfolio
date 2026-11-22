"""Deterministic output-quality scorer; authored responses, no LLM API used."""
import json
from pathlib import Path

cases = [json.loads(s) for s in Path(__file__).with_name("cases.jsonl").read_text().splitlines() if s.strip()]
results = []
for r in cases:
    try:
        payload = json.loads(r["response"])
        schema_ok = isinstance(payload, dict) and set(payload) == {"intent"} and payload["intent"] in ("billing", "technical", "unknown")
    except (ValueError, TypeError):
        schema_ok = False
        payload = None
    intent_ok = bool(schema_ok and payload["intent"] == r["expected_intent"])
    if r["human_quality"] not in (0, 1, 2):
        raise ValueError(f"Unrecognized authored human quality label {r['id']}")
    results.append({"id": r["id"], "schema_valid": schema_ok,
                    "intent_correct": intent_ok,
                    "authored_human_quality": r["human_quality"]})
print(json.dumps({"source": "synthetic, outputs manually authored",
                  "cases": len(results),
                  "schema_valid_rate": round(sum(r["schema_valid"] for r in results)/len(results), 3),
                  "exact_intent_accuracy_rate": round(sum(r["intent_correct"] for r in results)/len(results), 3),
                  "review_records": results}, indent=2))
