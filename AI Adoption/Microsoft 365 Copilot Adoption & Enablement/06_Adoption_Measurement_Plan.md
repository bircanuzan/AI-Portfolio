# Adoption and business impact measurement plan
**Hypothetical organisation, intended future trial only.** No live usage, learner attendance, tenant telemetry or measured productivity savings.

## Baseline before pilot
1. Approve task definitions for HR correspondence, finance variance notes and meeting follow-up.
2. Select a consenting pilot cohort and comparable tasks.
3. Capture **time to complete**, **reviewer-rated quality**, **error/correction rate**, **confidence** and **current tool usage**, using approved privacy controls.
4. Check licensing/access and readiness with IT. Set exclusions and human-review requirements.
5. Define decision criteria and sample sizes before observing results.

## Metric dictionary
| KPI | Formula / source | Decision use |
|---|---|---|
| Eligible seats | Number of provisioned licensed users in scope | Denominator for readiness |
| Active Copilot use | Active users / enabled users (Microsoft admin report definition) | Adoption trend, not necessarily productivity |
| Weekly retained users | Active in week N and N+1 / active in week N | Habit formation |
| Task time delta | Median comparison-group minutes – median pilot minutes | Efficiency hypothesis |
| Task correctness | Reviewed tasks meeting accuracy rubric / reviewed tasks | Quality gate; must not worsen |
| Learning completion | Participants finishing lab and assessment / enrolled | Enablement coverage |
| Prompt usefulness | Reviewed prompts passing role-specific 10-point rubric / total | Prompt quality |
| Champions coverage | Functions with active coach and documented office hours / target functions | Sustainable peer support |
| Escalations & safety | Counts by incident category and severity | Stop/go control |
| Realised value | Validated baseline minutes saved × volume × loaded cost **where justified** | Business-case estimate, not guaranteed ROI |

## Example **fictional** pilot worksheet (not results)
| Cohort | Enabled seats | Active users | Active rate | Baseline minutes/task | Proposed target | Verified outcome |
|---|---:|---:|---:|---:|---:|---|
| HR | 15 | — | — | To measure | 10% less task time with same quality | Not measured |
| Finance | 10 | — | — | To measure | More accurate and faster first drafts | Not measured |
| Operations | 20 | — | — | To measure | Fewer missed action owners | Not measured |
| Executive Office | 5 | — | — | To measure | Faster briefing with zero unsupported claims | Not measured |

**Causal caution:** Active-user data cannot, by itself, demonstrate a productivity benefit. Observe actual task outcomes with an appropriate comparison design; do not equate generated text volume with business value.

## Survey (pre, immediately after, day 14, day 45)
1. I can explain an appropriate use case in my role (1–5).
2. I can identify confidential information I should not paste into an unapproved tool (1–5).
3. I know how to verify an output against original sources (1–5).
4. I know when to ask a human or report an error (1–5).
5. I used an approved Copilot workflow in the past week (yes/no; optional).
6. Which workflow actually improved, and what evidence do you have? (free text)

## Steering cadence
Weekly champions check-in; fortnightly security/quality review; monthly leadership readout. Continue, modify or stop pilots based on **quality, user needs, risk, cost and measured business value**, not adoption volume alone.

## Microsoft instrumentation
Microsoft 365 admin center reports and Copilot Dashboard may provide usage indicators, subject to entitlements, admin permissions, privacy rules, configuration and available reporting. Do not infer exact report availability for an unnamed customer. See references in 09_Sources_and_Claims.md.
