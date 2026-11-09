# Evaluation Grader Failure Triage

An **independent, synthetic evaluation QA demonstration** for separating genuine candidate defects from false-positive grading, false-negative grading and invalid test environments.

This is a small-scale, inspectable engineering example—not a claim of running external models, maintaining a major production codebase, or contributing to an upstream open-source repository.

## Question answered

When a coding-agent candidate and an LLM judge disagree with an executable test oracle, what failed: the candidate, the grading rubric or the evaluation environment?

The triage policy applies **environment health first**, then compares the independent executable oracle with the grader verdict:

| Oracle | Grader | Classification |
|---|---|---|
| pass | pass | verified pass |
| fail | fail | genuine candidate failure |
| fail | pass | grader false positive |
| pass | fail | grader false negative |
| any | any | environment invalid when execution is unhealthy |

## Run

```bash
cd Evaluation-Grader-Failure-Triage
python -m unittest discover -s tests -v
python triage.py
```

Python 3.10+ standard library only.

## Scope and evidence

- `triage.py`: deterministic failure attribution engine and JSON report.
- `fixtures/judgments.json`: clearly labeled synthetic examples.
- `tests/test_triage.py`: all classification branches and environment precedence.
- `../.github/workflows/coding-agent-evaluation-labs.yml`: CI configuration.

In a real coding-agent evaluation, the oracle would come from a frozen executable test suite with captured exit codes, test logs, commits, and dependency versions. These fixtures supply those verdicts for demonstration and do not independently prove real model behavior.
