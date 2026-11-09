# Qualitative LLM grading protocol — source-grounded design

This project **does not invoke an LLM or claim model-run results**. It includes an actual line-citation validator so a future human or LLM reviewer can be audited.

## Prompt template for a future external reviewer

> Assess a candidate code patch against PR-101's acceptance criteria. Use only the provided repository snapshot, task specification and test logs. For every pass or fail judgment, include the case ID, a rubric criterion from `rubrics/qualitative_review.json`, an exact repository-relative file path, one-indexed line number and an exact source quote. If the available materials do not support a decision, return `abstain` with a reason. Do not infer a model's internal reasoning or claim benchmark success from superficial code style. Distinguish candidate bugs from environment failures.

## Strict JSON shape

```json
{
  "case_id": "PR101-C02",
  "criterion": "implementation-explanation",
  "verdict": "pass",
  "evidence": [
    {"path": "src/invoice.py", "line": 1, "quote": "Reference implementation"}
  ]
}
```

The reusable `src/review_validator.py::validate_review` checks schema, allowed criteria, path safety, actual line numbers and exact source quotations. `tests/test_review_validator.py` tests valid citations, missing evidence, invented quotes, path traversal, invalid line numbers and abstention.

## Review conflict resolution

1. Prefer executable assertions and source output over persuasive but unsupported narrative.
2. Check environment reproducibility and compare a clean reference run.
3. Request human review of ambiguous interpretations; do not silently average contradictory judgments.
4. Record judge identity/version, source SHA, prompt version and rationale before model-to-model comparisons.
5. Only report actual model results when real agent outputs, hashes, test logs and scoring records have been captured.
