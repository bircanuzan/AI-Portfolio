# Agent pilot and 30/60/90-day value plan

## Completed as of 29 October 2026
- Defined a realistic **UAE professional-services** HR policy use case, process boundaries, RACI and a staged assessment framework.
- Built [working offline JavaScript decision prototype + browser interface](../43_Microsoft_Copilot_Studio_HR_Service_Agent_Prototype/), executed 28 authored prompts and captured actual JSON outcomes.
- Documented the two failed synonym routes and set the release decision to **HOLD**.

## Not completed
Microsoft Copilot Studio setup, SharePoint live grounding, Teams/Power Automate integrations, real LLM responses, remote/public deployment, live permissions, independent security/HR review, employee testing, production KPI baseline or actual business outcome.

## Next 30/60/90 days (plans, not history)
**Days 1–30:** establish ownership, synthetic source-library governance, legal/privacy boundaries, initial Copilot Studio environment and agent; run first true LLM test set.

**Days 31–60:** engineer human-approval and exception flows in Power Automate; verify IAM/DLP, citations, logging, failure modes, latency and cost. Conduct independent HR adjudication and adversarial multi-turn test.

**Days 61–90:** if approved, run a limited supervised pilot; measure safety, correct answers, handoff time, incident rates, human-review effort and employee experience. Accept, hold, narrow or terminate based on objective controls.

## Proposed KPI definitions (not achieved)
- Grounded correctness: validated correct outputs / independently labelled agent responses; initial target >=95% on holdout test.
- Mandatory handoff recall: real high-risk cases routed correctly / all verified high-risk cases; target 100% in release suite.
- Actual human approvals: successfully approved cases / submitted cases; **zero evidence exists today**.
- Citation accuracy, unsupported-answer rate, trace completeness, median latency, rework, incidents, complaints and policy-change regression.
- Fully loaded cost-to-serve: licence, model credits, integration, security review, maintenance, human approval and rework vs baseline; **no savings claims**.

## Skills progression
1. Power Automate: approval and exception routing with real sandbox histories.
2. **Microsoft Copilot Studio:** configure, test and document a working grounded HR agent, not just a planned architecture.
3. Python/JS: enhance evaluation harness and independent holdout data.
4. Azure AI Foundry: enterprise architecture, monitoring, red teaming and CI/CD with engineering partners.

See [Project 43 actual evidence](../43_Microsoft_Copilot_Studio_HR_Service_Agent_Prototype/evidence/2026-10-29_test_run.json) and [Microsoft build checklist](../43_Microsoft_Copilot_Studio_HR_Service_Agent_Prototype/COPILOT_STUDIO_BUILD_GUIDE.md).
