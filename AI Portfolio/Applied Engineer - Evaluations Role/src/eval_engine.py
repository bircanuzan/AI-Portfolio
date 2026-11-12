"""Deterministic patch benchmarking with evidence-linked failure records.

No remote code execution and no real LLM agent integration. The benchmark
runs trusted, locally defined synthetic candidate patches only.
"""
from collections import defaultdict


def classify_exception(exc):
    if isinstance(exc, (TimeoutError, OSError, ConnectionError)):
        return "environment-or-infrastructure"  # review; not automatic candidate fault
    return "candidate-runtime-error"


def run_case(candidate_name, implementation, case):
    record = {"candidate": candidate_name, "case_id": case["id"],
              "category": case["category"], "status": None, "failure_type": None,
              "expected": case["expected"], "observed": None}
    args = case["input"]
    try:
        result = implementation(args["lines"], args["tax_rate"], args["discount_rate"])
        record["observed"] = result
        if "raises" in case["expected"]:
            record["status"] = "fail"
            record["failure_type"] = "validation-missed"
        elif result == case["expected"]:
            record["status"] = "pass"
        else:
            record["status"] = "fail"
            record["failure_type"] = "functional-regression"
    except Exception as exc:  # isolated test harness records unexpected outcomes
        record["observed"] = {"exception": type(exc).__name__, "message": str(exc)}
        if type(exc).__name__ == case["expected"].get("raises"):
            record["status"] = "pass"
        else:
            record["status"] = "error"
            record["failure_type"] = classify_exception(exc)
    return record


def validate_rubric(rubric, cases):
    weights = rubric["category_weights"]
    if set(weights) != {c["category"] for c in cases}:
        raise ValueError("rubric categories must exactly match evaluation case categories")
    if sum(weights.values()) != 100 or any(not isinstance(w, int) or w <= 0 for w in weights.values()):
        raise ValueError("rubric category weights must be positive integers totaling 100")
    case_ids = [case["id"] for case in cases]
    if len(case_ids) != len(set(case_ids)):
        raise ValueError("duplicate case identifiers are not allowed")


def score_runs(records, rubric):
    by_category = defaultdict(list)
    for item in records:
        by_category[item["category"]].append(item)
    score = 0.0
    for category, weight in rubric["category_weights"].items():
        items = by_category[category]
        if not items:
            raise ValueError("missing rubric category")
        score += weight * sum(item["status"] == "pass" for item in items) / len(items)
    return round(score, 2)


def run_benchmark(candidates, cases, rubric):
    validate_rubric(rubric, cases)
    results = []
    for name, implementation in candidates.items():
        records = [run_case(name, implementation, case) for case in cases]
        results.append({
            "candidate": name, "score": score_runs(records, rubric),
            "passed": sum(r["status"] == "pass" for r in records),
            "total": len(records), "records": records,
        })
    return results
