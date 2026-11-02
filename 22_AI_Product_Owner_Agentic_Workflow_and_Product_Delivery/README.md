## Cross-role enhancement — Creatio AI Consultant / enterprise agent specifications

- [Creatio-oriented discovery, value-mapping and CRM agent implementation specification](../24_Applied_AI_Transformation_Manager_MENA/05_Creatio_Enterprise_Agent_Consulting_and_CRM_Transformation.md), plus its synthetic prioritization script and tests.
- Enhances this product-owner case with customer discovery, executive value narrative, CRM/ERP/API/MCP interface requirements, adoption planning and explicit source/approval boundaries. It remains a fictional, independent exercise with no deployed Creatio solution.

# Project 22 — AI Product Owner | Agentic Workflow Discovery, Prototype & Product Delivery

**Oliver Wyman Digital role-aligned original working prototype.** Not an Oliver Wyman client engagement, live LLM agent platform or production integration. This package focuses on a product owner's personal *build-test-improve* responsibilities, not just documents.

## Product: HR Service Request Copilot (fictional)
Problem: employees submit common requests for HR policy guidance, leave-related questions and personal employment records. The AI assistant may summarize approved public HR FAQs; sensitive requests require human handoff. The product owner designs safe agent/tool boundaries and business acceptance before any live integration.

## View the deliverables
- [Discovery and user journeys](01_User_Discovery_and_Product_Vision.md): interviews to conduct, users, service blueprint, problem/solution framing.
- [Agentic solution and technical blueprint](02_Agentic_Workflow_Architecture.md): agent roles, context, tool call contracts, approvals, no-op/exception paths, API/retrieval design.
- [Prioritized product backlog](03_Product_Backlog_Roadmap_and_Acceptance.md): epics, user stories, INVEST acceptance criteria, sprint and outcome roadmap.
- [Responsible AI, readiness and value](04_Responsible_AI_UAT_Value_Adoption.md): trust, red-team tests, privacy, guardrails, adoption, KPI baselines and support.
- [Working local prototype](src/product_agent.py): personally inspectable deterministic state machine with safe tool selection, no external accounts, no LLM tokens, no real HRIS.
- [Evaluation scenarios](data/scenarios.json), [evaluation runner](src/evaluate.py), and [unit tests](tests/test_product_agent.py).

## Try it yourself
Python 3.10+, standard library only:
1. `python src/product_agent.py`
2. `python src/evaluate.py`
3. `python -m unittest discover -s tests -v`

## Product choices demonstrated
Discovery -> process and exception map -> scoped MVP -> agent/tool design -> working prototype -> scenario-based tests (happy path, ambiguous, unsafe, failed tool, escalation) -> adoption and KPI plan. **Autonomy boundary:** no actions changing employment/pay, leave entitlements or personal data without approved identity and human checks.

## JD alignment
AI Product Owner, agentic solutions, LLM concepts, context/retrieval, tool calling, APIs, Python prototyping, product discovery, service design, human-agent experience, user stories, product backlog, roadmap, UAT, risk/security collaboration, adoption, ROI, cost, AI governance, consultant teamwork.

**Integrity statement:** actual runnable logic is rule-based and intentionally offline. It is a *foundational agentic workflow prototype*, not a deployed LLM, integrated system or evidence of previous Oliver Wyman deliveries.

Job reference: https://gulfhire.com/jobs/ai-product-owner-dubai-gjtlcr
