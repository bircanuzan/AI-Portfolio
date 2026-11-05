# 02 — Cross-Functional Governance, RACI, Data Integrity
| Activity | Ops manager | Annotator | QA/adjudicator | Data steward | ML engineer | Privacy owner | Product owner |
|---|---|---|---|---|---|---|---|
| Objectives, SLA, resourcing | A/R | I | C | C | C | C | C |
| Source intake & access | A | I | C | R | I | C | C |
| Annotation | A | R | C | I | I | I | I |
| Quality, disagreements | A | C | R | C | C | C | I |
| Data/model interface | C | I | C | R | A/R | C | C |
| Privacy incident | C | I | C | R | I | A/R | I |
| Release decision | A/R | I | R | C | R | C | C |
| Stakeholder report | A/R | I | C | C | C | C | C |

A=Accountable; R=Responsible; C=Consulted; I=Informed. Final ML deployment requires separate production approval.

## Data governance controls
- **Minimization:** synthetic/de-identified text only. No real resumes, employee records, personal IDs or sensitive source documents.
- **Provenance:** every item has `case_id` and `source_id`; maintain source-system version and legally approved permissions in a real programme.
- **Integrity:** immutable raw intake; schema-validated staged data; independent reviewer fields; append-only adjudication and export version.
- **Access:** role-based least privilege; restricted high-risk queues; no production access is implemented here.
- **Quality drift:** recurring class confusion, coverage changes, annotation behavior and language/domain shifts trigger SME review.
- **Escalation:** severity 1 privacy exposure: stop/contain; severity 2 accuracy failure: HOLD; severity 3 delivery/SLA delay: remediate with ownership and ETA.
- **Retention:** propose a project-specific approved retention/deletion schedule; not assumed or enforced by this demonstrator.
