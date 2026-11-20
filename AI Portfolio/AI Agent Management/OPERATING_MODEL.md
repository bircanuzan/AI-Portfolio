# AI agent management operating model

**Independent design exercise.** The fictional client is a B2B operations team. No affiliation with an employer, maritime operator or paying client is implied. Implemented controls and proposed enterprise capabilities are distinguished below.

## Requirements, methodology and evidence

| Requirement | Method and artifact | Maturity |
|---|---|---|
| Opportunity discovery and prioritisation | Inventory workflows; score value, feasibility, data readiness and adoption readiness from 1–5. Rank by their sum, then review risk separately; mandatory safety constraints can veto a high score. | Proposed management method |
| Document processing and data extraction | Match structured reference in synthetic text; output schema separates data from action. | Local implementation; no OCR |
| Workflow routing, scheduling and checks | Allowlisted routing, appointment proposals and reference-presence checks. | Local implementation; no external writes |
| Lifecycle: prototype, test, monitor, iterate, retire | Define owner/version, intended use, data scope, rollout gate, rollback trigger and retirement record. Track changes against fixtures before release. | Tests implemented; production lifecycle proposed |
| Reliability and exception management | Three-attempt retry cap; review, rejection, quarantine and failure statuses; duplicate guard. | Local implementation |
| Data quality and integration | Require valid identifiers, document text, confidence range and allowed action. For enterprise adapters: validate schema/version, source authority, timestamps and completeness; reconcile against ERP/document IDs. | Local validation; ERP integrations proposed |
| Adoption and training | Operations-led discovery, workflow playbooks, role-based training, champion network and weekly blocker reviews. | Proposed pilot plan |
| KPI analytics and reporting | `evaluate()` computes fixture outcome accuracy, completion/status counts and attempts. | Executed on synthetic fixtures |
| Security, privacy and governance | Reject unknown tools, quarantine known attack patterns, route high/unknown risk to review; hash-linked audit. | Local demo; not comprehensive security |
| Vendor/tool evaluation | Weighted fit, integration, security, evaluation quality, support, portability and total-cost comparison. | Proposed scorecard |
| Reusable patterns and documentation | Reference workers plus policy gate, retry, deduplication and trace pattern. | Runnable reference code |
| Multi-step and sub-agent orchestration | Intake → validation → policy → worker → result → audit. Future supervisor dispatches extraction/routing/review specialists using typed state and bounded loops. | Sequential reference workflow; live multi-agent orchestration proposed |

## Enterprise AI technology plan

The following is a **design backlog**, not evidence of completed platform administration or deployment.

| Technology or capability | Proposed application and acceptance gate |
|---|---|
| Claude Enterprise / Teams | Tenant configuration, role-based provisioning/deprovisioning, workspace boundaries, usage policies and audit review. Verify with an authorized administrator in a test tenant. |
| Cowork desktop workflows and skills | Controlled document workflow, approved skill catalogue, versioned instructions and human review. Validate desktop permissions and data egress before enabling. No custom skill is installed by this project. |
| Custom plugins | Versioned tool schemas, scoped permissions, reviewed provenance and rollback. Test the actual plugin in a sandbox before rollout. |
| Claude Code CLI | Version-controlled coding workflow, reviewed hooks/slash commands, tests and bounded execution. No CLI execution or hook installation is claimed. |
| MCP integrations | Read-only ERP/document lookup first; scoped service identity, explicit schemas, tool-level authorization and timeout/error contracts. No server is implemented here. |
| Cron / scheduling | Schedule an idempotent worker with concurrency lock, retry budget, alerts and explicit timezone; dry-run before activation. No recurring task created. |
| Anthropic/OpenAI APIs, Agent SDK | Proposed interchangeable adapter accepts request IDs and returns schema-validated outputs, usage and latency. Benchmark streaming and batch modes where appropriate. No vendor SDK is installed. |
| Model selection | Compare quality, latency and cost using representative held-out tasks; route by measured capability, with fallback and budget caps. No unverified model prices or model comparisons are asserted. |
| Prompt design | Versioned system instructions, structured outputs, tool definitions, evidence citations and private-reasoning boundaries. Evaluate output correctness and tool traces rather than requesting hidden chain-of-thought. |
| Microsoft 365, Outlook, Teams, SharePoint and browser automation | Least-privilege connectors, approved domains, read/write separation and human approval for consequential actions. No live connection is present. |
| Programming and infrastructure | Python implementation; production plan adds durable event store, versioned configuration, secrets management, CI gates and deployment rollback. |

## KPI definitions and data collection

| KPI | Definition / data required | Current evidence |
|---|---|---|
| Fixture decision/output accuracy | Cases matching both status and expected output ÷ labelled cases | 20/20 in synthetic regression set |
| Completion rate | Completed tasks ÷ total attempts at task level | 7/20; exception-heavy synthetic set |
| Exception mix | Count and rate by review, rejected, quarantined, failed and duplicate | `reports/metrics.json` |
| Retry workload | Sum of simulated worker attempts | 13; no measured network retries |
| Adoption | Weekly active eligible users ÷ eligible users; report by cohort and workflow | Not measured |
| Processing quality | Correct extracted fields ÷ labelled fields, with false positives and omissions | Needs held-out real or representative synthetic documents |
| Throughput and latency | Completed tasks per clock hour; median and p95 end-to-end latency | Not measured; local fixture runtime is not service latency |
| Manual effort saved | Comparable baseline hands-on minutes − assisted hands-on minutes, including review/rework | Not measured |
| Cost per accepted task | Model + infrastructure + review cost ÷ accepted completed tasks | Not measured |
| ROI | (Verified attributable benefit − implementation and operating cost) ÷ total cost | Not measured; no claimed business savings |

For a pilot, collect consented/authorized event IDs, workflow versions, role/cohort, durations, human corrections, quality labels and costs. Minimize content retention and pseudonymize identifiers. Compare equivalent task mixes, include review and rework, and report sample size and uncertainty rather than attributing every change to AI.

## Pilot, ownership and release

1. **Discover:** operations process owner and users select one low-risk workflow; agree baseline and acceptance targets before experimentation.
2. **Sandbox:** Engineering owns adapters, data stewards validate data, security/privacy review permissions, and independent reviewers label held-out cases.
3. **Shadow:** agent proposes outputs without writing; compare human-approved ground truth, quality, time and exception rates.
4. **Limited rollout:** authenticated approvals, persistent audit, rollback switch, support playbook and small champion cohort. A source document can never grant approval or broaden a tool's scope.
5. **Review and scale:** operations accepts demonstrated value, Product reviews fit, Engineering signs off reliability, and security/data governance approve permitted scope. Suspend on unauthorized actions, data leakage or agreed quality violations.
6. **Retire:** revoke credentials, disable schedules, archive versions and evidence under retention rules, and transfer open exceptions to a named human owner.

## Build versus buy

Use a 1–5 evidence-backed score for workflow fit (25%), integration fit (20%), security/governance (25%), evaluation/observability (15%), maintainability/portability (10%) and total-cost transparency (5%). Weights are illustrative assumptions, not procurement findings. Failed mandatory access, privacy or audit criteria veto a recommendation regardless of score. Obtain current vendor documentation, sandbox evidence and full cost estimates before comparing actual products.
