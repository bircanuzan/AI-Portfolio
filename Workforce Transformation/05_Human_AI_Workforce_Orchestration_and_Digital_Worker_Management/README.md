# 05 — Human–AI Workforce Orchestration & Digital Worker Management

**Case:** Fictional Atlas UAE Shared Services uses multiple narrowly scoped digital worker *candidates* alongside HR service owners and analysts. This module explores **operational coordination and management**, not the single HR-agent competency assessment already in [Project 42](../../42_Human-AI_Workforce_Design_and_Agent_Governance/).

## Principal deliverables
- [Digital worker lifecycle, agent register and access matrix](01_Digital_Worker_Lifecycle_and_Register.md).
- [Human-agent orchestration, monitoring, control and release runbook](02_Orchestration_Runbook_and_Evaluation.md).
- [Synthetic test inputs](data/request_scenarios.json).
- [Runnable deterministic routing/guardrail engine](src/work_router.py) and [unit tests](tests/test_work_router.py).
- A blueprint for later Copilot Studio / Azure AI Foundry / orchestration API experiments, **not an assertion that these services were deployed**.

## Executive question
Who can authorize what a digital worker is allowed to do, how is its output checked, when should it hand back to a human, and how is its performance monitored, suspended or retired?

## Leadership research alignment
- ai_enterprise discussions: agent job descriptions, permissions, probation, performance reviews and enduring human accountability.
- CHRO discussions: override, escalation, audit trail and redesigning managers to supervise human-agent teams.
- sector_organization company-level initiatives: employee-built agent ecosystems and marketplaces; this exercise **does not claim sector_organization participation, access to OpenAI Frontier or production integration**.
- MOHRE context: data integrity and fair, accountable workforce-facing processes.

## Demonstration
From root:

    python "Workforce Transformation/05_Human_AI_Workforce_Orchestration_and_Digital_Worker_Management/src/work_router.py"
    python -m unittest discover -s "Workforce Transformation/05_Human_AI_Workforce_Orchestration_and_Digital_Worker_Management/tests" -v

**Evidence:** Executable local policy **simulation**, not an LLM, agent orchestrator, Microsoft tenant, HRIS integration or tested multi-agent deployment. No real employee, candidate or customer information.

[Portfolio home](../README.md) · [Existing agent evaluation laboratory](../../42_Human-AI_Workforce_Design_and_Agent_Governance/)