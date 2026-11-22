# Project Management - AI Evaluation

**HumanEvoX Consultancy | Independent AI model-training & expert-feedback portfolio project**

**Status:** Real, inspectable code and authored synthetic scenarios; **not a client project**. This repository does not claim any real LLM calls, live model improvements, production deployment, AI-model quality scores, freelance earnings or hands-on use of Jira/Asana/Microsoft Project.

## Why this project exists

A fictional enterprise project-delivery team wants to improve an AI assistant's ability to reason about real project-management decisions. The team needs difficult, realistic prompts, independent reference answers, explicit rubrics and repeatable tests for project timelines, resources, costs, risks, stakeholder decisions and Agile/Scrum delivery.

**Role alignment:** Created as an independent demonstration for the [OpenTrain Project Manager — AI Evaluation contract](https://www.opentrain.ai/jobs/project-manager-ai-evaluation--cmwpf3w7n001w07jplttgqphd/), posted 20 November 2026. The listing emphasizes creating and solving PM scenarios, evaluating AI-generated answers, writing clear reasoning and applying PMBOK, Agile, Scrum, scheduling, risk, resource allocation, performance tracking and professional communication. The source listing's requirement for familiarity with Jira, Asana and MS Project is addressed as a **conceptual field map**, not a claim of use or certification.

## The fictional client requirement

An AI product team receives plausible but sometimes wrong project-management guidance. Incorrect critical paths, capacity claims, earned value formulas or bypassed approval gates could lead to expensive decisions. Build a repeatable expert-review framework that:

1. Presents realistic project scenarios and the necessary input data.
2. Computes a defensible **reference answer** separately from any AI response.
3. Tests candidate responses for quantitative correctness, structured fields and governance decisions.
4. Records explicit reviewer explanations, root-cause tags, and remediation advice.
5. Supports future human review of stakeholder clarity, feasibility and PM methodology.

## Six concrete evaluation projects

| Project / scenario | What it tests | Reference method | Common AI failure |
| --- | --- | --- | --- |
| 1. Critical-path project schedule | Dependencies, earliest completion, project sequencing | Forward-pass DAG scheduling | Wrong critical path or unrealistic finish date |
| 2. Earned value project controls | CPI, SPI, EAC, budget/schedule interpretation | EV/AC, EV/PV and BAC/CPI | Incorrect formulas or confusing cost vs schedule performance |
| 3. Resource capacity allocation | Weekly specialist hours, task demand, feasibility | Capacity vs planned work | Overbooking project resources |
| 4. Risk management | Quantified exposure with explicit assumptions | Probability × financial impact (EMV) | Treating full risk impact as expected loss |
| 5. Agile / Scrum sprint planning | Velocity, overcommitment, replanning | Planned points vs past team velocity | Unrealistic sprint commitments |
| 6. Stakeholder change-control | Unapproved scope increase and project governance | Impact assessment, change log, authorized approval | Silent scope/baseline changes |

## Methodology (how AI-model evaluation would be run)

**Step 1 — Define task and scope:** Set client outcomes, project baseline, constraints, PMBOK-style governance expectations, Agile/Scrum conventions and risk acceptance criteria.

**Step 2 — Create benchmark cases:** Use only fictional schedules, costs, resources and change events. Specify inputs, assumptions, expected outputs, severity and failure type.

**Step 3 — Prepare independent references:** Calculate schedule critical path, earned value, risk exposure, resource capacity and sprint workload in Python before reviewing candidates.

**Step 4 — Compare responses:** The included harness scores hand-authored correct and deliberately incorrect JSON answers against computed references. In a real contract, replace fixtures with model responses from a versioned evaluation run and keep the test set fixed.

**Step 5 — Apply human judgement:** Use a six-dimension rubric for methodology, feasibility, risk governance, communication, mathematical accuracy and traceability. Reviewer agreement and severity are proposed controls.

**Step 6 — Explain findings:** Produce concise written feedback describing exact reasoning gaps, affected stakeholders, alternative plans, trade-offs and required escalation.

**Step 7 — Track improvements:** For a future actual LLM, log model/prompt version, baseline vs revised pass rate, regressions, severe issue count and reviewer disagreement. **No such model comparison has been executed in this project.**

## AI skills and domain expertise demonstrated

- **PM domain:** Scoping; business cases; work breakdown structure (WBS); critical path; schedule dependencies; capacity planning; RACI and role clarity; risk registers; change control; project lifecycle; delivery QA; stakeholder reporting; milestones, KPIs and SLAs; earned value / financial performance; Agile, Scrum and Waterfall distinctions.
- **Model training/evaluation:** Expert scenario design; gold/reference answers; structured evaluation rubric; prompt design; error classification; reasoning traceability; quantitative fact checks; feedback and adjudication protocol; human-in-the-loop escalation; testing for unsafe autonomous changes; regression-test design.
- **Communication:** Clear English rationales, business decision notes, concise stakeholder explanations, correction guidance and cross-functional project coordination.

## Technology and tools

| Tool / technology | Usage and evidence |
| --- | --- |
| Python 3 (standard library) | Runnable deterministic PM calculations, input validation and evaluation script |
| JSONL + JSON | Versionable synthetic cases, expected results, candidate responses and output report |
| unittest | Executable tests for critical path, earned value, capacity, risk, Scrum and change governance |
| Excel / Power Query / Power BI | Relevant project reporting and data-validation skill set; **not connected or used by this script** |
| PMBOK principles, Agile, Scrum, Waterfall | Professional domain methods exercised by the scenarios and reviewer rubric; no claim of PMP certification |
| Jira, Asana, Microsoft Project | Conceptual field mapping in [PM_TOOLS_AND_WORKFLOW_MAPPING.md](PM_TOOLS_AND_WORKFLOW_MAPPING.md); **no production integration or prior use asserted** |
| Azure AI / Microsoft Foundry, OpenAI or Anthropic LLM APIs | Possible future model-output sources; **no API integration, model calls or paid tokens used here** |

## Files

- [data/cases.jsonl](data/cases.jsonl) — six synthetic scenarios with independent reference explanation plus authored good/bad JSON responses.
- [evaluate_pm.py](evaluate_pm.py) — compute reference answers and field-level comparison with machine-readable synthetic-fixture report.
- [test_evaluate_pm.py](test_evaluate_pm.py) — independent unit tests with edge cases (including invalid dependency cycle and Boolean/numeric mismatch).
- [RUBRIC_AND_REVIEW_METHOD.md](RUBRIC_AND_REVIEW_METHOD.md) — proposed human evaluation rubric, severity, adjudication and KPIs.
- [PM_TOOLS_AND_WORKFLOW_MAPPING.md](PM_TOOLS_AND_WORKFLOW_MAPPING.md) — project status, dependencies, baseline and resource fields across common PM systems.

## Run locally (Python 3.10+, no account, GPU or external libraries required)

From inside this folder:

    python -m unittest -v test_evaluate_pm.py
    python evaluate_pm.py

The script writes to `results/synthetic_fixture_report.json` (ignored by Git). It reports how many of the **authored fixture answers** match independently computed PM references. These percentages describe the test fixture, **not actual AI model performance**. Review any generated result and exceptions rather than assuming the demo is production-ready.

## Metrics and results

**Measured only after local execution:** fixture unit-test pass count, correctness per reference field, false approval of change control, error detection count and schema compliance.

**Proposed for a real model project, not achieved:** model baseline accuracy, improvement after feedback, inter-reviewer agreement, issue-severity distribution, critical-path calculation error rate, harmful governance-bypass rate, clarification quality, response turnaround and cost per evaluation.

## Business relevance and interview summary

**Client problem:** Project-management advice from AI can sound plausible while using wrong calculations or bypassing governance. **Method:** realistic domain-expert scenarios, computed references, structured QA, explanation-based feedback and human adjudication. **Technology:** Python, JSONL, evaluation rubrics, PMBOK/Agile/Scrum concepts and project data structures. **Output:** inspectable benchmark fixtures and a repeatable offline scorer. **Commercial boundary:** a portfolio exercise, not a claim of client delivery, successful model fine-tuning or realized return on investment.

[Back to AI Portfolio](../README.md) · [AI model training, expert feedback, and model improvement](../AI%20model%20training%2C%20expert%20feedback%2C%20and%20model%20improvement/)