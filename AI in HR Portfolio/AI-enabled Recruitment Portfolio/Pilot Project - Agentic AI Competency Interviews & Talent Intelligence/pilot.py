"""Synthetic, offline structured interview pilot. No LLM, voice or candidate decision."""
import argparse
import json
from pathlib import Path

BLUEPRINT = Path(__file__).with_name("blueprint.json")


def load_blueprint(path=BLUEPRINT):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    items = data["competencies"]
    if not items or sum(item["weight"] for item in items) != 100:
        raise ValueError("Weights must total 100")
    if len(set(item["id"] for item in items)) != len(items):
        raise ValueError("Competency IDs must be unique")
    for item in items:
        if set(item["anchors"]) != {"1", "2", "3", "4", "5"}:
            raise ValueError("Each competency requires five anchors")
    return data


def start(blueprint, consent):
    if consent is not True:
        raise PermissionError("Recorded consent required")
    return {"role": blueprint["role"], "version": blueprint["version"],
            "consent": True, "answers": {}}


def questions(blueprint):
    return [{"competency": c["id"], "question": c["question"]}
            for c in blueprint["competencies"]]


def answer(session, blueprint, competency_id, response):
    known = {c["id"]: c for c in blueprint["competencies"]}
    if not session.get("consent") or competency_id not in known:
        raise PermissionError("Consent and known competency required")
    if competency_id in session["answers"]:
        raise ValueError("Duplicate answer in demo")
    if not isinstance(response, str) or not response.strip():
        raise ValueError("Empty answer")
    response = response.strip()
    session["answers"][competency_id] = response
    # Length is only a standardized trigger for clarification, NOT a skill score.
    return {"clarification": known[competency_id]["probe"]
            if len(response.split()) < 12 else None,
            "rating": "HUMAN_REVIEW_REQUIRED"}


def report(session, blueprint, human_reviewer, human_ratings):
    if not human_reviewer or not str(human_reviewer).strip():
        raise ValueError("Human reviewer ID required")
    if not session.get("consent"):
        raise PermissionError("Consent required")
    expected = {c["id"] for c in blueprint["competencies"]}
    if set(session["answers"]) != expected or set(human_ratings) != expected:
        raise ValueError("All answers and human reviews required")
    rows = []
    for c in blueprint["competencies"]:
        rating = human_ratings[c["id"]]
        score = rating["score"]
        quote = rating["quote"]
        rationale = rating["rationale"]
        if type(score) is not int or not 1 <= score <= 5:
            raise ValueError("Score must be human-provided integer 1–5")
        if not isinstance(quote, str) or not quote.strip() or quote not in session["answers"][c["id"]]:
            raise ValueError("Evidence quote must occur verbatim in original answer")
        if not isinstance(rationale, str) or len(rationale.strip()) < 8:
            raise ValueError("Reviewer rationale required")
        rows.append({"competency": c["name"], "human_score": score,
                     "weight": c["weight"], "anchor": c["anchors"][str(score)],
                     "evidence_quote": quote, "reviewer_rationale": rationale})
    return {"status": "SYNTHETIC_HUMAN_REVIEWED_DEMO",
            "role": session["role"], "blueprint_version": session["version"],
            "human_reviewer": human_reviewer,
            "ratings": rows,
            "weighted_arithmetic_mean_of_human_ratings": round(
                sum(r["human_score"] * r["weight"] for r in rows) / 100, 2),
            "NOT_validated_for_hiring": True,
            "decision": "No employment decision; human owner required"}


def run_demo():
    blueprint = load_blueprint()
    session = start(blueprint, consent=True)
    fictional_responses = {
        "api": "In a fictional integration I used OAuth scopes, idempotency keys and synthetic failure tests to check retry handling.",
        "security": "I limited read access to job-required fields and required an HR approval before allowing a fictional employee update.",
        "evaluation": "I reproduced a duplicate webhook event in a local test and introduced a repeatable regression test to detect recurrence.",
        "stakeholder": "When a stakeholder requested automatic decisions I documented the risks and agreed a human reviewer checkpoint with them."
    }
    reviews = {}
    for c in blueprint["competencies"]:
        reply = fictional_responses[c["id"]]
        answer(session, blueprint, c["id"], reply)
        reviews[c["id"]] = {"score": 3, "quote": reply[:40],
                            "rationale": "Human fictional input only; not an AI-rated candidate."}
    print(json.dumps(report(session, blueprint, "fictional-assessor-001", reviews), indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true", required=True,
                        help="Run synthetic offline human-scored example")
    parser.parse_args()
    run_demo()
