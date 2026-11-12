"""Offline annotation quality audit: fictional data only; no AI model trained."""
import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {"policy", "payroll", "mobility", "recruitment", "benefits", "other"}
RATERS = ("A", "B")

class DataQualityError(ValueError):
    pass

def rows(file, root=ROOT):
    with (root / "data" / file).open(newline="", encoding="utf-8") as handle:
        data = list(csv.DictReader(handle))
    if not data:
        raise DataQualityError(f"Empty dataset: {file}")
    return data

def audit(source, annotations, gold, agreement_threshold=0.80):
    """Strictly validate input and report quality; DO NOT auto-release data."""
    if not 0 <= agreement_threshold <= 1:
        raise ValueError("Threshold must be between zero and one")
    source_ids = [r["case_id"] for r in source]
    if any(not c for c in source_ids) or len(set(source_ids)) != len(source_ids):
        raise DataQualityError("Missing or duplicate source case ID")
    if any(not r.get("case_text", "").strip() for r in source):
        raise DataQualityError("Missing text")
    if any(r.get("synthetic", "").lower() != "true" for r in source):
        raise DataQualityError("Only synthetic source data allowed for public demo")
    ids = set(source_ids)
    label_map = {}
    for a in annotations:
        key = (a["case_id"], a["annotator_id"])
        if a["case_id"] not in ids or a["annotator_id"] not in RATERS:
            raise DataQualityError("Orphaned case or invalid annotator")
        if a["label"] not in ALLOWED:
            raise DataQualityError("Invalid annotation label")
        if key in label_map:
            raise DataQualityError("Duplicate annotation assignment")
        label_map[key] = a["label"]
    expected = {(c, r) for c in source_ids for r in RATERS}
    if set(label_map) != expected:
        raise DataQualityError("Incomplete independent A/B annotation pairs")
    gold_map = {}
    for g in gold:
        if g["case_id"] not in ids or g["gold_label"] not in ALLOWED:
            raise DataQualityError("Invalid gold label / case")
        if g["case_id"] in gold_map:
            raise DataQualityError("Duplicate gold record")
        gold_map[g["case_id"]] = g["gold_label"]
    if set(gold_map) != ids:
        raise DataQualityError("Missing gold records")
    a_counts = Counter(label_map[(c, "A")] for c in source_ids)
    b_counts = Counter(label_map[(c, "B")] for c in source_ids)
    matches = sum(label_map[(c, "A")] == label_map[(c, "B")] for c in source_ids)
    n = len(source_ids)
    observed = matches / n
    expected_chance = sum(a_counts[k] * b_counts[k] for k in ALLOWED) / n**2
    kappa = (observed - expected_chance) / (1 - expected_chance) if expected_chance < 1 else (1.0 if observed == 1 else 0.0)
    conflicts = [c for c in source_ids if label_map[(c, "A")] != label_map[(c, "B")]]
    scores = {r: sum(label_map[(c, r)] == gold_map[c] for c in source_ids) / n for r in RATERS}
    return {
        "source_items": n, "annotations": len(annotations),
        "annotation_completeness": 1.0,
        "observed_agreement": round(observed, 4),
        "cohens_kappa": round(kappa, 4),
        "annotator_gold_accuracy": {k: round(v, 4) for k, v in scores.items()},
        "disagreement_ids": conflicts,
        "disagreements": len(conflicts),
        "calibration_target": agreement_threshold,
        "release_recommendation": "hold_for_recalibration" if observed < agreement_threshold else "pending_human_signoff",
        "integrity_note": "Synthetic example only. Gold and labels created for demonstration."
    }

if __name__ == "__main__":
    import json
    report = audit(rows("source_requests.csv"), rows("annotations.csv"), rows("adjudicated_gold.csv"))
    print(json.dumps(report, indent=2))
