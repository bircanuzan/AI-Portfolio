# 07 | Adoption KPI and output-quality scorecard

## Core measurement: distinguish stages
| Measure | Definition | Data / owner |
|---|---|---|
| Eligible audience | Approved target population with access | IT + business |
| Licensed audience | Licences actually assigned (not automatically active users) | M365 admin |
| Active users | Distinct active Copilot users in a period | Copilot Analytics, where available |
| Adoption % | Active users / licensed users (within matching population/period) | Adoption lead |
| Training coverage % | People with completed enabling exercises / licensed users | L&D |
| Champion coverage | Active champions by department, qualitative reach | Change lead |
| Output correctness | Outputs passing all required scenario checks / reviewed outputs | Human evaluators |
| Repeat task-quality | Correct repeat use after four weeks / reviewed repeats | Functional owner |
| Verified hours released | Independently validated minutes saved net of correction, /60 | Process SME |
| Realized financial impact | Finance-confirmed savings or value after all costs | CFO |
| Business confidence | Survey evidence of practical comfort and trust | User research |

## Binary quality check for any exercise
1. The output meets the business objective and format.
2. Every quantitative/date/claim is traceable to allowed source content.
3. No fabricated action, policy approval, recipient or commitment.
4. Confidential information is not exposed to unauthorized participants.
5. Unknown items are clearly marked for human verification.
6. The final document/email/report is approved by an accountable human when required.

**Passing standard** for low-risk hypothetical scenarios: all six "Yes". Any access breach or invented policy commitment is an automatic fail irrespective of style.

## Business value methodology
Measure the same repeatable task *before and after* with matched cases, including review and correction time. Gross time reduction is not cash savings. Compare benefits to licence, enablement, support, compliance and opportunity costs; seek finance signoff for any realized value statement.

## Synthetic adoption example
The [CSV](data/synthetic_adoption_metrics.csv) contains four weeks of fictional usage for HR, Finance and Operations. The [Python report](src/adoption_report.py) validates basic consistency and calculates licensed-user adoption, training coverage, human-reviewed accuracy and verified time-release hypotheses. It is **not a real Copilot dashboard export or observed result**.

## Avoid false precision
- Usage counts do not prove outcomes.
- A learner's positive feedback is not a controlled productivity study.
- A lower handling time is not necessarily acceptable if accuracy deteriorates.
- Do not compare populations with different licences and permissions as if identical.
- Apply minimum cohort sizes/role-based access to protect employee usage privacy.

## Microsoft reporting
Microsoft documents license/readiness reports and Copilot Analytics dashboards which may include usage, adoption, impact and value views depending on permission/licence. Do not assert a dashboard metric is accessible to a client until validated:
https://learn.microsoft.com/en-us/copilot/microsoft-365/copilot-control-system/measurement-reporting
