import unittest
from evaluate import score, check_splits, run


class EvaluationTests(unittest.TestCase):
    def test_schema_and_errors(self):
        self.assertTrue(score("billing", '{"intent":"billing"}')["correct_intent"])
        self.assertFalse(score("billing", '{"intent":"technical"}')["correct_intent"])
        for output in ['oops', '[]', 'null', '{"intent":null}',
                       '{"intent":"billing","extra":1}']:
            self.assertFalse(score("billing", output)["valid_schema"])

    def test_leakage_and_duplicate_ids(self):
        rows = [{"id":"a", "text":"Hello WORLD", "split":"train"},
                {"id":"b", "text":" hello  world ", "split":"test"}]
        with self.assertRaises(ValueError):
            check_splits(rows)
        with self.assertRaises(ValueError):
            check_splits([rows[0], rows[0]])

    def test_held_out_only(self):
        rows = [{"id":"a","text":"train","split":"train","expected":"billing","output":"bad"},
                {"id":"b","text":"test","split":"test","expected":"billing","output":'{"intent":"billing"}'}]
        self.assertEqual(run(rows)["intent_accuracy"], 1.0)
        self.assertEqual(run(rows)["test_cases"], 1)
        with self.assertRaises(ValueError):
            run(rows[:1])


if __name__ == "__main__":
    unittest.main()
