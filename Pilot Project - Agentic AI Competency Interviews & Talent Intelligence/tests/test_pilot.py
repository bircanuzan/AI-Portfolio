"""python -m unittest discover -s tests -v"""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pilot import load_blueprint, start, questions, answer, report


class PilotTests(unittest.TestCase):
    def setUp(self):
        self.plan = load_blueprint()
        self.session = start(self.plan, True)
        self.ratings = {}
        for c in self.plan["competencies"]:
            text = "I implemented a tested synthetic integration with explicit logging and approval."
            answer(self.session, self.plan, c["id"], text)
            self.ratings[c["id"]] = {"score": 3, "quote": "I implemented a tested",
                                      "rationale": "Human fictional review with specific evidence."}

    def test_consent(self):
        with self.assertRaises(PermissionError):
            start(self.plan, False)

    def test_consistent_primary_questions(self):
        self.assertEqual(questions(self.plan), questions(self.plan))
        self.assertEqual(len(questions(self.plan)), 4)

    def test_quote_provenance(self):
        self.ratings["api"]["quote"] = "This text was never said"
        with self.assertRaises(ValueError):
            report(self.session, self.plan, "reviewer", self.ratings)

    def test_requires_named_human_reviewer(self):
        with self.assertRaises(ValueError):
            report(self.session, self.plan, "", self.ratings)

    def test_requires_complete_review(self):
        del self.ratings["api"]
        with self.assertRaises(ValueError):
            report(self.session, self.plan, "reviewer", self.ratings)

    def test_invalid_score(self):
        self.ratings["api"]["score"] = 6
        with self.assertRaises(ValueError):
            report(self.session, self.plan, "reviewer", self.ratings)

    def test_score_not_generated_by_answer(self):
        self.assertNotIn("rating", self.session)
        self.assertEqual(len(self.session["answers"]), 4)

    def test_weighted_arithmetic_from_human_ratings(self):
        r = report(self.session, self.plan, "reviewer", self.ratings)
        self.assertEqual(r["weighted_arithmetic_mean_of_human_ratings"], 3.0)
        self.assertTrue(r["NOT_validated_for_hiring"])

    def test_short_answer_prompts_fixed_clarification(self):
        session = start(self.plan, True)
        result = answer(session, self.plan, "api", "I built an API.")
        self.assertEqual(result["clarification"], self.plan["competencies"][0]["probe"])

    def test_cannot_submit_twice(self):
        with self.assertRaises(ValueError):
            answer(self.session, self.plan, "api", "Other response")


if __name__ == "__main__":
    unittest.main()
