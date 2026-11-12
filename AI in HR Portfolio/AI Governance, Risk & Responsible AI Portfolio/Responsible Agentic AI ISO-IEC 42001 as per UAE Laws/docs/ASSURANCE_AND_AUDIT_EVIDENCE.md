# Assurance file: what an auditor could and could not verify
**Audit framing:** portfolio exercise, not an actual company audit or regulator finding.

| Evidence ID | Requirement/theme | Artifact and scope | Status | Gap before credible live AIMS evidence |
|---|---|---|---|---|
| EV-01 | AI asset inventory | Hypothetical recruiting policy/message agent in README | DRAFT | System inventory, model/vendor/version, real data flow |
| EV-02 | Risk evaluation and treatment | data/risk_register.csv with 10 original risks | SYNTHETIC | Risk owners accept residual risks; dates and actions |
| EV-03 | Policy and roles | docs/GOVERNANCE_POLICY_AND_CONTROLS.md | DRAFT | Company adoption, executive approval, role assignments |
| EV-04 | Applicable legal obligations | docs/UAE_LEGAL_APPLICABILITY.md | RESEARCH | Legal opinion tied to actual entity and data processing |
| EV-05 | Authorization control testing | 12 locally executed synthetic test scenarios | **EXECUTED LOCAL DEMO** | Integrated, actual tool calls under secured infrastructure |
| EV-06 | Regression testing | 9 locally executed Python unit tests | **EXECUTED LOCAL DEMO** | CI run, environment provenance and negative testing |
| EV-07 | Data privacy/retention | Control spec, no real candidate data | DESIGNED | DPIA/processing register, transfer/supplier contracts |
| EV-08 | Internal audit | Proposed checklist below | NOT PERFORMED | Independent audit plan, samples, dated audit findings |
| EV-09 | Management review | Proposed agenda below | NOT PERFORMED | Signed meeting minutes and actions |
| EV-10 | Corrective actions | Proposed CAPA log below | NOT PERFORMED | Real defects, root cause and verification |

## Example internal-audit interview questions
- What exactly is inside/outside the AIMS boundary? Is it approved?
- Is there an accountable human for every consequential decision?
- Has the legal/privacy owner confirmed whether PDPL, DIFC or ADGM rules apply?
- Which tool permissions and processing purposes are authorized? Can the agent bypass them?
- Are real model prompts, outputs, evaluations and version changes captured under privacy-preserving retention?
- Are incidents, complaints, supplier changes and corrective actions reviewed?
- How are fairness risks measured and how is human override audited?
- Does a management review close the PDCA loop?

## Blank corrective-action register
| Finding ID | Detection date | Severity | Owner | Root cause | Fix | Re-test evidence | Closure sign-off |
|---|---|---|---|---|---|---|---|
| TBD | — | — | — | — | — | — | — |

## Sample management review (agenda, not minutes)
AIMS scope changes; strategic objectives; risk appetite and risk treatment; security/privacy/ethics issues; evaluation and drift; complaints and incidents; vendor risk; audit findings; resources; approved release decisions; action owners and deadlines.

**Interpretation:** matching all 12 expected results means the *author's synthetic decision rules* behaved as specified. It does not prove those rules are legally sufficient, fair to real candidates, resistant to all attacks or compatible with ISO certification.
