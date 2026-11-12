# Step 5 — SCALE only after value, reliability and risk controls are proven

## 1. A staged 30/60/90-day *proposal*, not an elapsed project timeline

| When | Work | Artifacts and gate |
|---|---|---|
| Days 1–15 | Baseline HR demand; shortlist/rank use cases; compare FAQ alternative | **G0** real business case and use-case approval |
| Days 16–30 | Readiness scoring, lawful processing, architecture, owners and boundaries | **G1** readiness ≥80/100 + all critical hard gates |
| Days 31–45 | Configure restricted sandbox, approved policy retrieval, human handoff, logging | **G2** identity/security/data/UX design review |
| Days 46–60 | Execute preproduction evaluation with authorized synthetic scenarios; fix defects; start shadow mode | **G3** critical safety test pass; no open critical risks |
| Days 61–75 | Supervised pilot, matched manual controls, real case metrics | **G4** planned value and quality thresholds demonstrated |
| Days 76–90 | More varied users, revised risk register, repeat test and rollback drill, board decision | **G5** evidence-based LIMITED SCALE or HOLD |

The timeboxes are illustrative. Do not compress tests simply to meet calendar deadlines.

## 2. Gates and explicit conditions

### G0 — Prioritize: PROCEED TO DESIGN only if
Real ticket baseline supports demand; candidate score independently reviewed; agentic workflow outperforms simple FAQ/workflow hypothesis; owner, budget, exclusions and scope signed.

### G1 — Readiness: PROCEED TO BUILD only if
Proposed weighted readiness ≥80/100, **no unapproved mandatory blockers**, HR policy owner assigned, lawful data flow confirmed, IAM and pilot user plans feasible.

### G2 — Design assurance: PROCEED TO TEST only if
Tool permissions are enforced outside model, HR policy sources versioned, restricted queue works, monitoring/identity tested, privacy and human escalation approved.

### G3 — Security assurance: PROCEED TO REAL-USER PILOT only if
All critical defined red-team/negative tests pass; no actual unauthorized write or confidential disclosure; stop switch and rollback demonstrated; critical incident process and audit traces confirmed; security/legal/HR approve. A "100% pass" on finite tests never implies zero residual risk.

### G4 — Demonstrated pilot outcome: PROCEED TO NEXT COHORT only if
Compared with the pre-registered manual baseline, the agent shows net time/quality benefit (proposed ≥20% HR effort reduction on eligible cases), correct route ≥95%, source-grounded answer accuracy ≥95%, citation coverage ≥98%, 100% critical escalation on evaluated high-impact set, satisfied pilot users and no unresolved severe failures. Measured full costs must be presented.

### G5 — Controlled scale: PROCEED TO EXPANSION only if
G4 metrics remain stable across **two consecutive independent review windows** (suggested two 2-week cohorts) with sufficient case variety and no safety regression; sponsor approves remaining risk; capacity/support staff are ready; rollback, incident notifications and governance routines function. Increase cohort size gradually. **Do not grant extra HRIS rights just because current read-only agent passes.**

## 3. What "proven" means in this roadmap

**Value:** measured before/after workload, error/reopen trend, employee/HR experience and net operating value; results comparable against simpler alternatives.

**Reliability:** actual outputs evaluated against approved source gold set, including difficult/ambiguous cases, confidence intervals where practical, stable quality across changed inputs/versions, timeouts and recovery.

**Risk controls:** real enforcement traces for denied access, PII, malicious prompts, approval gates, stop switch, vendor/data boundary, logging and escalation; documented residual risks and signed reviews.

If evidence is absent, label **NOT PROVEN**, not "green".

## 4. Expansion sequence and conditions

**Cohort A:** 2–3 policy categories, draft-only plus ticket triage, HR service staff supervised.  
**Cohort B:** extra departments and approved policies, same permissions; recertify taxonomy and sources.  
**Cohort C:** additional sites/employee groups/languages, only after validated translations, access segregation and localized legal review.  
**More autonomy (future):** separate new impact assessment and approval process. No automatic rights expansion.

Monitor after each enlargement. Freeze or roll back on drift, unsafe outputs, increased complaints, sensitive requests misrouted, or control failure.

## 5. RACI (illustrative)

| Activity | HR sponsor | HR service owner | IT/security | Legal/privacy | AI governance | HR reviewers |
|---|---|---|---|---|---|---|
| Select use case and business KPI | A | R | C | C | C | C |
| Approve policy and sources | I | A/R | C | C | C | R |
| Configure tool permissions | I | C | A/R | C | C | I |
| Determine applicable law/data use | I | C | C | A/R | C | I |
| Sign risk controls and evaluation | I | R | R | C | A | C |
| Perform pilot review | C | A/R | C | C | C | R |
| Scale or hold deployment | A | R | C | C | R | C |
| Stop unsafe agent action | I | C | A/R | C | C | I |

R = responsible; A = accountable; C = consulted; I = informed.

## 6. Operating reviews and rollback

Daily pilot: safety queue, approvals, denial anomalies, queue routing and feedback. Weekly: sampled accuracy, costs, throughput and cases reworked. Monthly after wider rollout: cross-functional risk review, policy freshness, incidents, drift, fairness and change backlog. Repeat tests after every material model/prompt/connector/permission change.

**Rollback:** revoke tool tokens, disable publication/entry point, revert to manual HR queue, preserve redacted evidence, notify owners, assess impact, remediate and retest before separately authorizing reinstatement.

Formal decision artifact: [16_Go_No_Go_Decision_Template.md](16_Go_No_Go_Decision_Template.md).