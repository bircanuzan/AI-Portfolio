# AI Impact Assessment and Assurance Plan — Completed Synthetic Case

## Recruitment decision-support agent (HR-SELECTION)
**Purpose:** Summarize structured work-sample evidence to assist trained human reviewers.
**Affected people:** Applicants; talent assessment and recruitment personnel.
**Highest-impact misuse:** Autonomous applicant scoring/rejection or unjustified personnel profiling.
**Governance position:** No final automated hiring or other consequential employee decisions.

### Potential harms and controls
| Risk | Proposed control | Verification method | Outstanding work |
|---|---|---|---|
| Harmful bias | Job-related assessment criteria, representation checks, independent fairness evaluation, human review | Suitable group analysis and sample-limited error rates | Actual lawful data and external assessor |
| Hallucinated evidence | Citation to approved original assessment evidence, abstention | Compare model outputs to independently verified case facts | Real-model TEVV |
| Privacy/data leakage | Minimization, purpose limitation, RBAC, retention and vendor assessment | Privacy/DPIA and permission boundary test | DPO approval |
| Unsafe autonomy | No ranking or hiring action tool, authenticated reviewer signoff | Deny high-impact action tests | Production identity and integration |
| Prompt injection | Source trust levels, constrained tools, retrieved-data isolation, attack evaluation | Red-team with realistic adversarial inputs | External model test |
| Explainability | Candidate-facing and recruiter-facing notices, source trail and limitations | Reviewer can reproduce basis for summary | User research and policy signoff |
| Governance/audit | Decision and control records, change tracking, incident/CAPA ownership | Independent document and trace review | Actual log retention |

### Business and model quality measures (not actual results)
Accuracy against reviewed ground truth, selective abstention, false-positive/false-negative impacts, subgroup validity, human override and review burden, access violations, time-to-remediation, model drift, incident frequency and candidate experience. Predeclare sampling, uncertainty and thresholds with subject-matter owners.

### Risk taxonomy
Impact and likelihood scores in the synthetic CSV are ordinal workshop inputs, NOT legal risk tiers, statistically valid probabilities or objective risk predictions. Controls that pass a toy test have *unknown* real-world effectiveness. Residual risk status remains OPEN.

### Assurance decision
HR-SELECTION release is HOLD because privacy approval, model evaluation and fairness review are pending in the fictional register. No candidate data are collected, no real model is tested, and no employment outcome is generated.

### Action register
CAPA-01 DPO privacy/dataflow assessment — OPEN.
CAPA-02 CHRO validated fairness/assessment methodology — OPEN.
CAPA-03 CISO enterprise tool security and red-team — OPEN.
CAPA-04 AI Engineering grounded model evaluation and observability — OPEN.
CAPA-05 Internal Audit independent evidence and release review — OPEN.
