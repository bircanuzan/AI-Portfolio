# 03 - Security, responsible AI and governance

## Governance operating model

- **Architecture review board:** approves reference architecture, supported interfaces and design exceptions.
- **HR process owner:** approves worker events and maintains HR policies and access roles.
- **Finance control owner:** owns cost-center references, accounting treatment, reconciliation and close controls.
- **Group IT / integration owner:** owns technical controls, releases, logging, incident handling and vendor dependencies.
- **Cybersecurity / privacy / legal:** independently review authentication, PII minimization, UAE legal applicability, residency/transfer and retention.
- **Program steering committee:** approves scope, funding assumptions, stage gates and value hypotheses.
- **Human approvers:** must authorize sensitive employee or financial decisions; AI suggestions never directly execute changes.

## Security controls by layer

| Layer | Control | Evidence to request |
|---|---|---|
| HCM | Role-based access, segregation of duties, maker/checker | User/role matrix, change approval logs |
| Integration | Service identities, TLS, secret vault, scoped privileges | Security architecture, penetration review, credential rotation procedure |
| Data | Minimize PII, classify fields, explicit retention | Data inventory, lawful basis assessment and mapping |
| ERP | Finance-owned cost-center and accounting controls | Approved ledger/reconciliation process |
| Reporting | Least privilege and aggregation | Dashboard security tests and access log |
| Operations | Monitoring, replay approval, change control | Alert catalog, incident runbook, evidence register |

## Synthetic risk register

| Risk | Likelihood / impact (illustrative) | Mitigation | Owner |
|---|---|---|---|
| Unauthorized workforce data exposure | M / H | Data minimization, access review, redacted logs | Cyber + HR |
| Wrong finance cost center | M / H | Finance master validation, approval, reconciliation | Finance |
| Duplicate interface event | M / H | Event ID idempotency / replay lock | Integration |
| Late/retroactive worker change | M / M | Effective date policy, review queue | HR + Finance |
| AI hallucinated HR/finance advice | M / H | Retrieval sources, constrained drafts, human decision gate | AI risk owner |
| Unapproved subsidiary exception | M / M | Exception ADR and steering approval | EA |
| Unmeasured value | H / M | Baseline, benefit owner and cadence | PMO |

## Responsible AI extension (optional)

Potential assistant: summarize reconciliation exceptions, draft a remediation note, explain policy steps, identify possible data-quality anomalies. **Do not** approve terminations, promotion/pay decisions, journal entries, payment instructions, employee ratings or privileged user access.

Suggested controls: defined permitted actions; citations to approved policies; out-of-scope refusal; masked data; prompt-injection defenses; audit trail; output verification; AI risk/bias assessment; incident escalation; evaluation set including false-positive and sensitive-action tests.

**Frameworks to assess, not claim certified against:** ISO/IEC 42001 management-system concepts, applicable UAE data protection laws and sector-specific obligations. Legal applicability requires specialist validation; do not infer compliance from this work sample.

## Release evidence checklist

Architecture decision log; requirements traceability; data mapping; DPIA / privacy decision where necessary; role/SoD review; test evidence; rejected-event log; threat assessment; support readiness; training completion; rollback procedure; operational owner sign-offs; measured benefit reporting.
