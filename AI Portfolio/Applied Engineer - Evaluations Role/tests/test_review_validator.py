import unittest
from src.review_validator import validate_review


class GroundedReviewTests(unittest.TestCase):
    def valid_review(self):
        return {
            "case_id": "PR101-C02",
            "criterion": "implementation-explanation",
            "verdict": "pass",
            "evidence": [
                {"path": "src/invoice.py", "line": 1, "quote": "Reference implementation"}
            ],
        }

    def test_accepts_real_source_line(self):
        self.assertEqual(validate_review(self.valid_review())["verdict"], "pass")

    def test_rejects_fabricated_quote(self):
        record = self.valid_review()
        record["evidence"][0]["quote"] = "invented production claim"
        with self.assertRaises(ValueError):
            validate_review(record)

    def test_rejects_missing_evidence(self):
        record = self.valid_review()
        record["evidence"] = []
        with self.assertRaises(ValueError):
            validate_review(record)

    def test_rejects_path_traversal(self):
        record = self.valid_review()
        record["evidence"][0]["path"] = "../../outside.json"
        with self.assertRaises(ValueError):
            validate_review(record)

    def test_rejects_invalid_line(self):
        record = self.valid_review()
        record["evidence"][0]["line"] = 100000
        with self.assertRaises(ValueError):
            validate_review(record)

    def test_abstention_requires_reason(self):
        record = {"case_id": "PR101-C02", "criterion": "abstention", "verdict": "abstain"}
        with self.assertRaises(ValueError):
            validate_review(record)
        record["reason"] = "Incomplete source snapshot"
        self.assertEqual(validate_review(record)["verdict"], "abstain")

    def test_rejects_unknown_criterion(self):
        record = self.valid_review()
        record["criterion"] = "invented-criterion"
        with self.assertRaises(ValueError):
            validate_review(record)


if __name__ == "__main__":
    unittest.main()
