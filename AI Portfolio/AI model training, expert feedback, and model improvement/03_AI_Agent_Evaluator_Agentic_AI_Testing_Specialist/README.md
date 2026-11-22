# AI Agent Evaluator / Agentic AI Testing Specialist

**Project:** Assess a fictional HR-service AI agent before it can access tools, retrieve records or change sensitive employee information.

**Evidence status:** Independent synthetic educational demonstration. No real client, deployed model, trained production system, or commercial result is claimed. **Deliverable:** Runnable synthetic quality/assurance demonstration, not a live model test.

## Fictional business / client requirement

Assess a fictional HR-service AI agent before it can access tools, retrieve records or change sensitive employee information. A team needs an auditable and repeatable decision process rather than untracked subjective opinions.

## Methodology

1. Define permitted versus restricted tools, user roles and approval rules.
2. Create synthetic agent traces with tool calls, outputs and decision points.
3. Detect unauthorized tool use, skipped approvals and missing evidence in the trajectory.
4. Produce pass/fail trace findings and human-review exceptions.

## Skills and technology / AI stack

Python 3, JSONL trace evaluation, authorization design, state machines, tool/function-calling concepts, LangGraph/MCP concepts (reference only), audit logs, human approval gates.

## Evaluation metrics and acceptance evidence

Unauthorized action detection, approval-bypass count, false positives, trace coverage and end-to-end task outcome. These are **metrics to measure**, not results already attained. All authored candidate answers, labels and traces are fixtures; no LLM API generation is claimed.

## Portfolio deliverables

- `audit_agent_traces.py` — runnable synthetic quality/assurance demonstration, not a live model test
- `cases.jsonl` — entirely synthetic scenarios, annotations, traces or evaluation examples
- `README.md` — business requirement, workflow, measurable indicators, and limitations

**Run:** Python 3.10+, from this directory: `python audit_agent_traces.py`. Project 08's full LoRA training requires optional packages and model weights.

## Commercial relevance / interview framing

This project showcases the *methods* used in **AI Agent Evaluator / Agentic AI Testing Specialist** positions. To describe real work accurately, distinguish a portfolio exercise from professional assignments; only claim real-world outcomes when independent evidence exists.

[All 8 role tracks](../) · [AI Portfolio](../../)
