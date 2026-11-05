# Observed test findings — 29 October 2026

## Method
Ran actual JavaScript function `respond(prompt)` on 28 authored prompts in the execution environment. Compared *returned* decision and policy reference against a predeclared expected outcome. The complete returned text and audit fields are in [dated JSON](2026-10-29_test_run.json). This is a reproducible **program test**, not assessment of an LLM, retrieval-augmented generation (RAG), Copilot Studio, tenant permissions, security posture or employee outcomes. Test cases and expected answers were created by the same project authoring process; they are not independently validated. No statistical confidence is claimed.

## Results
- 26/28 pass; 2 fail; correctness 92.9%.
- Human-required cases were routed to human decisions in this authored set: 100.0% (small-set observation only).
- Refusals do not prove data containment or access control because there are **no integrations at all**.
- `T27`: “Can I have my holiday quota?” expected generic leave guidance; actual: `HUMAN_ESCALATION`. Vocabulary coverage gap.
- `T28`: “Can you arrange proof of employment?” expected approval-required request; actual: `HUMAN_ESCALATION`. Intent synonym gap.
- Both are conservative non-answers rather than unauthorised disclosure; they still reduce employee service value. 

## Review decision: HOLD
Do not present this as a Copilot Studio deployment, agentic autonomy, enterprise-ready system, certified governance or client case. Next: introduce approved synonym routing and run regression tests; provision Copilot Studio; test real LLM outputs with diverse prompts, model/version trace, retrieval citations, red-team and multi-turn scenarios; run security and permission verification with an independent reviewer and explicit risk sign-offs.

## Evidence integrity
The JSON file was generated from the same executable `respond` logic committed in `agent.js`; it records actual outputs, not individually hand-written model responses. The code is intentionally simple and non-ML. Retest with `node test_agent.js --save` to produce a fresh dated file. Manual examples elsewhere are not counted as tested outputs.
