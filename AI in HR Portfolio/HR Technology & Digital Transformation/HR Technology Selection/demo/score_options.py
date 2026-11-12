"""Synthetic HR-tech vendor scoring. NOT a real vendor assessment or procurement decision."""
from __future__ import annotations
import csv
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
WEIGHTS = {
    "functional": Decimal("0.30"),
    "security": Decimal("0.25"),
    "integration": Decimal("0.20"),
    "experience": Decimal("0.15"),
    "cost": Decimal("0.10"),
}

def rank_options(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    result = []
    for row in rows:
        if not row.get("name", "").strip():
            raise ValueError("Option name is required")
        mandatory_passed = (row["mandatory_security_pass"].lower() == "true"
                            and row["mandatory_privacy_pass"].lower() == "true")
        total = Decimal("0")
        for k, w in WEIGHTS.items():
            score = Decimal(row[k])
            if not score.is_finite() or not (0 <= score <= 5):
                raise ValueError(f"Invalid 0-5 score: {k}")
            total += score * w
        result.append({
            "option": row["name"],
            "eligible": mandatory_passed,
            "score_out_of_5": str(total.quantize(Decimal("0.01"))),
            "decision": "SHORTLIST_FOR_REVIEW" if mandatory_passed else "INELIGIBLE_MANDATORY_GATE",
        })
    return sorted(result, key=lambda x: (not x["eligible"], -Decimal(x["score_out_of_5"]), x["option"]))

def main() -> None:
    with (HERE / "synthetic_vendor_scores.csv").open(encoding="utf-8", newline="") as handle:
        results = rank_options(list(csv.DictReader(handle)))
    for x in results:
        print(f'{x["option"]}: {x["score_out_of_5"]}/5 | {x["decision"]}')

if __name__ == "__main__":
    main()
