# B — User Acceptance Testing, Defect Governance and Business Sign-Off

## Test strategy
**Scope:** UC-01 intake status, exception ownership and audit requirements in the fictional handover case. Test layers are distinct:

1. **Local executable unit demonstration:** deterministic Python `route_case` on a 12-row synthetic CSV, with unit tests. It does not read PDFs, execute LLMs, send emails or connect to business tools.
2. **Planned system/integration test:** validate authenticated intake, document repositories, Power Automate events, escalation timing and source-of-truth state reconciliation in an approved test tenant. **Not performed**.
3. **Planned business UAT:** signoff by Finance, Handover, Customer Care, Project Delivery, Compliance and IT. **Not performed; no actual business acceptance claimed**.

## Synthetic scenario catalog and expected result
| ID | Input / scenario | Expected system route | Business acceptance condition |
|---|---|---|---|
| UAT-01 | Complete handover pack | READY_FOR_HUMAN_APPROVAL | Does **not** auto-authorize handover |
| UAT-02 | Missing contract | NEEDS_DOCUMENTS | Missing-item reason visible to coordinator |
| UAT-03 | Missing identity proof | NEEDS_DOCUMENTS | Data collection follows privacy rules |
| UAT-04 | Missing payment clearance document | NEEDS_DOCUMENTS | Human follows up for evidence |
| UAT-05 | Payment not cleared | HUMAN_REVIEW | Assigned to Finance, no customer approval sent |
| UAT-06 | Project not ready | HUMAN_REVIEW | Project Delivery must clear |
| UAT-07 | Possible duplicate | HUMAN_REVIEW | Original/reference cross-check required |
| UAT-08 | Identity/contract mismatch | HUMAN_REVIEW | Compliance review, never auto-correct |
| UAT-09 | Empty unit reference | NEEDS_DOCUMENTS | No silent default unit |
| UAT-10 | Empty customer reference | NEEDS_DOCUMENTS | No false customer mapping |
| UAT-11 | Unknown readiness | HUMAN_REVIEW | Unknown is not treated as YES |
| UAT-12 | Another complete pack | READY_FOR_HUMAN_APPROVAL | Human final sign-off still mandatory |

These match the 12 wholly invented records in [`data/synthetic_handover_cases.csv`](data/synthetic_handover_cases.csv). **Code-level result:** 7 local Python unit-test functions passed, including the 12-row scenario suite (14 checks at a minimum, with additional per-row assertions). This is a reproducible local demonstration, **not production or enterprise UAT**.

## Representative defect lifecycle (template; no observed defects implied)
| Severity | Definition | SLA and decision |
|---|---|---|
| Critical | Unauthorized release, privacy breach, misrouted financial authorization | Stop rollout, incident owner assigned immediately; no-go |
| High | Payment or readiness check incorrectly passes, audit evidence missing | Fix and full regression before go-live |
| Medium | Incorrect reminder, confusing rejection message or inaccurate KPI tag | Fix or signed time-bound workaround before next phase |
| Low | Cosmetic or nonblocking labels | Product backlog and owner |

## Traceability
| Requirement | Synthetic evidence | Further system/UAT evidence required |
|---|---|---|
| FR-01/02 | UAT-02/03/04/09/10, Python unit tests | UI validations, document access, accessibility |
| FR-03/05 | UAT-05/06/07/08/11, Python unit tests | Finance, Delivery and Compliance approval workflow |
| FR-04 | UAT-01/12, Python unit tests | Human e-sign and controlled customer message |
| FR-06 | Rule-version field in local response | Persistent timestamped audit event, actor identity, tamper controls |
| FR-07/08/09/10 | **Not locally implemented** | SLA integration, security test, AI extraction evaluation, reporting reconciliation |

## Formal go-live gate (approval template, not signatures)
- [ ] Business owner agrees acceptance scope and all critical tests pass
- [ ] Finance and Project Delivery verify delegated approval rules
- [ ] Compliance/privacy and security complete assessments
- [ ] No critical or high severity defect open
- [ ] Support runbook, rollback and incident reporting rehearsed
- [ ] Champions trained; SOP/version and communications approved
- [ ] Baseline collection approach agreed with Finance
- [ ] Signed UAT evidence and approval recorded

**Sign-off fields:** name, function, delegated authority reference, date/time, environment/version, test evidence link, outstanding risks and explicit GO/NO-GO. In this portfolio case all signatures are intentionally **blank**.
