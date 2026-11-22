# HR Expert AI Evaluation — Job Skills, Methodology, AI and Tech Stack

Source: [Alpheva HR Expert vacancy](https://www.alpheva.ai/jobs/76042b19-12ff-4bfd-a509-265485861fc1/) (role/domain research November 2026). Distinguish job-relevant skills from specific software not expressly required in the posting.

## Domain skills

| HR expertise | Realistic model output to evaluate | Expert-grade standard |
|---|---|---|
| Talent Acquisition & recruitment | role scoping, structured interviews, applicant assessment, selection advice | job-related evidence, equitable evaluation, human hiring decisions |
| Talent Management | goal setting, performance feedback, internal mobility, development/succession scenarios | supporting evidence, calibrated criteria, human ratings/promotions |
| Human Capital Operations | onboarding, policies, leave, grievances, employee relations, employee lifecycle | versioned applicable source policy, confidentiality, escalating sensitive cases |
| Total Rewards & compensation | salary bands, compensation scenarios, pay equity, grade adjustments | cite band assumptions and authorization; never directly change pay |
| Organization Design & Workforce Planning | role architecture, reporting lines, capacity, skills demand, human–agent work allocation | consistent structures, net capacity net of oversight; no automatic headcount action |
| Employer Branding | candidate communication, careers content and employer claims | source validation, review and publication consent |

## AI evaluation skillset aligned to role

1. **Expert task design:** write realistic prompts from routine and edge-case HR workflows, with precise known constraints.
2. **Reference responses:** produce defensible answers based on provided, versioned policy and grounded facts, not generic advice or made-up local law.
3. **Model output critique:** check factual accuracy, completeness, professional HR judgment, internal consistency, regulatory caveats, fairness and missing evidence.
4. **Rubric authoring / pairwise preferences:** explicit binary checks and severity-weighted scoring with separate critical failure labels.
5. **LLM response quality assurance:** evaluate hallucinations, outdated policy, bias, privacy leakage, policy conflicts and unsupported conclusions.
6. **Agentic workflow assurance:** distinguish advisory responses from write requests; enforce human approval for hiring, pay, grade and employee relations.
7. **Data QA and validation:** compare structured outputs to synthetic truth records; schema validation, regression checks and traceable case IDs.
8. **SME feedback:** concise defect explanation, corrected reference outcome, escalation recommendation and next-test suggestion.
9. **Audit and measurement:** case-level accuracy, critical violation count, policy citation completeness, repeatability and reviewer agreement.

## Technology / AI tools

| Category | Examples | Evidence status |
|---|---|---|
| Model evaluation automation | Python 3, json, pathlib, unittest, GitHub version control | **Used in this project** |
| Synthetic case data | JSON test fixtures, stable test IDs, policy versions | **Used in this project** |
| Scoring approach | Deterministic rule checks, severity tags, test expectations | **Used in this project** |
| AI / LLM testing methods | Golden reference answers, rubric-based evals, LLM-as-judge calibration, red teaming, adversarial cases, groundedness scoring | **Designed; no live model runs in this folder** |
| Practical analytics | Excel, Power Query, Power BI, pandas, SQL (where available) | **Potential implementation tools; not used by this project's Python script** |
| HR technology context | ATS, Oracle HCM, Workday, SAP SuccessFactors, LMS/LXP, people analytics | **Domain systems, not integrated here** |
| Optional AI frameworks | Azure Microsoft Foundry evaluation, LangChain/LangGraph, MLflow, Weights & Biases, LlamaIndex | **Possible future integrations, not part of tested case** |
| Governance | RBAC, versioned HR policy retrieval/RAG, source-aware search, controlled human approval, redacted traces | **Requirements/design, not production services** |

## JD-to-demonstration mapping

**Job focus:** apply senior HR judgment to evaluate advanced AI outputs, identify missing constraints, compare reasonable responses, create ideal answers with explicit criteria and explain consequential errors. **Implemented demonstration:** eight synthetic cases, reference standards, deterministic safety rubric, tests. **Portfolio limitation:** the demonstration does not measure a frontier model and does not constitute professional paid Alpheva work.
