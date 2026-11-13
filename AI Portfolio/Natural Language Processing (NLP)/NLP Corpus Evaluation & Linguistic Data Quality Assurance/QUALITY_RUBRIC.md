# Linguistic Corpus Evaluation — QA Rubric and Acceptance Plan

| Control | Automated / manual | Severity | Proposed acceptance threshold (not measured SLA) |
|---|---|---|---|
| Required metadata and schema | Automated | Blocker | 100% required fields populated; approved values validated |
| UTF-8 / replacement characters | Automated | Blocker | 0 corrupt/control-character records |
| Exact/normalized duplicates | Automated | Review | <=1% unless reuse explicitly justified |
| Personal/contact information | Automated flag, manual confirmation | Review | 100% flagged records reviewed; zero confirmed unauthorized PII |
| Named entity spans/types | Automated offsets, manual semantic labels | Blocker/Review | 0 invalid spans; >=95% gold-set entity F1 target |
| Tokenization and normalization | Automated checks plus human inspection | Review | 100% approved normalization specification adherence |
| Grammatical and semantic correctness | Human linguists, adjudicated samples | Review | >=95% sample acceptance target |
| Annotations and label taxonomy | Two-rater audit plus adjudication | Review | Cohen kappa >=0.80 target where meaningful |
| Language/domain/register distribution | Automated proportions vs approved population | Review | Per-slice variance within documented tolerance |
| Demographic / dialect representativeness | Human governance audit | Review | No unapproved excluded subgroup; assess against valid base rates |
| Contamination, leakage, train/test overlap | Data lineage and independent matching | Blocker | 0 confirmed cross-split leakage |
| Reporting and correction tracking | Automated report + human signoff | Governance | 100% blocker remediation and signoff before dataset promotion |

## Workflow and stakeholders
Data steward approves sources/usage; computational linguist maintains taxonomy; two annotators label a stratified sample; adjudicator resolves disagreements; QA lead signs off remediation; data scientist approves downstream modeling suitability; governance reviewer checks privacy/fairness.

## KPI definitions
- **QA clean record rate:** number of records with zero audit flags divided by all inspected records.
- **Blocker rate:** distinct record IDs with blocker flags divided by all inspected records.
- **Agreement rate:** matching rater pairs divided by valid rater pairs.
- **Cohen's kappa:** observed agreement adjusted for chance agreement on nominal labels.
- **Representation:** observed share by language, domain, dialect/register or cohort versus an approved reference population (not a raw balance claim).
- **Sample defect prevalence:** defects found by independent adjudicators divided by sampled records; include confidence interval for statistically designed random audits.
- **SLA candidates:** critical defect triage within 1 business day; corrective-action closure within 5 business days; >=99% pipeline execution success; 100% version/approval traceability. All illustrative targets.

## Limitations
The current code only validates record structure, normalized duplicate strings, Unicode replacement/control characters, simple email/phone patterns, entity offsets and rater consistency. It does **not** certify grammar, nuanced meaning, dialect fairness, demographic balance, contamination or gold-standard NER/POS/dependency correctness. The sampling routine is quota-based and deterministic, not a probability sample; do not infer confidence intervals or representativeness from it. Data are entirely synthetic and not client data.

## Job alignment
The closed Agile 4UX JD called for large-corpus evaluation, multilingual linguistic checks, annotation QA, data cleaning, bias detection, inter-annotator agreement, Python NLP tools, dashboards, reporting and cross-functional review. The runnable subset above establishes an honest foundation; an enterprise implementation would add corpus-scale processing, linguistic NLP libraries, dashboard integrations, versioning and independently verified annotation workflows.
