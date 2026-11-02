# HR Service Q&A assistant — controlled evaluation design

## Hypothetical UAE client problem
Routine HR requests consume time and create contradictory advice when policies lack version control. Exceptions, confidential matters, statutory entitlements and individual rights should **not** be handled by an unauthenticated chatbot.

## Scope of this runnable proof of concept
- Five original **fictional internal workflow** source documents, each with ID and version.
- Offline deterministic keyword routing; answer is returned **verbatim from catalog**, not produced by an LLM.
- Four outcomes: **ANSWER** (cites fictional source), **ESCALATE** (human HR case), **REFUSE** (third-party information) and **UNKNOWN** (out-of-library).
- 20 named question tests with **expected route, expected policy, actual answer, versioned citation and result**.

## Evaluation matrix
| Category | Cases | Expected |
|---|---|---|
| Standard policy navigation | Q01–Q10 | Answer, cite correct document; two paraphrase gaps are included |
| Human exception / grievance | Q11–Q14 | Escalate, never invent decisions |
| Third-party privacy | Q15–Q17 | Refuse disclosure |
| Personal authenticated data | Q18 | Escalate securely |
| Unknown topic | Q19 | State unknown, no policy fabrication |
| Statutory entitlement | Q20 | Escalate, do not invent a UAE legal entitlement |

## Scoring
Pass requires **both route and policy ID** to match the independent expected labels. A wrong source ID counts as a failure. A response is not legally correct merely because its category matches. The reference JSON preserves the full actual response and test mismatch.

## Risks and mitigations
1. Phrase variation ("working from home", "working extra hours"): negative tests remain visible; remediate with explicit synonym coverage or a validated enterprise retrieval layer.
2. Prompt confusion between self-information and third-party data: require authenticated access for personal HR queries; do not connect to HRIS until independently reviewed.
3. Missing statutory or locally required detail: avoid generating entitlement amounts; route to official HR/legal channels.
4. Confidential matters: secure case routing with privacy logging and human SLA, not chat storage.
5. Source freshness: assigned policy owner, version, approval date, deprecation process and re-test trigger.

## Future validation for a hosted LLM / Copilot Studio
Deploy only when an authorised tenant, security review and approved policy corpus exist. Capture exact provider/model/version, tokens/costs, reproducible prompts, actual unredacted outputs in access-controlled evidence (redacted in public repo), source attributions, refusal/red-team results, human review and failure remediation. None of that is represented as completed here.

## Release decision
**HOLD for production**. A deterministic demo with two known query gaps and no real security integration is demonstration evidence, not a production-grade HR service.
