# Business-oriented Microsoft 365 Copilot Adoption & Enablement Consultant

**Project 34 | Independent business-side consulting and learning-design portfolio**

## In one sentence
Show how a consultant helps executives, HR, Finance, Sales and operational teams **identify useful Microsoft 365 Copilot workflows, learn them through practical exercises, adopt them safely, and measure whether working practices improve**.

**This is NOT** Microsoft Certified Trainer (MCT) accreditation, a tenant configuration, a real client deployment, or evidence that these workshops were delivered to a customer. It is an original, fully documented learning and change-adoption *design* with synthetic materials. English-language delivery is assumed; no other language proficiency is claimed.

## START HERE — choose an artefact

| Read | What you get | Role requirement |
|---|---|---|
| [01 — Business discovery and use-case prioritisation](01_Business_Discovery_and_Use_Case_Prioritisation.md) | Interview guide, use-case assessment and business pain-point mapping | Stakeholder engagement and business acumen |
| [02 — Facilitator guide and workshop agendas](02_Interactive_Copilot_Workshop_Facilitator_Guide.md) | A timed end-user workshop and champions workshop with practical exercises | Interactive enablement and facilitation |
| [03 — App-by-app prompt and exercise library](03_Outlook_Teams_Word_PowerPoint_Excel_OneDrive_SharePoint_Exercises.md) | Scenario prompts, expected results and checks across all seven requested apps | Microsoft 365 Copilot demonstrations |
| [04 — Executive workshop and value story](04_Executive_Leadership_Workshop_and_Value_Story.md) | A 60-minute C-suite discussion, decision pack and business value hypothesis | Senior stakeholder engagement |
| [05 — Adoption, champions and 30/60/90 plan](05_Adoption_Champions_and_30_60_90_Day_Plan.md) | Roles, communications, behaviour change and adoption interventions | Scale adoption, not just technical training |
| [06 — Licence, readiness, privacy and governance](06_Copilot_Readiness_Licensing_Security_and_Governance.md) | Access caveats, permissions, oversharing checks and responsible AI | Enterprise adoption and technical collaboration |
| [07 — Measurement, KPI definitions and scenario evaluation](07_Adoption_KPIs_Quality_Scorecard_and_Value_Case.md) | Measurement framework, measurable learning and quality gates | Proving behaviour and business impact |
| [08 — Instructional design and competency assessment](08_Learning_Journey_Instructional_Design_and_Assessment.md) | Different audience learning journeys, scenarios, rubrics and follow-up | Learning and development design |
| [Synthetic sample source pack](sample_materials/) | Fictional email, meeting notes, business memo and anonymised spreadsheet data | No client data needed for workshop preparation |
| [Small adoption KPI calculator](src/adoption_report.py) and [tests](tests/test_adoption_report.py) | Transparent offline calculations on synthetic usage data | Analytical and evidence-led advisory |

## What a workshop participant actually does
A learner begins with a real *type* of business problem (represented here by fictional data), uses a safe prompt and the relevant Copilot experience where available, reviews its output against the source, then decides what needs human verification. The learning design focuses on **judgement, adoption and change of behaviour**, not buttons, superficial prompt lists, or unverified promises that AI always saves time.

## Run analytics
Python 3.10+; no Microsoft credentials or external dependencies:

~~~bash
python src/adoption_report.py
python -m unittest discover -s tests -v
~~~

## Compatibility and product truth
Microsoft 365 Copilot experiences, grounding, in-app availability, cross-app access and advanced features **vary by licence, tenant configuration, permissions, product updates and region**. Demos must be checked in the actual client tenant before facilitation. Microsoft published materials explain this distinction:

- Microsoft official adoption guidance: https://learn.microsoft.com/en-us/microsoft-365/copilot/enablement-resources
- Licence and supported experiences: https://support.microsoft.com/en-us/microsoft-365-copilot/what-copilot-license-do-i-have
- Grounding and organisation content: https://support.microsoft.com/en-us/microsoft-365-copilot/how-grounding-works-with-a-work-or-school-account
- Measurement guidance: https://learn.microsoft.com/en-us/copilot/microsoft-365/copilot-control-system/measurement-reporting

## Evidence statement
All names, metrics, business documents, results, delivery plans and workshop schedules are **synthetic portfolio examples**, not verified client activities or personally delivered commercial workshops. There is **no account connection, user telemetry, Microsoft product testing, recording or learner attendance evidence** in this repository.


## New vacancy-aligned companion folder

For recruiter form answers (dedicated Microsoft 365 Copilot years vs. transferable learning/enablement years), a direct mapping to BlackStone eIT-type responsibilities, new HR/Finance/Operations/Executive scenarios, and workshop/measurement designs, see **[Microsoft 365 Copilot Adoption & Enablement](../Microsoft%20365%20Copilot%20Adoption%20%26%20Enablement/)**. This is a companion evidence pack, not a claim of a second delivered commercial project.
