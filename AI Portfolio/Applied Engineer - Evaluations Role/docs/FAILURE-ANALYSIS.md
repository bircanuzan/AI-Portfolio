# Evidence-driven failure analysis and false-positive controls

## Tax-before-discount bug (functional regression)

- Case IDs: PR101-C02 and PR101-C03.
- Expected: tax is assessed on the discounted subtotal.
- Candidate fault: synthetic patch calculates tax on gross subtotal.
- Reproduction: `python benchmark.py`; inspect matching `records` in `artifacts/benchmark-results.json`.
- Reviewer decision: **candidate functional failure**, supported by literal expected/observed values.

## Downward-rounding bug (functional regression)

- Case ID: PR101-C04.
- Expected tax: 0.02 (0.30 × 5% = 0.015, half-up).
- Faulty patch tax: 0.01 (round-down).
- Reviewer decision: **candidate functional failure**; independent edge-case assertion.

## Environment versus candidate fault

A timeout, unavailable runner or filesystem failure is tagged `environment-or-infrastructure`. Such errors are not automatically attributed to the candidate implementation. A re-run on a healthy environment plus confirmed matching setup is required before model-failure attribution.

## Rubric safeguards

- 10 stable case identifiers, literal test oracles and explicit category weights.
- Duplicate test IDs, missing categories and weights that do not total 100 reject the evaluation.
- Each record preserves `case_id`, `expected`, `observed`, `status` and `failure_type`.
- Repeated deterministic evaluation is tested via `test_scores_are_repeatable`.
- Scores describe **synthetic local patch performance** only, not accuracy rates for commercial AI agents.

## Extend to real-world repository evaluations

Use a real open-source repository and explicitly licensed, reviewable PRs. Pin commit SHA and dependencies; document OS/Python versions and network restrictions; run a baseline; apply the candidate patch; run relevant focused and whole-suite tests; inspect logs; collect stdout, stderr, diffs and trace IDs; separate flaky tests from patch regressions; and confirm each failure by reproduction. Never run arbitrary external agent-generated code in a privileged or network-enabled CI runner.
