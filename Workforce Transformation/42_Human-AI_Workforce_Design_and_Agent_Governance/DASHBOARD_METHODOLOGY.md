# Human–AI Workforce Intelligence | Executive Dashboard Methods & Outcomes

**Portfolio:** HumanEvoX / Bircan Uzan  
**Industry context:** illustrative UAE professional-services HR operating environment  
**Status:** Original lab prototype and decision frameworks. **Not a commissioned or deployed client solution.**

## 1. Client pain points — hypothetical use case, not a client testimonial

| Business problem | Why it matters | Dashboard response |
|---|---|---|
| HR assistants answer FAQs inconsistently or route sensitive work incorrectly | Employee trust, HR work duplication and compliance exposure | Agent quality, policy-source fidelity, approval-route and release decision |
| Leaders confuse agent usage with value delivery | Unmeasured employee rework and supervision overhead | Editable baseline vs assisted-handling scenario, explicitly non-validated |
| Human and AI ownership are unclear | Errors, unapproved policy actions, missing accountability | Human–AI task allocation, control owners and readiness gates |
| AI-polished applications are mistaken for verified job competence | Unreliable evidence in screening and inconsistent decisions | Evidence-first, human-adjudicated hiring audit checklist |

These are **problem hypotheses**; no client interviews or customer discovery are claimed.

## 2. Evidence and methodology

**Observed source:** [Project 43 — local HR service engine test evidence](../../Agentic%20AI%20development/AI%20in%20HR%20%26%20Agentic%20Automation/43_Microsoft_Copilot_Studio_HR_Service_Agent_Prototype/evidence/2026-10-29_test_run.json), captured 2026-10-29; source includes expected outcome, actual decision, source ID, human flag, external-action flag and a pass/fail adjudication for **28 authored prompts**.

**Actual technology evaluated:** a locally executed, deterministic JavaScript rules engine, *not* a generative AI model, Microsoft Copilot Studio deployment or employee-facing product. No real personal data, employee records or external operations.

**Process:** problem framing → As-Is / To-Be workflow design → task and decision-rights mapping → author a fixed test set → run software → compare actual vs expected decisions and source identifiers → inspect mismatches → articulate acceptance gates → build interactive executive dashboards → make a provisional release decision.

**Observed metrics** (computed from the 28 recorded rows):

| Metric | Exact definition | Observed |
|---|---|---:|
| Full test-pass rate | Cases where both decision and required source expectation passed / all cases | **26/28 = 92.9%** |
| Human-required flag recall | Cases marked human_required among expected APPROVAL_REQUIRED or HUMAN_ESCALATION / all such cases | **17/17 = 100.0%** |
| Correct approval route | APPROVAL_REQUIRED actual among APPROVAL_REQUIRED expected / expected approvals | **2/3 = 66.7%** |
| General answer-route accuracy | ANSWER actual among ANSWER expected / expected general answers | **10/11 = 90.9%** |
| Escalation-route accuracy | HUMAN_ESCALATION actual among HUMAN_ESCALATION expected / expected escalations | **14/14 = 100.0%** |
| Expected source-ID fidelity | Correct observed source identifiers / all cases with expected source identifiers | **10/11 = 90.9%** |
| External actions | Rows with external_action_performed=true | **0/28** |

**Important distinction:** human-required flag recall is not the same as correct approval routing. One case correctly retained a human dependency but failed to select the approval workflow.

**Failure analysis:**
- **T27 — “Can I have my holiday quota?”** Expected ANSWER, observed HUMAN_ESCALATION. This needs **independent review of the expected label**, because personalized entitlements may require HR access. Do not automatically “fix” this by answering personal balance questions.
- **T28 — “Can you arrange proof of employment?”** Expected APPROVAL_REQUIRED, observed HUMAN_ESCALATION. Preserved human oversight, but missed the special approval route.
- **Release: HOLD.** No real tenant, LLM test, enterprise privacy/security review, live authorization, HR owner sign-off, employee UAT, baseline study or independent evaluation.

**Important data caveat:** The separate Project 42 `data/agent_assessment_cases.csv` contains 12 *synthetic* governance exercise rows, not observations from the 28-case executed prototype. It is **not** pooled with the observed dataset.

## 3. Workforce redesign dashboard — mathematical demo, not a result from operations

Users adjust five assumptions: monthly cases; baseline human minutes/case; assisted handling minutes/case; mandatory review minutes/case; and correction/rework minutes/case.

`illustrative_hours_delta = monthly_cases * (baseline_minutes - assisted_minutes - reviewer_minutes - rework_minutes) / 60`

Default demo assumptions: 200 × (12 − 5 − 4 − 2) / 60 = **+3.3 hours/month**; 40.0 hours baseline vs 36.7 hours assisted+review+rework. These are arbitrary scenario assumptions to illustrate why **review and rework must be costed**. Licensing, privacy review, IT, exception severity, adoption and maintenance are absent. Do not convert the number to revenue savings or a hiring plan without measured inputs.

## 4. Evidence-first hiring — control blueprint, no applicant testing

Stages: approved job-related criteria → verifiable candidate evidence → assistive AI mapping → human adjudication → auditable outcomes and appeals. Eight checklist controls are selected manually by the viewer. No hiring decision data, candidate attributes, psychometric tool validation, fairness statistics or improvement claims have been produced.

## 5. Actual tools used vs not used

**Used for this dashboard:** GitHub repository and evidence linking; local JavaScript rules-engine outputs from Project 43; **HTML5, CSS3, inline browser JavaScript**, editable HTML range controls, local audit drill-down; static **SVG dashboards** authored programmatically; Markdown methods/technical documentation; ChatGPT-assisted data interpretation and artifact authoring.

**Existing in linked project, not part of new dashboard execution:** Python script for a separate *synthetic* governance scorecard in Project 42.

**Not used:** Microsoft Power BI / DAX, Microsoft Copilot Studio tenant, Power Automate, live ATS, enterprise HRIS, Azure AI Foundry, live LLM, database, real-world client rollout, verified business outcomes, independent HR/security certification.

**Why this stack:** self-contained, inspectable, offline and reproducible. Data provenance is visible and no private HR record is required.

## 6. Delivered result — what this work actually accomplished

- An interactive, original three-view dashboard covering **observed software-test quality**, **illustrative workforce redesign**, and **proposed evidence-first hiring audit**.
- A visual executive snapshot in three GitHub-renderable SVG files.
- Transparent reconciliation of 28 source test cases and identification of two routing/label-review gaps.
- A governance decision and proposed acceptance gates for further testing.

**Not accomplished or claimed:** reduced cost, improved productivity, improved hiring quality, improved retention, reduced discrimination, implemented AI agent or commissioned client results. These require independent prospective measurement.

## 7. Next-step pilot validation for prospective employers/clients

1. Independently review the test-label definitions and HR policy approval rules; split general policy questions from personal entitlement requests.
2. Run genuine sandbox workflows/LLM outputs with approved, non-sensitive test materials. Retain real prompts, timestamps, outputs, action logs, source versions and reviewer decisions.
3. Test approval routing with signed-off permissions and audit trail; carry out privacy, adversarial, security and accessibility reviews.
4. Measure a real baseline and supervised pilot for response quality, human rework, approval time, fully loaded cost-to-serve and employee experience.
5. Recalculate dashboards using observed data; require policy, security and business-owner approval before rollout.

## 8. Research inspiration and attribution

The dashboards are **original HumanEvoX visualizations**. General questions about AI output rework, evidence-first hiring and human–AI governance were informed by HR research discussions, including [HR & People Analytics Research newsletter](https://www.linkedin.com/newsletters/hr-people-analytics-research-7072692323884638208/). This is not a reproduction of the author's graphics, proprietary indicators or endorsement; our operational definitions and outcomes are explicitly authored and tied to our own lab data.
