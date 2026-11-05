"""Executable sanity tests for synthetic claim triage: no insurer UAT implied."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from demo import make_synthetic_claims, validate_data, run  # noqa: E402


class SyntheticClaimDemoTests(unittest.TestCase):
    def test_repeatability(self):
        a = make_synthetic_claims(120)
        b = make_synthetic_claims(120)
        self.assertTrue(a.equals(b))

    def test_valid_input(self):
        report = validate_data(make_synthetic_claims(120))
        self.assertEqual(report["status"], "pass")

    def test_duplicate_rejected(self):
        df = make_synthetic_claims(120)
        df.loc[1, "claim_id"] = df.loc[0, "claim_id"]
        self.assertEqual(validate_data(df)["status"], "fail")

    def test_negative_amount_rejected(self):
        df = make_synthetic_claims(120)
        df.loc[0, "claim_amount_aed"] = -1
        self.assertEqual(validate_data(df)["status"], "fail")

    def test_personal_field_rejected(self):
        df = make_synthetic_claims(120)
        df["email"] = "no-person@example.invalid"
        report = validate_data(df)
        self.assertEqual(report["status"], "fail")
        self.assertIn("email", report["unexpected_columns"])

    def test_suggestion_is_not_an_adverse_claim_decision(self):
        import tempfile
        import pandas as pd
        with tempfile.TemporaryDirectory() as directory:
            summary = run(Path(directory), n=150)
            sample = pd.read_csv(Path(directory) / "review_queue_sample.csv")
            self.assertEqual(summary["train_rows"] + summary["holdout_rows"], 150)
            self.assertTrue(sample["review_score"].between(0, 1).all())
            self.assertTrue(set(sample["suggested_route"]).issubset({"human_review", "standard_queue"}))
            self.assertTrue(((sample["review_score"] >= 0.40) ==
                             (sample["suggested_route"] == "human_review")).all())


if __name__ == "__main__":
    unittest.main()
