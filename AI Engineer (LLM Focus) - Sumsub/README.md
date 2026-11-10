# AI Engineer (LLM Focus) — Multi-Turn Agent Engineering & Evaluation

**Target competency:** LangGraph orchestration, multi-turn LLM-agent architecture, tool execution safety, traceability, Model Context Protocol (MCP), RAG assessment, and compliance-aware AI workflows.

**Portfolio status:** technical reference design and educational prototyping, **not** a customer deployment or a claim of production-shipped agent systems. No Sumsub data, proprietary Summy components, live KYC cases, credentials, or personal information are used.

## Problem
An AI copilot for regulated operations must preserve multi-turn context, call approved tools safely, attribute grounded answers to retrieved evidence, avoid looping, and escalate sensitive cases to human reviewers rather than silently deciding high-risk outcomes.

## Architecture and methods
1. **Stateful orchestration:** LangGraph StateGraph, thread-scoped conversation state, explicit routing/END conditions, bounded step budget.
2. **Tool gateway:** allowlisted, schema-validated, read-only case tools; timeouts, bounded retry/backoff, idempotency policy, explicit degraded-state and human fallback.
3. **MCP and Agent Skills:** versioned, scoped read-only tools with clearly documented inputs, outputs and authorization boundaries; no unsafe external actions.
4. **RAG:** retrieval of permitted documents, document provenance, groundedness checks, abstention on missing evidence, adversarial evaluation sets.
5. **Tracing and evaluation:** structured records of tool calls, error classes, latency and answer quality; offline regression gates, human approval and online A/B comparison once deployed.
6. **Production readiness plan:** Docker image, GCP/AWS, Kubernetes, observable service boundary and Java/Dropwizard integration are *proposed integration targets*, not asserted experience or deployed components.

## Existing repository evidence
- [LangGraph conditional-routing / human-approval prototype](../Agentic%20AI%20Orchestration/01-LangGraph-Human-Approval-Workflow/README.md)
- [MCP read-only tool server prototype](../Agentic%20AI%20Orchestration/02-MCP-Skill-Inventory-Tools/README.md)
- [LangSmith tracing prototype](../Agent%20tracing%20and%20testing/01-LangSmith-Agent-Decision-Traces/README.md)
- [RAG evaluation prototypes](../RAG%20evaluation/README.md)

## Interview and technical explanation
- [Interview questions and concise answers](INTERVIEW_QA.md) — appended as discussed; distinguish built work from planned engineering.
- [Engineering acceptance criteria](DESIGN_AND_ACCEPTANCE.md) — what a production-grade deployment must prove.

## Evidence standard
No invented uptime, LLM accuracy, latency, transaction volume, incident reduction, production stack proficiency, or client outcomes. Prototype behavior must be tested before being described as implemented.
