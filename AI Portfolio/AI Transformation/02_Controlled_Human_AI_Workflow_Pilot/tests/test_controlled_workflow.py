import importlib.util
from pathlib import Path
import unittest

PATH = Path(__file__).resolve().parents[1] / "src" / "controlled_workflow.py"
SPEC = importlib.util.spec_from_file_location("controlled_workflow", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

class WorkflowTests(unittest.TestCase):
    def request(self, **changes):
        r = {"case_id":"TEST", "actor_role":"hr", "classification":"restricted",
             "source_approved":True, "action":"draft_answer"}
        r.update(changes)
        return MODULE.route(r)

    def test_sample_cases(self):
        self.assertEqual([x["decision"] for x in MODULE.run()], [
            "DRAFT_FOR_HUMAN_REVIEW", "DENY_ACCESS", "HOLD_SOURCE_VALIDATION",
            "HUMAN_APPROVAL_REQUIRED", "BLOCK_EXTERNAL_SIDE_EFFECT"
        ])

    def test_restricted_source_needs_hr(self):
        self.assertEqual(self.request(actor_role="manager")["decision"], "DENY_ACCESS")

    def test_no_auto_execution_even_when_approved(self):
        self.assertEqual(self.request(action="publish_external")["decision"], "BLOCK_EXTERNAL_SIDE_EFFECT")

    def test_unknown_action_is_blocked(self):
        self.assertEqual(self.request(action="delete_employee_record")["decision"], "BLOCK_UNSUPPORTED_ACTION")

    def test_no_source_content_in_audit(self):
        result = MODULE.route({**{"case_id":"TEST","actor_role":"hr","classification":"internal",
            "source_approved":True,"action":"draft_answer"}, "secret":"SYNTHETIC-SECRET"})
        self.assertNotIn("secret", result)
        self.assertNotIn("SYNTHETIC-SECRET", str(result))

if __name__ == "__main__":
    unittest.main()
