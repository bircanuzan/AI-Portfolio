"""Synthetic assessment-centre evidence scoring and calibration.

Educational portfolio only; not validated psychometric scoring or hiring.
"""
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RATERS = {"A", "B"}
COMPETENCIES = {
    "analytical_thinking",
    "stakeholder_management",
    "decision_making",
    "coaching_development",
}
EXERCISES = {"in_basket", "role_play", "group_discussion"}


class AssessmentDataError(ValueError):
    """Input structure, content or integration is inconsistent."""


def read_csv(filename, data_dir=None):
    base = Path(data_dir) if data_dir else ROOT / "data"
    with (base / filename).open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def assess(observations, adjudicated):
    """Validate assessor records, report independent agreement and integrated scores.

    Each evidence item has two independent ratings and one explicitly reviewed
    final rating. No automatic decisions about candidate suitability are made.
    """
    if not observations or not adjudicated:
        raise AssessmentDataError("No observation or adjudication records")

    notes = {}
    source_meta = {}
    for row in observations:
        evidence_id = row.get("evidence_id", "").strip()
        rater = row.get("assessor_id", "").strip()
        exercise = row.get("exercise", "").strip()
        competency = row.get("competency", "").strip()
        behavior = row.get("behavioral_evidence", "").strip()
        if not evidence_id or rater not in RATERS or exercise not in EXERCISES:
            raise AssessmentDataError("Invalid evidence ID, assessor or exercise")
        if competency not in COMPETENCIES or not behavior:
            raise AssessmentDataError("Unknown competency or missing behavioral evidence")
        try:
            rating = int(row["rating"])
        except (TypeError, ValueError, KeyError):
            raise AssessmentDataError("Rating must be an integer from 1 to 5") from None
        if str(rating) != row["rating"].strip() or rating not in range(1, 6):
            raise AssessmentDataError("Rating must be an integer from 1 to 5")
        key = (evidence_id, rater)
        if key in notes:
            raise AssessmentDataError("Duplicate assessor observation")
        old = source_meta.setdefault(evidence_id, (exercise, competency, behavior))
        if old != (exercise, competency, behavior):
            raise AssessmentDataError("Assessors disagree on source evidence metadata")
        notes[key] = rating

    expected = {(eid, rater) for eid in source_meta for rater in RATERS}
    if expected != set(notes):
        raise AssessmentDataError("Each item needs independent A and B rating")

    finals = {}
    for row in adjudicated:
        eid = row.get("evidence_id", "").strip()
        reason = row.get("adjudication_rationale", "").strip()
        if eid not in source_meta or eid in finals or not reason:
            raise AssessmentDataError("Missing, duplicated or unsupported adjudication")
        try:
            final_rating = int(row["final_rating"])
        except (TypeError, ValueError, KeyError):
            raise AssessmentDataError("Final rating must be an integer 1 to 5") from None
        if str(final_rating) != row["final_rating"].strip() or final_rating not in range(1, 6):
            raise AssessmentDataError("Final rating must be an integer 1 to 5")
        finals[eid] = final_rating
    if set(finals) != set(source_meta):
        raise AssessmentDataError("Every evidence item needs integrated rating")

    groups = defaultdict(list)
    a_counts, b_counts = Counter(), Counter()
    exact = 0
    disagreements = []
    for eid, (_, comp, _) in source_meta.items():
        a, b = notes[(eid, "A")], notes[(eid, "B")]
        a_counts[a] += 1
        b_counts[b] += 1
        exact += a == b
        if a != b:
            disagreements.append(eid)
        groups[comp].append(finals[eid])

    if set(groups) != COMPETENCIES or any(len(x) != 3 for x in groups.values()):
        raise AssessmentDataError("Expected three observations per four competencies")

    n = len(source_meta)
    observed_agreement = exact / n
    expected_chance = sum(a_counts[r] * b_counts[r] for r in range(1, 6)) / (n * n)
    kappa = ((observed_agreement - expected_chance) / (1 - expected_chance)
             if expected_chance < 1 else (1 if observed_agreement == 1 else 0))

    raw_scores = {c: sum(vals) / len(vals) for c, vals in groups.items()}
    overall = sum(raw_scores.values()) / len(raw_scores)

    return {
        "observed_items": n,
        "independent_ratings": len(notes),
        "exact_agreement": round(observed_agreement, 4),
        "cohens_kappa": round(kappa, 4),
        "disagreement_evidence_ids": sorted(disagreements),
        "integrated_competency_scores": {
            c: round(score, 2) for c, score in sorted(raw_scores.items())
        },
        "descriptive_overall_mean": round(overall, 2),
        "lowest_scoring_competency": min(raw_scores, key=raw_scores.get),
        "caveat": "Synthetic unvalidated exercise; not an employment decision or normed test.",
    }


if __name__ == "__main__":
    summary = assess(
        read_csv("assessor_observations.csv"),
        read_csv("adjudicated_ratings.csv")
    )
    print(json.dumps(summary, indent=2))
