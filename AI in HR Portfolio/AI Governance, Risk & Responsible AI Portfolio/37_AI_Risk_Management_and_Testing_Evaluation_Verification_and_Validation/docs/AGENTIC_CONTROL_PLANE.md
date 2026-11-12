# Agentic Control Plane — Concept Architecture (Not Deployed)

## Proposed control plane
```text
Authorised notification / policy source
       |
Source intake (signature / URL / hash / effective-date review)
       |
Human policy / legal validation ---> Source Version Register
       |                                 |
Change-impact detector ---> AI System / Agent Registry
       |                                 |
Test-case generation request ---> Independent TEVV runner
       |                                 |
Risk policy engine (control rules, thresholds and HOLD)
       |
Approval routing: HR owner + Security/Privacy + Legal + Assurance
       |
Approved index/model/prompt release OR rollback / quarantine
       |
Runtime logging -> monitoring -> incident triage -> periodic re-evaluation
```

## Agentic guardrails and technical design handoff
| Concern | Proposed safeguard | Engineering evidence required |
|---|---|---|
| Prompt injection | Separate untrusted tool/source content from system instructions; injection-resistant tool policies | Red-team replay and adversarial test logs |
| Tool misuse / excessive agency | Least-privilege allowlists, scoped identity, human approval for consequential writes | IAM policy tests and denied-action logs |
| Hallucinated policy | Retrieval from approved version with citation + abstain on unsupported answer | Grounding evaluation and exceptions |
| Data leakage | PII minimisation, redaction, encryption, logging controls and restricted retrieval | Privacy review + leakage tests |
| Unsafe outputs | Context-specific refusal/escalation policies; incident route | Unsafe-content test records |
| Source drift | Signed/verified notices, source hash, effective-date review and regression suite | Change tickets, source diff and retest results |
| Model / prompt changes | Version pinning and no silent promotion | Release manifest and rollback test |
| Auditability | Append-only event trail and links to source/test/approval IDs | Event-store trace and retention controls |
| Sovereign or regulated deployments | Residency boundaries, supplier due diligence, approved hosting / data flows | Jurisdiction-specific architecture review |

**Scope boundary:** The Python evaluator in this portfolio simulates a *release gate*. It is not an Agentic Control Plane, prompt injection defence, API integration or production monitoring system.

## Architecture design decisions
- **Fail closed for critical missing evidence**: simulated HOLD is recommended, not automatically imposed on a live system.
- **Separation of duties**: an AI vendor cannot self-certify its outputs in this demonstration.
- **Human appeal / contestation**: any affected person must have a route to challenge AI-assisted conclusions in a real system.
- **Independent re-verification**: model change and policy source change have separate triggers and approvals.
