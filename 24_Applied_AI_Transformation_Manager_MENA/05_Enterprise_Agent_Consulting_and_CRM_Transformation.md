# Applied AI Consulting — Enterprise CRM consulting skills extension (November 2026)

**Role benchmark:** a public AI consulting role. This is an **independent synthetic consulting case**, not customer delivery, a live CRM integration, or a deployed agent.

## Client problem / discovery (hypothetical UAE enterprise services team)
CRM queues are overloaded with repeated service inquiries, document questions, customer record-update requests and exceptions. Clients want shorter time-to-answer while maintaining access controls and escalation.

**Discovery workshop sequence:** 1) sponsor objectives and SLA baselines; 2) shadow front-line process; 3) customer/service-data inventory and sensitivity classification; 4) identify high-volume intents and downstream ownership; 5) define ROI hypotheses; 6) prioritize with technical feasibility, risk, adoption readiness and change cost. Required evidence from a real client: task frequency, processing times, quality/complaint data, permissions, ticket examples with consent, CRM/API capabilities.

## AI opportunity map and value hypothesis
The CSV and runnable scoring script illustrate *relative prioritization* using explicitly hypothetical inputs, not actual client ROI. Low-risk FAQs are favored over autonomous changes to sensitive CRM records. Avoid asserting realized savings without a signed measurement baseline.

- Opportunity A: RAG-supported FAQ answers with policy citation, read-only → pilot candidate.
- Opportunity B: Summarize inbound cases with clear source links → sandbox candidate.
- Opportunity C: Draft CRM notes for **human confirmation** → gated pilot candidate.
- Opportunity D: Directly modify personal/customer financial records → **not authorized**.

## To-be architecture and agent specification
Employee/customer → authenticated portal → approved knowledge retrieval → grounded assistant → decision router.
- **Agent A (read only):** clarify, retrieve approved knowledge, cite source/version, refrain from unsupported answers.
- **Agent B (draft only):** propose next action and prepare a CRM case-note preview (no direct write).
- **Human operator:** reviews sensitive exceptions, access and final write authorization.
- **Systems:** CRM, ERP, SaaS integrations via REST APIs, OAuth2 and/or MCP-style tools after enterprise approval; tools use narrow schemas and allowlisted actions.
- **Handoff:** human routing includes case type, source IDs, reason and permitted metadata (no PII in telemetry).

## Implementation-ready specification
| Scenario | Source | Allowed action | Required acceptance |
|---|---|---|---|
| Generic public support FAQs | approved versioned knowledge | read and cite | citation accuracy, uncertainty fallback |
| Case summarization | authenticated authorized CRM data | draft only | no fabricated facts, links to source |
| Change customer address | identity + consent + human approver | human handoff | zero unauthorized writes |
| Sensitive financial request | no general agent access | refuse/escalate | data access and leakage test |

## Roadmap (illustrative)
Weeks 1–2 discovery/data access and risk assessment; 3–4 read-only prototype + 20-case benchmark; 5–6 UAT/pilot with human approvals; 7–8 limited controlled release after security go/no-go; 30/60/90 days value review and monitored expansion.

**Governance:** business owner, policy/content owner, product, engineering, security/privacy, customer-success owner. Explicit sign-off and rollback ownership.

**Measurable outcomes to collect, not invented:** containment of eligible FAQs, human handoffs correctly triggered, grounded citation rate, resolution time baseline vs pilot, agent cost per resolved case, CSAT, p95 latency and unauthorized action incidents.

## Executive value story
"We can start with read-only policy answers and human-approved drafts while proving quality and cost. Permissioned actions are an explicit later gate, not an assumption. The decision is contingent on UAT safety, available CRM integrations and demonstrated value."

## JD requirements mapping
Discovery/value mapping → workshop + opportunity scoring. AI agents and LLM architecture → agent specification and boundary. Process redesign → before/after flow. API/MCP and CRM/ERP → integration contracts as *design*. Executive communication → value narrative. Delivery collaboration → acceptance, RACI and pilot release gates. Adoption/ROI → measured-outcome plan, no claimed results.

## Related portfolio
[Agentic product discovery & prototype](../22_AI_Product_Owner_Agentic_Workflow_and_Product_Delivery/README.md) · [AI Solutions Engineering](../AI%20Solutions%20Engineering/README.md) · [AI Integration Engineering](../AI%20Integration%20Engineering/README.md).
