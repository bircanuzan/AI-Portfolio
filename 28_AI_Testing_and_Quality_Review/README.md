## NEW — Kraken AI Growth Ops (remote UAE) JD extension — 2 November 2026

**[Open role-specific operational QA case and requirements map](05_Kraken_AI_Growth_Ops_JD_Alignment.md).** This extends the same AI Testing & Quality Review project, rather than creating a redundant folder.

- **New practical artifacts:** `qa_demo/agent_events_synthetic.json`, `qa_demo/agent_ops_eval.py`, and `qa_demo/test_agent_ops_eval.py`.
- **Skills mapped to vacancy:** platform release/regression checks, agent output review, unauthorized-action approval gates, exception routing, queue and defect triage, severity-based escalation, bug reproduction, QA runbooks, release readiness and monitoring KPIs.
- **Evidence status:** all events are fictional; rule-based Python checks are not proof of live Kraken product tests, Mixpanel use, Jira use, or real LLM evaluations.

Run locally: `python -m unittest qa_demo.test_agent_ops_eval -v` and `python qa_demo/agent_ops_eval.py qa_demo/agent_events_synthetic.json`.

---

## New JD extension — software_group QA Engineer (Dubai remote, 2 November 2026)

- [JD skills mapping, test plan, requirements traceability, defect template and release gates](04_software_group_QA_Engineer_JD_Skills_Test_Plan_and_Defects.md)
- [Local HTTP API QA lab](qa_demo/README.md): Python HTTP service, automated functional/negative/integration/regression tests, Postman collection, optional Playwright browser smoke and [GitHub Actions CI](../.github/workflows/qa-demo-ci.yml).
- **Skills/tech from JD:** requirements-to-test coverage, manual QA documentation, Python test automation, REST/JSON and Postman, CI/CD, browser automation example, Jira-style defect and Agile triage, UAT and security boundary negative tests.
- **Evidence honesty:** the executable application and tests are synthetic local demonstrations; no software_group software was tested. Optional Playwright/CI results are not asserted until runs are verified.

# AI Testing & Quality Review

**HumanEvoX — original portfolio demonstration (fictional case study).**

Business-user testing of AI outputs against approved source material, evidence logging and human escalation.

## Purpose
Demonstrate concrete deliverables for prospective AI/HR transformation and learning-design roles or scoped consultancy projects. All people, companies, test outputs and operational examples are synthetic or illustrative. No claim is made that a live client implementation, AI product test or training delivery occurred.

## Included artifacts
- [01_Test_Plan_and_Evaluation_Rubric.md](01_Test_Plan_and_Evaluation_Rubric.md)
- [02_Sample_Test_Cases.csv](02_Sample_Test_Cases.csv)
- [03_Defect_and_ReTest_Template.md](03_Defect_and_ReTest_Template.md)

## Scope and delivery boundary
Documentation, business-user review, analysis or instructional design as described in each file. The original documentation-only artifacts are unchanged. A new local synthetic HTTP QA lab now demonstrates test code and API behavior; no production system, model change, production security assurance or actual training delivery is claimed. Any live work requires client source materials, defined scope, decision owners and approvals.

## Suggested portfolio presentation
Explain the scenario, show the artifacts, identify assumptions, and describe how the materials would be validated with a real client.
