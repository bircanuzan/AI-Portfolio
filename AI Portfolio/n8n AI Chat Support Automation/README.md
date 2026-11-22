# n8n AI Chat Support Automation

**Portfolio status:** Proposed reference architecture / demonstration based on a freelance job description. Not an implemented client deployment.

## Business requirement
Design an n8n-based multi-agent AI customer-support solution integrating Claude and Gemini, SQL interaction logs, confidence scoring and human escalation. Route inbound questions to the right specialist, use knowledge-based answers, avoid hallucinated promises, and log every handoff.

## What I do / my responsibilities
1. Gather support requirements, classify ticket intents and define customer-service KPIs and escalation policy.
2. Map conversation journey: channel intake -> intent classification -> knowledge retrieval -> response drafting -> risk/confidence check -> approve/send or escalate.
3. Design n8n workflows with triggers, conditional branches, reusable sub-workflows, retry paths and webhooks.
4. Specify specialist agents: triage/routing, knowledge lookup, response drafting, policy/QA review and escalation coordination.
5. Integrate Claude and Gemini through approved API credentials; compare output quality, latency and spend.
6. Create SQL schemas for conversations, message events, agent decisions, confidence signals and escalation queues.
7. Define structured output schemas, source citations and confidence indicators. Low confidence is escalated, not treated as guaranteed probabilistic accuracy.
8. Design human-in-the-loop approvals for refunds, account changes, privacy-sensitive inquiries and unsupported claims.
9. Test multi-turn scenarios, prompt injection, ambiguous inquiries, missing knowledge, language switches and system failures.
10. Define operational dashboards for resolution time, agent containment, response quality, escalation rate, API costs and customer satisfaction.

## Skills demonstrated / developed
- Agentic AI architecture and multi-agent orchestration
- n8n visual workflow design and API integration
- Customer-support process design and service operations
- LLM prompt engineering and tool/API calling
- Claude and Gemini integration and comparative evaluation
- Retrieval-augmented generation (RAG) and knowledge grounding
- SQL database modeling and event logging
- Classification, confidence calibration and evaluation rubrics
- Human-in-the-loop escalation, responsible AI and privacy controls
- API testing, observability, analytics and cost optimization

## Technology and AI tools
| Layer | Tools | Purpose |
|---|---|---|
| Orchestration | n8n, Webhook, HTTP Request, Switch, IF, Execute Workflow | Triggers, routing, tool calls and reusable pipelines |
| LLMs | Anthropic Claude API; Google Gemini API | Intent interpretation, grounded drafting and QA comparison |
| Retrieval | Embeddings, pgvector / vector database, source documents | Retrieve authorized support policies and FAQ answers |
| Storage | PostgreSQL / MySQL, SQL | Conversation and decision logs, handoffs and events |
| Service integration | REST APIs, JSON, Postman | Connect ticketing, CRM and support channels |
| Optional app | FastAPI, Python, pandas | Middleware, evaluation and offline analytics |
| Evaluation | Test datasets, rubric graders, pytest / Postman | Quality, safety, multi-turn and regression checks |
| Monitoring | n8n execution logs, Power BI, Grafana (optional) | SLA, response cost, agent failures and escalation trends |
| Security | OAuth / API keys, secret storage, least privilege, PII masking | Protect customer data and govern automations |

**Technology is proposed, not verified as installed or deployed by this README.**

## Multi-agent architecture
```text
Incoming chat / webhook
        |
     Triage agent
        |
  Knowledge retrieval -- authoritative policy sources
        |
   Drafting agent (Claude or Gemini)
        |
  QA/policy validation agent
        |
   +---- safe, grounded ----> send response + SQL audit
   |
   +---- uncertain/sensitive -> human approval / ticket queue
                                    |
                               SQL audit + follow-up
```

## Methodology
1. **Discover:** map intents, channels, volume, current resolution times and high-risk actions.
2. **Design:** define schemas, routing rules, retrieval boundaries and support escalation.
3. **Prototype:** build a sandbox n8n flow with synthetic tickets and mock endpoints.
4. **Evaluate:** score groundedness, correctness, policy compliance, escalation accuracy and costs.
5. **Pilot:** conduct shadow-mode review before permissioned customer-facing operation.
6. **Operate:** version prompts, monitor failed executions, manage incidents and track KPI trends.

## Evaluation scenarios
- Normal FAQ answered from approved source
- No relevant knowledge document: escalate instead of inventing answer
- Refund/account change: require human approval
- Prompt injection inside retrieved documentation: reject override instructions
- Duplicate webhook delivery: avoid duplicate responses/tickets
- Anthropic/Gemini timeout or rate limit: retries and safe fallback
- Multi-turn request requiring preserved context and masked personal information

## KPIs (hypothetical targets, not achieved)
| KPI | Measurement | Example pilot target |
|---|---|---|
| Grounded response quality | reviewer-approved answers / evaluated answers | >=95% |
| Escalation recall on risky cases | correctly escalated risky cases / all risky cases | >=99% |
| First response latency | p50/p95 response seconds | establish baseline, then improve |
| AI containment | resolved without human agent / eligible cases | >=40%, conditioned on quality |
| Audit completeness | logged decisions / total decisions | 100% |
| Cost per resolved conversation | total model/tool spend / resolved conversations | compare Claude vs Gemini |
| Customer satisfaction | positive survey responses / surveyed conversations | track against existing baseline |

## Deliverables
- n8n workflow diagram and node configuration specification
- Multi-agent roles and structured input/output schemas
- SQL schema, logging and retention specification
- Claude/Gemini integration and fallback design
- Escalation/approval matrix, test cases, KPI dashboard specification
- Security and production-readiness checklist

## Evidence and limitations
This is a portfolio design intended to explain the responsibilities, skills and tools applicable to the freelance brief. No client affiliation, live support system, measured gains or production readiness is implied.
