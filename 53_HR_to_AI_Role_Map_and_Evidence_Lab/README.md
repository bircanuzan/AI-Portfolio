# Project 53 — HR-to-AI Role Map, Evidence-Based Career Fit & Practical Portfolio Lab

**HumanEvoX | Bircan Uzan | 2 November 2026**

> Original project inspired by a LinkedIn post by Shishir B. describing six HR-adjacent AI role families, four Claude skills, a role-fit tool, a 60-day plan, three portfolio case studies, interview preparation and application templates. This is an **independent adaptation, not Shishir B.'s proprietary content or an endorsement/collaboration**. We have not obtained his original Claude skills. Four original Claude-compatible templates are included.

## Why it exists
**Client/employer problem:** HR candidates and leaders have overlapping domain expertise but cannot easily show a credible transition into data, HR technology, AI governance and AI-enabled delivery. Generic upskilling advice often confuses proposed work, executable code and proven client outcomes.

**Approach:** (1) map six adjacent role families; (2) score documented evidence against capability requirements, with explicit gaps and knockout conditions; (3) offer a *voluntary* 60-day 5-hours-per-week practice roadmap; (4) package three original, reproducible offline cases with source data and stated limits; (5) supply interview and professional-profile templates.

**Tools:** Python 3 standard library, CSV, JSON, Markdown, GitHub; four written Claude-compatible SKILL.md instructions (not executed inside Claude). The 20-case policy evaluation is a **deterministic keyword router, not an LLM**.

## Read and run
| Deliverable | Link | Evidence maturity |
|---|---|---|
| Six AI-adjacent HR role maps, skills and fit | [01_Role_Map_and_Entry_Routes.md](01_Role_Map_and_Entry_Routes.md) | Researched-style role taxonomy, not verified live vacancies |
| Role-matcher scoring, eligibility and gap check | [02_Role_Matcher_Methodology.md](02_Role_Matcher_Methodology.md) / [Python CLI](scripts/role_matcher.py) | Heuristic, no employment prediction |
| 60-day, 5-hour/week optional plan | [03_60_Day_Portfolio_Plan.md](03_60_Day_Portfolio_Plan.md) | Planning aid; no course completion claimed |
| Case 1: attrition analysis, 200 employees | [04_Attrition_Analysis_Case.md](04_Attrition_Analysis_Case.md) / [CSV](data/synthetic_200_employees.csv) | Deterministic synthetic data |
| Case 2: AI-screening risk assessment | [05_AI_Screening_Risk_Case.md](05_AI_Screening_Risk_Case.md) / [CSV](data/screening_risk_cases.csv) | Synthetic control/risk register; not vendor audit |
| Case 3: HR policy assistant, 20 questions | [06_HR_Policy_Assistant_Evaluation.md](06_HR_Policy_Assistant_Evaluation.md) / [Evaluation cases](data/hr_policy_20_evaluation_cases.csv) | Local deterministic route-test design |
| Evidence and project limitations | [07_Evidence_Register.md](07_Evidence_Register.md) | Source-of-truth claims register |
| Interview, CV, LinkedIn, case-study templates | [08_Interview_and_Application_Templates.md](08_Interview_and_Application_Templates.md) | Editable originals, not application submission |
| Four Claude-compatible skills | [Skill pack](../.claude/skills/) | Written SKILL.md files, no Claude installation/test claim |

### Offline Python commands
From this folder:

~~~bash
python scripts/role_matcher.py
python scripts/attrition_analysis.py
python scripts/screening_risk_audit.py
python scripts/policy_evaluator.py
~~~

No APIs, dependencies, personal data, paid Claude subscription or cloud account required.

## How this differs from the current portfolio
This is a **cross-project navigator and evidence pack**, not a replacement for existing [Project 03 (people analytics)](../People%20Analytics%20%26%20HR%20Data/03_People_Analytics_AI/), [Project 43 (policy agent prototype)](../43_Microsoft_Copilot_Studio_HR_Service_Agent_Prototype/), [Project 44 (AI governance)](../AI%20Governance%2C%20Risk%20%26%20Responsible%20AI%20Portfolio/44_AI_Ethics_Responsible_AI_and_AI_Governance/), [Project 47 (adoption)](../AI%20Adoption/47_AI_Adoption_Program_Management/), [Project 49 (psychometrics)](../Talent%20Assessment/49_Psychometric_Assessment_and_Talent_Evaluation/) or [Project 52 (dashboards)](../People%20Analytics%20%26%20HR%20Data/52_HR_People_Analytics_Research_Dashboard_Library/).

**No client deployment, attrition prediction, AI bias certification, proprietary Claude skill, actual ATS audit or production HR agent is claimed.** Professionally relevant evidence must be checked role by role against real vacancies before use in a CV or interview.

## Three standalone hands-on projects built from this framework

The original compact case exercises below have been expanded into three complete independent GitHub folders:

1. **[Project 54 — 200-employee attrition analysis](../People%20Analytics%20%26%20HR%20Data/54_Attrition_Analysis_200_Employee_Synthetic_Case/)** — its own synthetic 200-row dataset, Python metrics, tests and departmental dashboard.
2. **[Project 55 — AI recruitment screening risk](../AI-enabled%20Recruitment%20Portfolio/55_AI_Recruitment_Screening_Risk_Assessment/)** — paired synthetic candidate test fixtures, flawed vs controlled mock scorer, risk register and release gate.
3. **[Project 56 — HR policy assistant](../56_HR_Policy_Assistant_20_Question_Evaluation/)** — versioned fictional policies, working local Python router, 20 prompt evaluations, mismatch evidence and human escalation blueprint.

These **extend** the original exercises rather than claiming that a synthetic prototype is a real ATS, deployed cloud model or client success story.
