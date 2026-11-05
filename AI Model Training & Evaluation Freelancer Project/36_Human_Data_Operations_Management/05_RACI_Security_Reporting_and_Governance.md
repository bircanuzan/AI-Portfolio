# 05 | RACI, data integrity, security and governance

## Fictional operating roles
- **Data Operations Lead:** owns workflows, queue health, source contract and operational reporting.
- **Annotation Lead:** owns taxonomy, worker instruction, task allocation, calibration and rework.
- **Annotators A/B:** independently apply approved guidelines and record evidence.
- **Senior Reviewer:** arbitrates disagreements and documents gold rationale.
- **Data Engineer:** owns secure ingestion, validation automation, data lineage and pipeline support.
- **AI/ML Evaluator:** defines downstream evaluation and dataset fitness for purpose; does not overwrite human gold silently.
- **Security / Privacy:** controls permitted access, retention, redaction and lawful source use.
- **Business Sponsor:** approves targets, data purpose, spend and scale or hold decisions.

## RACI — overview
| Outcome | Accountable | Responsible | Consulted |
|---|---|---|---|
| New data source onboarding | Security + business data owner | Data engineer | Ops lead |
| Task guidance and calibration | Annotation lead | Reviewer + HR SME | ML evaluator |
| Annotator scheduling | Ops lead | Annotation lead | Delivery manager |
| Adjudicated reference labels | Senior reviewer | Senior reviewer | Domain SME |
| Data quality automation | Data engineer | Data engineering | QA lead |
| Dataset release | Data governance owner | Ops lead / reviewer | Security + sponsor |
| Executive KPI reporting | Ops lead | Analyst | Sponsor / Finance |

## Security-by-design
No live employee data in public repositories. Real company data require permitted sourcing, PII/sensitive data handling, jurisdiction-aware access policies, encryption, audit trails, assignment controls, dataset-retention and deletion policy, conflict resolution and model-use licensing.

## Reporting cadence
Daily queue/incident check; weekly annotator calibration and quality review; fortnightly process-improvement meeting; monthly sponsor review of coverage, quality, costs, blockers and risks.

## Issues and escalation
Urgent: exposure of personal data, forbidden source use, broken consent, compromised reviewer access -> stop/restrict ingestion and incident response.
Material: schema drift, incomplete dual labels, low agreement, no gold/unclear rubric -> hold dataset release, clarify instructions and retest.
Operational: backlog or rework above approved capacity -> adjust reviewer allocation with quality safeguards.

**This is a designed operating model, not a live staffed human annotation team.**
