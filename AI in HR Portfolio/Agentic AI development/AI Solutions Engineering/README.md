# AI Solutions Engineering — Agentic Employee Service Implementation

**Status:** independently designed synthetic portfolio demonstration, not a production deployment. **Vacancy:** an independent AI solutions engineering role brief (https://ae.indeed.com/viewjob?jk=6adfd74623d03c67).

## Problem & outcome
A UAE employee-services operation needs an assistant to answer approved HR policy questions, escalate exceptions and prepare helpdesk requests only after explicit user confirmation. Success is measured by policy answer correctness, safe escalation, UAT pass rate, absence of unauthorized actions, adoption and ticket resolution time. No results are yet measured.

## Demonstrated process
1. Discovery: map users, systems, data and authorization; agree KPIs and constraints.
2. AS-IS/TO-BE: manual HR inbox to approved-answer/exception-handoff workflow.
3. Design: intent routing, knowledge source with policy IDs, tool schemas, human-in-the-loop approval.
4. Configuration: offline Python rules-based agent simulator (not a live LLM) and tests.
5. UAT: functional, exception, privacy, prompt-injection and sign-off tests.
6. Launch: support RACI, rollback, analytics, 30/60/90-day client check-ins.

## JD skill-to-evidence matrix
| Job requirement | Planned/created artifact | Evidence state |
|---|---|---|
| Client discovery, requirements, user stories | REQUIREMENTS_AND_UAT.md | Documented synthetic case |
| Configure agents, prompts and workflows | agent_demo.py | Runnable offline simulator |
| Knowledge, guardrails, escalation | policy source IDs and human-routing rules | Testable locally |
| APIs, OAuth and webhooks | Proposed integration contract | Design only, not connected |
| UAT, onboarding, sign-off | REQUIREMENTS_AND_UAT.md | No client sign-off claimed |
| Post-launch metrics | KPI definition and support plan | No live metrics |

Run: `python agent_demo.py` and `python -m unittest test_agent_demo.py` (Python 3.10+, standard library only). For genuine proof next, configure a sandbox Copilot Studio agent, capture real redacted response logs and execute UAT against the real platform.
