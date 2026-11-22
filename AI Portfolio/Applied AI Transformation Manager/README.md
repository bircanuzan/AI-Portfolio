# Applied AI Transformation Manager | Enterprise Agentic AI Transformation Lab

**HumanEvoX — Independent synthetic engineering and consulting case**

This new folder aligns to [Cognition's Applied AI Transformation Manager — MENA JD](https://jobs.ashbyhq.com/cognition/416528a8-2067-4bec-ac70-73d4ffa52290/). It demonstrates multi-account strategy, a coding-agent rollout programme, human–agent operating model, adoption and consumption analytics, and **net-of-review workforce value economics**.

## Project: Enterprise Engineering Agent Rollout & Value Assurance

**Business problem:** A fictional UAE/KSA group wants an AI software engineering assistant used across thousands of engineers, but lacks a verified baseline, a controlled rollout plan and reliable measurement of net value. Engineer "time saved" is overstated if review, rework, failed attempts, exceptions, oversight, licenses and enablement are ignored.

**Built and tested:** Python 3.11 standard-library model, synthetic CSV data, JSON reporting, regression tests and GitHub Actions. The calculator separately counts baseline time, successful assist human work, failed attempts' original work, human review of all attempts, rework, exception handling and recurring oversight. Negative capacity is supported.

**Governance:** Every modeled account is held for missing real-world evidence/approvals. No automatic deployment, hiring, salary, headcount, procurement or code changes.

## Project contents

- [JD skill and tech/AI matrix](JD_SKILLS_AND_TECH.md) — demanded skills and recommended architecture vs what was actually executed
- [Case study, operating model and rollout](OPERATING_MODEL_AND_ROADMAP.md) — client problem, discovery, AI CoE, roles, decision rights, engineer adoption and executive decision gates
- [Synthetic engineering accounts](data/synthetic_engineering_cohorts.csv) — three fictional cross-border engineering cohorts
- [Python net-value model](src/net_value.py) — baselines, review/rework/exception/oversight, hypothetical cost and release decision
- [Unit tests](tests/test_net_value.py) — regression tests for review burden, negative gains, invalid inputs and human gates
- [Evidence notes](EVIDENCE.md) — what runs vs proposed integrations

## Reproduce

From repository root:

    python "AI Portfolio/Applied AI Transformation Manager/src/net_value.py"
    python -m unittest discover -s "AI Portfolio/Applied AI Transformation Manager/tests" -v

## Integrity

This is an **independent fictional portfolio exercise**, not a Cognition customer project or a production Devin deployment. No live LLM/Devin SDK, client data, external API, enterprise integration or measured ROI is used here. A synthetic FTE-equivalent or dollar proxy is not actual savings or a staffing recommendation.

The JD asks for a CS/EE degree, professional SWE experience and 3–5 years at Big Three strategy consulting firms; this project does not supply those missing professional credentials.

## Prior work retained

The previously created [MENA Applied AI Transformation Manager case](../AI%20Transformation/24_Applied_AI_Transformation_Manager_MENA/) is preserved, with its original files and value-capture calculator. This new separate project adds stronger accounting for real human effort, negative scenarios and stage gates.

**CV-safe claim:** Independently developed and tested a synthetic enterprise AI agent adoption and net-value modelling project, with an AI CoE design, task/ownership architecture and leadership scorecard for engineering transformation.
