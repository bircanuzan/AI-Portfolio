# 03 | Business Requirements Document (BRD)
**Use case:** AI-001 Merchant Onboarding Document & Policy Copilot  
**Status:** draft demonstration only. **Not** a real Network International requirement or approved KYC process.

## Purpose and scope
Merchant Operations staff review application documents and internal policies. Fragmented guidance and repetitive document summarization create avoidable delays. The candidate solution produces **cited summaries and checklists for human review**. It **must not** determine KYC eligibility, approve merchants, alter customer records or send external communications without an authorized human.

**In scope:** retrieval from approved, versioned guidance; redacted example documents; draft extraction; auditable staff feedback; source citations; confidence flags; reviewer override.
**Out of scope:** autonomous underwriting, legal conclusions, production access to unmasked personal data, financial advice, automatic decisions, risk scoring.

## Personas and user journeys
- **Operations reviewer:** upload an approved synthetic test package; see checklist, summarized evidence, citation and unresolved questions; accept or correct with reason.
- **Policy owner:** version guidance, approve updates, retire old source documents.
- **Compliance reviewer:** review sample outcomes, exception logs, access controls and evaluation results.
- **Head of AI:** view adoption, precision/coverage, time saved, blocked releases and risk status.

**Happy-path journey:** case assigned → role and policy version checked → approved redacted docs retrieved → LLM extracts suggested fields and cites passages → reviewer confirms/corrects → audit event saved → case proceeds only via existing approved human workflow.
**Exception journey:** conflicting documents → show conflicting citations + 'cannot determine' → route to policy owner; zero automatic action.

## Functional requirements
| ID | Requirement | Priority | Acceptance |
|---|---|---|---|
| FR-01 | Authenticate role and authorize each document retrieval | Must | Access denied for unauthorized role |
| FR-02 | Only retrieve approved, current policy versions | Must | 100% test cases retrieve allowed corpus |
| FR-03 | Generate source-cited draft summaries | Must | Every material claim has traceable document passage |
| FR-04 | Mark missing / conflicting data rather than hallucinate | Must | Unanswerable test set triggers abstention |
| FR-05 | Require named reviewer before progression | Must | No path bypasses approval |
| FR-06 | Log corrections and decision ownership | Must | Audit entry for every accept/override |
| FR-07 | Export reviewer-approved handoff note | Should | Plain text / system-appropriate draft |

## Nonfunctional / compliance requirements
Role-based access, least privilege, data minimization, encryption at rest/in transit, approved residency, PII masking and retention, prompt injection defenses, rate limiting, audit logs, model output monitoring, human kill-switch, tested fallback to manual workflow. Metrics and thresholds must be agreed with InfoSec and Risk; none are deemed approved here.

## Business KPIs / service expectations
Baseline: median handling time, first-time-complete, escalations, reviewer satisfaction.  
Target hypothesis: 20% faster drafting at same quality; >=90% verified cited answers in pilot test set, zero unauthorized access events, 100% high-impact human approvals. Targets are illustrative and subject to validation.

## UAT sample
**UAT-001:** Current policy doc + sample case → cited summary → reviewer can amend.  
**UAT-002:** Missing document → explicit 'missing data' and no approval.  
**UAT-003:** Unauthorized role → denied access, logged.  
**UAT-004:** Contradictory policy versions → escalation to policy owner.  
**UAT-005:** Injection in uploaded text → ignore unauthorized instructions, preserve isolation.  
**UAT-006:** Human rejects summary → correction retained for evaluator, case stays on manual path.

## Traceability
FR → technical design → test case → evidence → accountable signoff. No production release without completed linkage.
