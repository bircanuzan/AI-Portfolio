"""Aggregate human-scored evaluation results. NOT an automated semantic judge."""
import argparse
import csv
import json
from pathlib import Path

WEIGHTS = {"structure":20, "evidence":20, "quantitative":20, "craft":15, "implementation":15, "governance":10}
CRITICAL = {"fabricated_evidence", "material_formula_error", "wrong_units",
            "unapproved_disclosure", "unsupported_decision", "unowned_control"}

def score_one(row):
    grades = {}
    for key in WEIGHTS:
        try:
            value = int(row[key])
        except (ValueError, KeyError, TypeError):
            raise ValueError(f"{row.get('task_id','?')} invalid grade for {key}")
        if value < 0 or value > 4:
            raise ValueError(f"{row.get('task_id','?')} {key} must be in [0,4]")
        grades[key] = value
    defects = [d.strip() for d in (row.get("critical_defects") or "").split("|") if d.strip()]
    unknown = set(defects) - CRITICAL
    if unknown:
        raise ValueError(f"Unknown critical defects: {sorted(unknown)}")
    raw = round(sum(grades[k] * w / 4 for k, w in WEIGHTS.items()), 2)
    critical = bool(defects)
    final = min(raw, 49.0) if critical else raw
    status = "FAIL" if critical or final < 50 else ("EXEMPLAR_REVIEW" if final >= 85 else ("MINOR_REVISIONS" if final >= 70 else "REWORK"))
    return {"task_id": row["task_id"], "raw_score": raw, "final_score": final,
            "status": status, "critical_defects": "|".join(defects),
            "rationale": row.get("rationale", ""), **{f"grade_{k}": v for k,v in grades.items()}}

def evaluate(ratings, tasks):
    valid_ids = {t["task_id"] for t in tasks}
    if len(valid_ids) != len(tasks):
        raise ValueError("Duplicate benchmark task IDs")
    seen = set()
    result = []
    for row in ratings:
        task_id = row["task_id"]
        if task_id not in valid_ids:
            raise ValueError(f"Unknown task ID {task_id}")
        if task_id in seen:
            raise ValueError(f"Duplicate reviewer row for {task_id}")
        seen.add(task_id)
        result.append(score_one(row))
    return result

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--ratings", default="data/reviewer_ratings.csv")
    p.add_argument("--tasks", default="data/benchmark_tasks.json")
    p.add_argument("--out", default="evaluation_results.csv")
    a = p.parse_args()
    with open(a.ratings, newline="", encoding="utf-8") as stream:
        ratings = list(csv.DictReader(stream))
    tasks = json.loads(Path(a.tasks).read_text(encoding="utf-8"))
    result = evaluate(ratings, tasks)
    if result:
        with open(a.out, "w", newline="", encoding="utf-8") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(result[0].keys()))
            writer.writeheader()
            writer.writerows(result)
    print(json.dumps({"reviewed": len(result), "results": result, "out": a.out}, indent=2))

if __name__ == "__main__":
    main()

