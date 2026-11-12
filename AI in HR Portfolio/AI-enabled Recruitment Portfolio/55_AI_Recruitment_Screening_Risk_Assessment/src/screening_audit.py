"""Project 55: deterministic mock screener, paired stability audit, human-review gate.

All CV features are invented. This is not an AI model or a real recruitment system.
"""
import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def screen(candidate, controlled=False):
    """Return mock score/route; the flawed mode intentionally uses inappropriate proxies."""
    score = 12 * candidate["skills"] + 8 * candidate["work_sample"]
    if not controlled:
        if candidate["cv_format"] == "scanned":
            score -= 14
        if candidate["career_gap_years"] > 1:
            score -= 12
        if candidate["name_token"] == "B":
            score -= 8
        if candidate["keyword_density"] >= 8:
            score += 10
        if candidate["accented_text"]:
            score -= 8
        if not candidate["cover_letter"]:
            score -= 7
        if not candidate["linkedin_url"]:
            score -= 7
        if candidate["section_order"] == "unusual":
            score -= 9
        if candidate["font_type"] == "decorative":
            score -= 10
    decision = "ADVANCE" if candidate["required_license"] and score >= 60 else "REVIEW"
    return {"score": score, "decision": decision}

def audit(cases):
    items = []
    for pair in cases:
        original = screen(pair["baseline"], False)
        alternate = screen(pair["variation"], False)
        corrected_original = screen(pair["baseline"], True)
        corrected_alternate = screen(pair["variation"], True)
        flip = original["decision"] != alternate["decision"]
        corrected_flip = corrected_original["decision"] != corrected_alternate["decision"]
        expect_stable = pair["expected_decision_stable"]
        items.append({
            "id": pair["id"], "expect_stable": expect_stable,
            "flawed_flip": flip, "controlled_flip": corrected_flip,
            "unjustified_flawed_flip": expect_stable and flip,
            "unjustified_controlled_flip": expect_stable and corrected_flip
        })
    return {
        "pairs": len(items),
        "unjustified_flawed_flips": sum(x["unjustified_flawed_flip"] for x in items),
        "unjustified_controlled_flips": sum(x["unjustified_controlled_flip"] for x in items),
        "results": items
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="", help="Optional JSON audit destination")
    args = parser.parse_args()
    cases = json.loads((ROOT / "data/paired_synthetic_candidate_tests.json").read_text())["conditions"]
    with (ROOT / "data/risk_register.csv").open(newline="", encoding="utf-8") as f:
        risks = list(csv.DictReader(f))
    report = audit(cases)
    report["risks"] = len(risks)
    report["release_gate"] = "HOLD" if report["unjustified_flawed_flips"] else "REVIEW"
    text = json.dumps(report, indent=2)
    print(text)
    if args.out:
        Path(args.out).write_text(text + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
