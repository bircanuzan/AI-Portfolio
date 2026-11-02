# Privacy, DPIA and data-governance annex — fictional SampleCo
**Decision:** privacy counsel's assessment is required before processing identifiable HR or insurance data. **Not legal advice.** No live personal data is included in this project.

## Legal applicability screening (no assumption of automatic jurisdiction)
| Regime | Screening question | Project action |
|---|---|---|
| UAE Federal Decree-Law No. 45 of 2021 (PDPL) | Is the controller/processor and processing in scope, subject to applicable exclusions and implementing requirements? | Map processing, lawful basis, notice, rights, retention and transfers; obtain UAE counsel sign-off |
| DIFC Data Protection Law | Is the entity or processing governed by DIFC legislation? | Assess separately, not treated as identical to Federal PDPL |
| ADGM Data Protection Regulations | Does ADGM jurisdiction apply? | Separate regime screening and counsel review |
| GDPR | Is there an EU establishment/targeted activity/monitoring or other applicable basis? | If in scope document lawful basis, transparency, transfers and DPIA |
| EU AI Act | Does the provider/deployer/system/output satisfy jurisdictional and risk conditions? | Document case-specific applicability; *internal T1-T4 tiers are not EU legal categories* |

## DPIA intake template — AI-001 (sample)
**Data subjects:** applicants. **Data:** CV, employment history, job application and role requirements. **Purpose:** generate suggested shortlist, not automatic rejection. **Special-category traits:** not needed for ranking; avoid inference. Equality testing may need separately authorised protected-group data under strict access controls and legal justification. **Vendor:** hypothetical third-party LLM processor. **Data flow:** recruiter uploads applicant -> secured retrieval context -> model generates evidence-linked recommendation -> human reviews -> ATS stores decision and reason -> deletion under retention schedule.

| Question | Simulated response | Action |
|---|---|---|
| Is processing necessary and proportionate? | Not proven | Compare no-AI baseline and minimisation options |
| Has a valid lawful basis been documented? | No | Counsel to verify before pilot |
| Is applicant privacy notice complete? | No | Explain AI assistance, human decision and contest pathway |
| Are retention and deletion tested? | No | Define ATS- and processor-side schedules, verify deletion |
| Any data transferred outside UAE? | Unknown | Confirm model hosting, subprocessors, contractual safeguards |
| Who handles access/correction/objection requests? | HR Privacy Officer | Publish service procedure and record response times |
| Is model training on customer data disabled? | Unknown | Obtain binding vendor DPA / configuration assurance |
| Are security, access and breach processes proven? | No | Complete threat review and tabletop exercise |

**Outcome:** HIGH privacy uncertainty; STOP live candidate uploads until resolved. This is not a DPIA sign-off.

## Data governance operating model
1. **Data owners:** HR / Claims / IT business owners accountable for permitted purpose.
2. **Data stewards:** manage accuracy, classification, lineage, quality and catalog entries.
3. **Data catalog minimum fields:** asset ID, source, owner, legal basis, sensitivity, lineage, quality checks, retention, region, consumers, model versions, deletion controls.
4. **Quality dimensions:** completeness, accuracy, timeliness, consistency, representativeness, lineage traceability.
5. **Access controls:** least privilege; no secrets or PII in prompts/logs unless approved and protected; separate development/test/production data.
6. **Vendors:** DPA, subcontractor inventory, training restrictions, data residency/transfer analysis, breach timelines, audit rights, change notifications and exit deletion proof.
7. **Security and sovereignty:** decide residency controls from contracts and applicable obligations, not from general claims that 'all AI must stay in the UAE'.

## Sample metadata register
| Asset | Data classification | Steward | Approved purpose | Key quality rule |
|---|---|---|---|---|
| D-HR-001 fictional CV corpus | Personal/restricted | HR Steward | simulated candidate-assist testing only | 100% synthetic; no real identifiers |
| D-CLAIMS-001 fictional claim labels | Restricted | Claims Steward | simulated triage evaluation | verified label provenance required before deployment |
| D-POL-001 HR policy text | Internal | HR Policy Owner | employee FAQ retrieval | version/date and owner on every chunk |

## Approval checkpoints
Privacy (DPO/Legal) -> Data Steward -> Security -> Risk -> independent QA -> Governance Committee; critical privacy defects produce **NO_GO**, uncertain documents produce **HOLD**. Log requester and decisions. Any new data purpose or new vendor requires re-review.
