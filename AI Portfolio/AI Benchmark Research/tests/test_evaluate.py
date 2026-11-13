"""Deterministic unit tests; no live model calls or network requests."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from evaluate import (canonical_url, evaluate, grade_run, load_jsonl,
                      normalize_answer, validate_tasks)


ROOT = Path(__file__).resolve().parents[1]
TASKS = load_jsonl(ROOT / "data" / "benchmark_tasks.jsonl")
RUNS = load_jsonl(ROOT / "data" / "synthetic_model_runs.jsonl")


class BenchmarkTests(unittest.TestCase):
    def test_source_backed_tasks_validate(self):
        validate_tasks(TASKS)
        self.assertEqual(len(TASKS), 4)

    def test_duplicate_tasks_rejected(self):
        with self.assertRaisesRegex(ValueError, "Duplicate task"):
            validate_tasks(TASKS + [TASKS[0]])

    def test_missing_canonical_answer_alias_rejected(self):
        task = dict(TASKS[0], accepted_answers=["totally different"])
        with self.assertRaisesRegex(ValueError, "canonical answer"):
            validate_tasks([task])

    def test_non_https_source_rejected(self):
        task = dict(TASKS[0], sources=[{"url": "http://example.com"}])
        with self.assertRaisesRegex(ValueError, "HTTPS"):
            validate_tasks([task])

    def test_answer_normalization(self):
        self.assertEqual(normalize_answer("  STD   97  "), "std 97")
        self.assertEqual(canonical_url("HTTPS://OPENAI.COM/index/browsecomp/?x=1"),
                         "https://openai.com/index/browsecomp")

    def test_correct_cited_answer(self):
        item = grade_run(TASKS[0], RUNS[0])
        self.assertEqual(item["verdict"], "correct")
        self.assertTrue(item["cited_primary_source"])
        self.assertFalse(item["review_required"])

    def test_wrong_answer_without_primary(self):
        item = grade_run(TASKS[0], RUNS[1])
        self.assertEqual(item["verdict"], "incorrect")
        self.assertEqual(item["diagnosis"], "missing_primary_source")
        self.assertTrue(item["review_required"])

    def test_wrong_answer_despite_primary_retrieval(self):
        item = grade_run(TASKS[1], RUNS[2])
        self.assertEqual(item["diagnosis"], "reasoning_or_extraction_error")
        self.assertTrue(item["retrieved_primary_source"])

    def test_abstention(self):
        item = grade_run(TASKS[2], RUNS[3])
        self.assertEqual(item["verdict"], "not_attempted")
        self.assertEqual(item["diagnosis"], "abstention")

    def test_uncited_correct_answer_flag(self):
        run = dict(RUNS[0], sources_used=[])
        self.assertTrue(grade_run(TASKS[0], run)["uncited_correct_answer"])

    def test_aggregated_replay_counts(self):
        report = evaluate(TASKS, RUNS)
        self.assertEqual(report["verdict_counts"],
                         {"correct": 3, "incorrect": 2, "not_attempted": 1})
        self.assertEqual(report["run_mode_counts"], {"synthetic": 6})

    def test_unknown_task_refused(self):
        bad = dict(RUNS[0], task_id="UNKNOWN")
        with self.assertRaisesRegex(ValueError, "Unknown task_id"):
            evaluate(TASKS, [bad])


if __name__ == "__main__":
    unittest.main()
