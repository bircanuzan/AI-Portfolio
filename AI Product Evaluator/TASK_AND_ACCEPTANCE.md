# Evaluation protocol

1. Read the task brief verbatim; identify required steps and prohibited actions.
2. Record model/version, run date, prompt, scenario, output, platform status and token/usage-limit constraints.
3. Verify required steps from on-screen or stored evidence. Never infer a completion from assistant assurances alone.
4. Mark missing/unexpected steps and false success claims; attach exact evidence snippets.
5. If a run resets or fails, record retry ID and avoid silently merging attempts.
6. Independent human reviewer checks semantic correctness and policy sensitivity.

**Acceptance:** every test has task ID, expected/actual outputs, anomaly category, evidence reference and pass/fail reason. No live models are evaluated by the offline sample.