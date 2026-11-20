import hashlib
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from manager import AgentManager, evaluate


class ManagementTests(unittest.TestCase):
    def test_labelled_cases_and_outputs(self):
        cases = json.loads((ROOT / "data/cases.json").read_text())
        metrics, _ = evaluate(cases)
        self.assertEqual(metrics["outcome_and_output_matches"], len(cases))

    def test_caller_cannot_self_approve(self):
        task = {"id": "x", "action": "route_workflow", "document": "route this",
                "risk": "high", "confidence": 1, "approved": True}
        self.assertEqual(AgentManager().run(task)["status"], "review")

    def test_audit_hash_chain_and_tamper_detection(self):
        cases = json.loads((ROOT / "data/cases.json").read_text())
        _, events = evaluate(cases)
        prev = "GENESIS"
        for event in events:
            stored_hash = event["hash"]
            body = {k: v for k, v in event.items() if k != "hash"}
            self.assertEqual(body["previous_hash"], prev)
            self.assertEqual(hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest(), stored_hash)
            prev = stored_hash
        events[0]["status"] = "tampered"
        body = {k: v for k, v in events[0].items() if k != "hash"}
        self.assertNotEqual(hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest(), events[0]["hash"])

    def test_duplicate_does_not_repeat_execution(self):
        manager = AgentManager()
        task = {"id": "once", "action": "route_workflow", "document": "routing",
                "risk": "low", "confidence": .9}
        self.assertEqual(manager.run(task)["status"], "completed")
        self.assertEqual(manager.run(task)["attempts"], 0)


if __name__ == "__main__":
    unittest.main()
