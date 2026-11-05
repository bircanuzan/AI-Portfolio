# Governance, risk and evidence — UAE HR agent use case

## Six-stage methodology
1. **Discover and bound:** interview HR Ops, HRIS, employee representatives, security and legal; capture SIPOC/BPMN and identify high-consequence services, affected workers and data.
2. **Allocate work:** put personal decisions and personal-data access with authorised humans; use deterministic automation for approvals and routing; use a narrowly grounded agent for general FAQs. Assign named service owner, policy owner, model owner, data owner and approvers.
3. **Assess:** use versioned test set, gold standard, policy citations, multi-turn tests, prompt injection, human-escalation recall, data-exfiltration attempts, calibration and independent adjudication.
4. **Control:** Entra identity and least privilege, approved SharePoint policy library, allowlisted tools, DLP, per-connector permission checks, evidence retention, time-limited tokens, incident playbooks and rollback.
5. **Probation:** sandbox verification, offline test, shadow mode, supervised limited pilot, explicit HOLD / GO / RETIRE gates and weekly incident review.
6. **Monitor:** model/policy regressions, retrieval accuracy, complaints, privacy incidents, human review burden, unit economics, adoption, retirement and re-approval on changes.

## Framework-to-control mapping (design, not certification)
| Reference | Planned operational evidence |
|---|---|
| NIST AI RMF — Govern | Board-approved policy, AI ownership, risk appetite, sign-offs, incident register |
| NIST AI RMF — Map | HR workflow, stakeholder impact, source/data-flow inventory, decision consequences |
| NIST AI RMF — Measure | Test transcripts, benchmark stratification, prompt-injection, citation, access and human-review tests |
| NIST AI RMF — Manage | Blocked releases, corrective-action queue, rollback/kill switch, periodic revalidation |
| Security-by-design | Named identity, connector RBAC, DLP, audit logging, breach handling, retention and access review |
| Human rights / employee safeguards | No automated adverse employment action, human appeal, employee disclosure and bias review |

## RACI
| Decision | HR Ops owner | AI Engineering | Security & Privacy | HR policy owner | Legal | HR case reviewer |
|---|---|---|---|---|---|---|
| Service scope | A | C | C | R | C | I |
| Policy correctness | A | C | C | R | C | R |
| Agent implementation | C | A/R | C | C | I | I |
| Connector access controls | C | R | A | C | C | I |
| Safety/HR benchmark | A | R | C | R | C | R |
| Business go/no-go | A | R | C | C | C | C |
| Personal HR decisions | A | I | C | C | C | R |
| Monthly agent performance | A | R | C | R | C | R |

## Threats and gates
- **Sensitive data / prompt injection:** deny private record access in enforced connector permissions, validate identity and outbound content, red-team; a prompt alone never constitutes a control.
- **Hallucinated, stale or missing policy:** require versioned approved citations, grounded evaluation, independent reviewer and abstention if source insufficient.
- **Unapproved action:** no direct write/send tools for HRIS, payroll, letters or visa status; deterministic approvals and reviewer audit trails.
- **Human overreliance:** service-owner signoff, transparent AI disclosure and human complaint channel.
- **Evaluation bias / coverage:** independent test authors, realistic multi-turn prompts, stratification and holdout set; do not generalise from 28 authored prompts.

## Evidence maturity matrix
| Control or capability | Measured in Project 43? | Evidence gap |
|---|---|---|
| Deterministic routing on test prompts | Yes, 26/28 correct decision+source | Synonym misses T27/T28; no independent review |
| Text citations to sample policy versions | Yes, where matched | Not linked to live SharePoint/version access |
| Human escalation recommendation | Yes, a response field | No live human queue or flow run |
| Human approval recommendation | Yes, a response field | No actual Power Automate/Teams approval |
| No unauthorised HRIS writes | No HRIS connection exists | Enforce and attack-test read-only permissions in tenant |
| Copilot Studio LLM safety and answer quality | **Not tested** | Configure agent; capture model outputs and independent review |
| Authentication, PII handling and compliance | **Not tested** | Access control, DLP, DPIA/legal review and independent penetration assessment |

## Current release decision
**HOLD.** Two false-negative intent matches exist and Microsoft tenant execution, privacy assessment, independent QA and production controls have not been completed. Observed outputs are captured in [Project 43 evidence](../43_Microsoft_Copilot_Studio_HR_Service_Agent_Prototype/evidence/2026-10-29_test_run.json). Earlier [12-row CSV](data/agent_assessment_cases.csv) remains a separate, hand-authored **synthetic scoring exercise** and must not be presented as model test evidence.

References: https://www.nist.gov/itl/ai-risk-management-framework ; https://learn.microsoft.com/en-us/microsoft-copilot-studio/ ; https://learn.microsoft.com/en-us/power-automate/
