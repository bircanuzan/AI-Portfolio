"""Run: python -m unittest discover -s tests -v"""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from corpus_quality import cohen_kappa, inspect_corpus, normalized_text, stratified_sample

def record(**updates):
    row = dict(id="1", language="en", domain="support", register="business",
               source="synthetic", text="Hello world", annotations={"a": "x", "b": "x"}, entities=[])
    row.update(updates)
    return row

class CorpusQualityTests(unittest.TestCase):
    def test_clean_dataset_passes(self):
        report = inspect_corpus([record()])
        self.assertEqual(report["release_decision"], "PASS_AUTOMATED_QA")
        self.assertEqual(report["qa_clean_record_rate"], 1)
    def test_duplicate_detected(self):
        report = inspect_corpus([record(), record(id="2", text="  HELLO   world ")])
        self.assertEqual(report["issues_by_code"]["duplicate_text"], 1)
    def test_encoding_and_rater_disagreement(self):
        report = inspect_corpus([record(text="bad \ufffd", annotations={"a": "x", "b": "y"})])
        self.assertIn("encoding_or_control_character", report["issues_by_code"])
        self.assertIn("annotator_disagreement", report["issues_by_code"])
    def test_invalid_ner_span(self):
        report = inspect_corpus([record(entities=[{"start": 0, "end": 99, "label": "ORG"}])])
        self.assertIn("invalid_entity_offset", report["issues_by_code"])
    def test_pii_review(self):
        report = inspect_corpus([record(text="Email demo@example.test please")])
        self.assertIn("potential_personal_data", report["issues_by_code"])
    def test_kappa(self):
        self.assertEqual(cohen_kappa([("A","A"),("B","B")]), 1)
        self.assertIsNone(cohen_kappa([]))
    def test_stable_multilingual_sampling(self):
        rows = [record(id=str(i), language="tr" if i % 2 else "en") for i in range(10)]
        self.assertEqual([x["id"] for x in stratified_sample(rows)], [x["id"] for x in stratified_sample(rows)])
        self.assertEqual(len(stratified_sample(rows)), 4)
    def test_unicode_normalization(self):
        self.assertEqual(normalized_text(" ＨＥＬＬＯ   "), "hello")

if __name__ == "__main__":
    unittest.main()
