# B — AS-IS / TO-BE Process Design, Controls and SOP

## AS-IS (hypothetical, not observed at Azizi)
```mermaid
flowchart TD
 A[Email attachments arrive] --> B[Download and rename files]
 B --> C[Manual spreadsheet tracker]
 C --> D{Documents complete?}
 D -- No --> E[Email customer and wait]
 E --> B
 D -- Yes --> F[Send separate Finance and Delivery emails]
 F --> G[Chase status and reconcile tracker]
 G --> H[Coordinator prepares release request]
 H --> I[Authorized human approves handover]
```

## TO-BE (proposed system design, not deployed)
```mermaid
flowchart TD
 A[Guided handover case intake] --> B[Immutable case ID and safe file references]
 B --> C[Required field and document checks]
 C --> D{Pack complete?}
 D -- No --> E[NEEDS_DOCUMENTS with audit reason]
 E --> F[Notify coordinator to request corrections]
 D -- Yes --> G{Mismatch or duplicate?}
 G -- Yes --> H[HUMAN_REVIEW - Compliance/Coordinator]
 G -- No --> I{Payment cleared and unit ready?}
 I -- No / Unknown --> J[HUMAN_REVIEW - Finance/Project]
 I -- Yes --> K[READY_FOR_HUMAN_APPROVAL]
 H --> L[Human resolves and records evidence]
 J --> L
 K --> M[Authorized human verifies and signs]
 L --> M
 M --> N{Authorized approval granted?}
 N -- No --> O[Return/reject with recorded reason]
 N -- Yes --> P[System issues approved notification]
 P --> Q[Monitor KPIs, exceptions and feedback]
```

## SOP (future controlled publication)
1. **Create:** Coordinator opens case with unique reference. Collect only approved minimum data.
2. **Validate:** Rules engine checks specified fields. Future document extraction may propose fields, never silently overwrite source data.
3. **Classify:** Missing data gets NEEDS_DOCUMENTS; flags/uncertain statuses get HUMAN_REVIEW; fully complete gets READY_FOR_HUMAN_APPROVAL.
4. **Review:** Assigned human verifies source evidence, confirms finance and project readiness, requests corrections and records reason.
5. **Approve:** Authorized person provides explicit digitally recorded decision. A system-ready state is **not** approval.
6. **Notify:** Approved message only after real approval event; customer-facing wording must be reviewed by Customer Care/Legal.
7. **Monitor:** Review exceptions and overdue work daily; log defects and changes; weekly AI Lead incident and value review.

## Example decision ownership / RACI
| Decision/task | Customer Care | Handover | Finance | Project Delivery | IT/AI Lead | Compliance |
|---|---|---|---|---|---|---|
| Completeness checklist | C | **A/R** | I | I | C | C |
| Payment clearance | I | C | **A/R** | I | I | I |
| Project readiness | I | C | I | **A/R** | I | I |
| Workflow rule changes | I | A | C | C | **R** | C |
| Risk, policy and privacy controls | I | C | C | C | R | **A** |
| Final handover release | I | **A/R** (delegated signatory only) | C | C | I | I |

A = accountable, R = responsible, C = consulted, I = informed. The real organization's formal delegation-of-authority matrix always overrides this fictional RACI.

## Risk and control register
| Risk | Impact | Preventive control | Detective/response |
|---|---|---|---|
| AI extraction misreads identity or unit | Wrong case decision | Confidence gating, human source verification | Sample QA, block on mismatch, error trend |
| Sensitive customer data exposure | Privacy and contractual harm | RBAC, minimization, approved retention | Access logs, incident response |
| Automation sends false approval | Legal/customer impact | No system auto-approval; signed event required | Daily authorization reconciliation and rollback |
| Duplicate submission | Conflicting records | Unique case key and duplicate review | Duplicate queue report |
| Aging escalations create overload | Adoption failure | Workload limits, champions support | Weekly queue age, feedback channel |
| Hidden manual work | Inflated ROI | Time-study sampling and finance sign-off | Quarterly benefit realization review |

**Rollback trigger (planned):** unauthorized status communication, privacy issue, unexplained decision discrepancy or elevated critical defects -> pause automated notifications, revert to controlled manual checklist, open incident, obtain reauthorization before restart.
