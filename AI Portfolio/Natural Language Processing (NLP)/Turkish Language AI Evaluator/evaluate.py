"""Aggregate human-entered Turkish language AI evaluations.

Does not automatically verify factuality, interpret Turkish, or analyze images.
Python 3.10+; standard library only.
"""
from __future__ import annotations
import argparse
from collections import Counter
import json
from pathlib import Path

DIMENSIONS = ("alignment", "coherence", "groundedness", "fluency", "cultural_tone")
ISSUE_CODES = {
    "message_drift", "unsupported_claim", "contradiction",
    "visual_attribute_mismatch", "fluency", "tone_cultural_nuance",
    "needs_verification", "other",
}
SEVERITIES = ("low", "medium", "high", "critical")

def validate(rows: list[dict]) -> list[str]:
    """Return clearly located schema/annotation issues for human QA repair."""
    errors: list[str] = []
    seen: set[str] = set()
    for n, row in enumerate(rows, 1):
        tag = str(row.get("item_id") or f"row-{n}")
        if tag in seen:
            errors.append(f"{tag}: duplicate item_id")
        seen.add(tag)
        if row.get("language") != "tr":
            errors.append(f"{tag}: expected language=tr")
        for key in ("prompt", "ai_output", "reference_evidence"):
            if not isinstance(row.get(key), str) or not row[key].strip():
                errors.append(f"{tag}: missing {key}")
        annotations = row.get("annotations")
        if not isinstance(annotations, list) or not annotations:
            errors.append(f"{tag}: annotations must be a nonempty list")
            continue
        for j, annotation in enumerate(annotations):
            aid = f"{tag}/reviewer-{j+1}"
            if not isinstance(annotation, dict):
                errors.append(f"{aid}: invalid annotation")
                continue
            scores = annotation.get("scores")
            if not isinstance(scores, dict):
                errors.append(f"{aid}: missing scores")
            else:
                for dimension in DIMENSIONS:
                    value = scores.get(dimension)
                    if type(value) is not int or value not in (0, 1, 2, 3):
                        errors.append(f"{aid}: {dimension} must be integer 0..3")
            codes = annotation.get("issue_codes")
            if not isinstance(codes, list) or any(c not in ISSUE_CODES for c in codes):
                errors.append(f"{aid}: invalid issue_codes")
            if annotation.get("severity") not in SEVERITIES:
                errors.append(f"{aid}: invalid severity")
            if not isinstance(annotation.get("rater"), str) or not annotation["rater"].strip():
                errors.append(f"{aid}: missing rater")
            if not isinstance(annotation.get("feedback"), str) or not annotation["feedback"].strip():
                errors.append(f"{aid}: missing actionable feedback")
            if isinstance(codes, list) and "visual_attribute_mismatch" in codes and not row.get("visual_reference"):
                errors.append(f"{aid}: visual mismatch requires supplied visual metadata")
    return errors

def summarize(rows: list[dict]) -> dict:
    errors = validate(rows)
    if errors:
        return {"status": "INVALID_INPUT", "record_count": len(rows), "validation_errors": errors}
    issue_counts: Counter[str] = Counter()
    severity_counts: Counter[str] = Counter()
    dimension_totals: Counter[str] = Counter()
    review_count = 0
    adjudication_ids = []
    for row in rows:
        annotations = row["annotations"]
        for ann in annotations:
            review_count += 1
            issue_counts.update(ann["issue_codes"])
            severity_counts[ann["severity"]] += 1
            for dimension, rating in ann["scores"].items():
                dimension_totals[dimension] += rating
        if len(annotations) > 1:
            signatures = {
                (tuple(sorted(a["issue_codes"])), tuple(a["scores"][d] for d in DIMENSIONS))
                for a in annotations
            }
            if len(signatures) > 1:
                adjudication_ids.append(row["item_id"])
        if any(a["severity"] == "critical" for a in annotations):
            adjudication_ids.append(row["item_id"])
    adjudication_ids = list(dict.fromkeys(adjudication_ids))
    return {
        "status": "REVIEW_REQUIRED" if adjudication_ids or issue_counts else "NO_ISSUES_FLAGGED",
        "dataset": "synthetic_hand_annotated_demo",
        "record_count": len(rows),
        "review_count": review_count,
        "issue_counts": dict(issue_counts),
        "severity_counts": dict(severity_counts),
        "mean_dimension_scores_0_to_3": {
            dim: round(dimension_totals[dim] / review_count, 3) if review_count else None
            for dim in DIMENSIONS
        },
        "adjudication_item_ids": adjudication_ids,
        "interpretation": "Descriptive aggregation of human annotations only; not automated AI evaluation."
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=str(Path(__file__).parent / "data" / "synthetic_turkish_evaluations.jsonl"))
    parser.add_argument("--output")
    args = parser.parse_args()
    with open(args.input, encoding="utf-8") as handle:
        rows = [json.loads(line) for line in handle if line.strip()]
    result = summarize(rows)
    output = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        path = Path(args.output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    if result["status"] == "INVALID_INPUT":
        raise SystemExit(1)

if __name__ == "__main__":
    main()
