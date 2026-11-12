# Research/evaluation signal gate

1. Define intended capability and failure taxonomy before collecting samples.
2. Specify task schema, data provenance, completion criteria and disallowed leakage.
3. Calibrate two domain reviewers on anchor examples; log disagreement.
4. Track sampling coverage, severe errors and evaluator confidence.
5. Halt release claims if coverage < 90%, agreement < 80%, or severe defects unresolved. Thresholds are illustrative, not research-validated.
6. Create an iteration ticket linking failure class, corrected task and reviewer signoff.

**Expected deliverables:** task schema, data dictionary, discrepancy log, calibration record, pass/hold decision and limits statement.

**Exclusions:** RL environment implementation, production ownership, published benchmark or measured model lift are not demonstrated by this project.