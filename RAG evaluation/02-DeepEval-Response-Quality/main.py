"""Run with deepeval test run main.py; evaluation uses a configured LLM."""
from deepeval import assert_test
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, SingleTurnParams

def test_response_correctness():
    case = LLMTestCase(
        input="What is the demo expense limit?",
        actual_output="The example policy caps expenses at USD 100.",
        expected_output="The example expense policy limit is USD 100.",
    )
    metric = GEval(
        name="Correctness",
        criteria="Does the actual answer agree factually with the expected answer?",
        evaluation_params=[SingleTurnParams.ACTUAL_OUTPUT, SingleTurnParams.EXPECTED_OUTPUT],
        threshold=0.7,
    )
    assert_test(case, [metric])
