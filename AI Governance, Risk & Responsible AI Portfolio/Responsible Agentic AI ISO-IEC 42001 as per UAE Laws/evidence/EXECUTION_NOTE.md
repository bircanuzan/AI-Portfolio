# Local execution evidence — 2 November 2026
Environment: local Python 3 runtime; external dependencies none. **No LLM/API, browser, ATS, actual candidate data or deployed HumanEvoX application used.**

## Exactly what was executed
```bash
python -m unittest discover -s tests -v
python src/governance_gate.py > evidence/local_result.json
```
**Observed results:** 9 unit tests passed; **12 authored synthetic expected-vs-actual governance decisions matched**, 0 failures. The gate returned ALLOW_DEMO_ONLY, ESCALATE_HUMAN or DENY decisions and reason-coded control IDs.

**Method limitation:** the same project author prepared the expected decisions and deterministic evaluation rules; therefore 12/12 is a local software regression result, not independent assurance or empirical model evaluation. This record does not certify compliance. For reproduced exact JSON output, run the CLI as shown.

## Actual issues/exceptions identified
- This is a control-design demonstration; no production IAM, audit-log immutability or human approval service exists.
- The prompt-injection field is a **pre-labelled synthetic signal**, not an adversarial text detector.
- The demo accepts Boolean fields such as `lawful_basis_recorded` as inputs; it does **not** independently validate legal sufficiency.
- Legal source currency, fairness and live model responses remain untested.
- No project hours or professional experience are assigned to any individual.

## Next objective evidence milestone
With explicit authorization and appropriate privacy/security controls, integrate a real LLM test environment, capture **prompts, model/tool responses, versions and independent assessment**, document actual defects and reviewer sign-offs. Until then, use “local deterministic governance prototype” in CVs and client discussions.
