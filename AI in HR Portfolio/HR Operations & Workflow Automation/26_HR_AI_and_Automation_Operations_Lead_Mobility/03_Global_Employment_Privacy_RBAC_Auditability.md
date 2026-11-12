# 03 — Compliance-aware mobility automation, privacy and agent governance

## Sensitive data lifecycle
| Stage | Risks | Safeguard |
|---|---|---|
| Request intake | Passport/national ID sent through uncontrolled email | Approved portal, minimization and secure redirection |
| Extraction | Model copies IDs/PII into prompt/logs | Redaction, permissioned OCR service and safe sandbox |
| Integration | Broad API tokens / unvalidated webhooks | RBAC, service identities, signature validation, least privilege |
| Storage | Unnecessary copies and indefinite retention | Approved vault, records schedule, lawful basis and deletion pathway |
| Use | AI invents legal entitlement or work authorization | Source-linked guidance, mandatory specialist decisions |
| Audit | Raw documents leaked to BI | Log only opaque case IDs, event categories and control outcome |
| Deletion | Copies retained in queues/backups | Documented deletion/backup retention and incident process |

## Roles
- employee: submit request and view own permitted case status (server-verified identity).
- mobility_ops: perform approved intake, request evidence and propose specialist review.
- senior_mobility: authorized case supervision and permissioned review.
- legal_specialist: signs jurisdiction-specific legal interpretation (not modeled in executable demo).
- payroll_operator: views payroll-approved effective-date events only; cannot decide mobility eligibility.
- admin/technical: maintain credentials and integrations with segregation of duties.

## Maker/checker and human oversight
**Maker:** identifies a routing category, required non-sensitive missing metadata and recommended human queue.
**Checker:** validates role, request scope, idempotency, approved policy version and whether sensitive judgement must go to a human.
**Human:** makes any immigration, work authorization, financial/payroll or contractual decision.

## Threat and negative tests
Prompt injection attempts to bypass approvals; PII accidentally submitted; replayed webhook; dependency timeout; conflicting case status; source-language ambiguity; expired consent; cross-border export to unapproved region; compromised low-code credential; HRIS and payroll disagreement; lack of suitable human reviewer.

## Governance registers
- Decision log with accountable risk owner and versioned policy reference.
- Access review and purpose/retention matrix per jurisdiction.
- Case event traces without employee identity.
- Production readiness checklist covering security, legal, engineering and operations approvals.

**This document is not immigration advice and does not guarantee jurisdiction compliance.**
