# 03 — Responsible AI risk, policy and incident playbook

## Policy pillars
1. **Purpose limitation:** state legitimate task, users and alternatives.
2. **Data minimisation:** use only data that the institution approved; no copying employee/student records into unapproved consumer AI tools.
3. **Human decision authority:** never delegate high-stakes admission, employment, finance, disciplinary or welfare outcomes to an unapproved autonomous system.
4. **Grounding & verification:** check policy and factual references against trusted sources; log uncertainty.
5. **Transparency:** tell users when outputs are AI-assisted where appropriate; provide human appeal/escalation.
6. **Access & retention:** role-specific permissions, retention rules, audit trace and vendor data-use restrictions.

## Simplified intake risk tiers (illustrative)
| Tier | Use case | Minimum gate |
|---|---|---|
| Low | Drafting a generic internal announcement with no confidential data | Training, acceptable-use guidance, supervisor review |
| Medium | Staff policy knowledge assistant grounded in approved documents | DPO/InfoSec review; access controls; accuracy UAT; named owner |
| High | Advice or recommendations affecting admissions, HR decisions or student wellbeing | Formal impact assessment; Legal/DPO approval; independent evaluation; explicit human decision; likely defer |

Risk tier is an **initial triage**, not a final legal classification; policy owners may escalate at any time.

## Failure and incident sequence
1. **Detect:** staff, champion, helpdesk or telemetry flags unsafe output, disclosure, harmful advice or drift.
2. **Contain:** pause affected workflow, revoke access or disable feature as appropriate; preserve evidence.
3. **Classify:** product owner + InfoSec/DPO assess security, privacy, academic and operational impact.
4. **Escalate:** notify incident owner and applicable institutional stakeholders; counsel determines legal notification duties and timelines.
5. **Remediate:** fix prompts, retrieval documents, permissions, guardrails, vendor settings and/or user instructions; regression test.
6. **Approve restart:** documented go/no-go by accountable authority; update risk and exception registers.

## Illustrative scenario
**Issue:** policy assistant quotes a superseded leave policy to staff. **Action:** suspend the answer route, link current HR policy, review retrieval index freshness, validate corrected answers against test cases, notify affected staff if relevant, restore only after approval.

## Exception record template
ID | Trigger | Affected workflow | Impact/severity | Owner | Containment | Root cause | Corrective test | Approval to restart | Status

**Standards references for design:** NIST AI RMF and applicable privacy/security rules are inputs to policy design; this simulation does not claim ISO certification, formal NIST compliance or legal advice.
