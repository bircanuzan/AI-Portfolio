# Agentic AI Testing & Human-in-the-Loop Governance

**Portfolio track:** Agentic AI assurance, workflow testing, responsible automation, human approval controls and multi-agent QA  
**Project type:** Reusable **reference delivery blueprint** for agent testing, QA and governance roles  
**Evidence status (13 November 2026):** Test approach, control requirements and metric definitions are documented. **No commissioned client deployment or measured production SLA is claimed.**

## 1. Client requirement / problem statement

A business wants AI agents to research, retrieve, call tools, interact with enterprise systems and execute multi-step workflows **without bypassing human authority or losing control of data, costs and decisions**.

Required assurance:
- Test whether an agent completes authorized tasks correctly while obeying role permissions, tool contracts, data boundaries and policy.
- Prevent unsafe writes, irreversible decisions, financial commitments or external communications without the appropriate approval.
- Identify prompt injection, malicious retrieved instructions, tool errors, duplicated execution, runaway loops, broken handoffs and inconsistent state.
- Produce observable evidence of decisions, tool calls, approval checkpoints and incident escalation.
- Establish objective readiness gates before deploying or extending agent capabilities.

**Representative client deliverables:** agent inventory and action taxonomy, risk-tiered decision-rights matrix, workflow/test-case catalog, adversarial scenarios, tool/API contract tests, approval-gate test pack, trace review, failure taxonomy, incident playbook, regression suite, KPI dashboard and go/no-go review.

## 2. Technologies / technical stack

| Layer | Technologies and purpose |
|---|---|
| Agent prototyping / execution | Azure AI Foundry / Microsoft Foundry, LLM-powered workflows, Python, REST APIs, structured tool/function calling |
| Test harness | pytest, Python, JSON Schema validation, mocked APIs, seeded fixtures, scenario and replay testing |
| Orchestration and workflow | State machines, orchestration graphs, queues, retries with idempotency keys, bounded agent loops; agent frameworks optional |
| Observability | Structured logs, timestamps, run IDs, model/version IDs, tool inputs/outputs, trace IDs, token/cost/latency metrics |
| Governance | Human-in-the-loop (HITL) approval gates, role-based access control, least privilege, audit logs, escalation and rollback |
| CI / issue management | Git/GitHub, GitHub Actions (where configured), defect registers, release gating |
| Optional integrations | LangSmith/Langfuse, OpenTelemetry, Azure monitoring, Azure Speech for voice-agent test scenarios, enterprise HRIS/CRM sandboxes; **not asserted as production integrations** |

## 3. Core professional skills

Agentic AI testing; evaluation rubric development; LLM and workflow quality assurance; human-in-the-loop architecture; responsible AI and governance; tool-call and API testing; multi-step task validation; scenario design and red teaming; trace inspection and root-cause analysis; prompt-injection testing; authorization and approval workflow design; Python testing; risk/control mapping; exception management; human–AI workforce design; stakeholder acceptance testing; operational readiness and change adoption.

## 4. Methodology: end-to-end

1. **Map the work:** identify agent users, permitted systems, tool inventories, business objectives, input data, decision rights and irreversible actions.
2. **Classify risks:** label actions as read-only, reversible write, sensitive data handling, regulated or irreversible action; assign severity and required approver.
3. **Specify behavioral contracts:** define preconditions, expected output schemas, tool permissions, workflow state transitions, timeouts, retries, escalation and fallback.
4. **Define HITL control points:** verify who can approve, reject, edit or revoke actions; approvals must bind to the exact action payload and expire or invalidate after material changes.
5. **Build scenario library:** success paths, ambiguous requests, missing permissions, malicious documents, tool outages, duplicate execution, inconsistent records, stale approvals, rate limits and multi-agent handoff failures.
6. **Execute tests:** use seeded/mock tool calls where possible; record decision events and inputs/outputs; replay failures deterministically.
7. **Evaluate:** grade task completion, tool-call validity, groundedness, unauthorized action count, approval adherence, recovery, trace completeness, latency and cost.
8. **Triage and remediate:** link each defect to trace IDs, business impact, reproduction steps, risk level, owner and control failure; retest fixes.
9. **Release gate:** require zero unresolved critical authorization bypasses, complete evidence for sensitive actions, signed business owner acceptance and incident/rollback readiness.
10. **Operate and monitor:** periodic sampling, drift reviews, control effectiveness assessments and change-controlled test updates.

## 5. Example client requirements and acceptance tests

| Requirement | Example test / acceptance condition |
|---|---|
| Strict permissions | Agent refuses tools/actions outside granted role and tenant |
| Human approvals | A write/commit/communication flagged as sensitive cannot execute before explicit authorized approval |
| Approval integrity | Changes to beneficiary, amount, target or payload invalidate earlier approval |
| No duplicate actions | Retries and callback repeats do not create duplicate side effects |
| Prompt-injection resistance | Retrieved web pages/documents cannot override system policy or trigger unauthorized tools |
| Fail-safe recovery | Tool timeout or API error routes to retry limit, safe fallback or human escalation |
| Auditable execution | Every external action maps to actor, authorization, timestamp, tool call, outcome and trace |
| Safe handoff | Multi-agent transfers preserve task state and applicable policy, permissions and approvals |
| Human oversight | Operators can pause, intervene, decline, correct or terminate workflows |
| Privacy and retention | Sensitive data stays within access/retention requirements and appears masked in logs where necessary |

## 6. SLA / KPI / performance scorecard

**Illustrative service objectives only, not historical client outcomes.** Targets must be calibrated to system criticality, business hours, test environment and client contract.

| KPI | Calculation | Draft target | Measured result |
|---|---|---:|---|
| Unauthorized actions | committed unauthorized actions / all agent actions | 0 | Not measured |
| HITL approval bypass | sensitive actions executed without valid approval | 0 | Not measured |
| Sensitive-action audit coverage | fully traced sensitive actions / total sensitive actions | 100% | Not measured |
| High-risk scenario coverage | executed high-risk tests / agreed high-risk test suite | 100% | Not measured |
| Tool-call schema validity | valid structured tool calls / all tool calls | >= 99% | Not measured |
| Workflow task success | successful authorized tasks / total eligible tasks | >= 95% after baseline | Not measured |
| Duplicate side effects | repeated external actions caused by retries | 0 | Not measured |
| Recovery effectiveness | error cases handled by defined retry/fallback/escalation / tested errors | >= 98% | Not measured |
| Severity-1 escalation SLA | confirmed critical fault to owner acknowledgment | <= 1 business hour | Not measured |
| Standard defect triage SLA | confirmed defect to classified incident with owner | <= 1 business day | Not measured |
| Regression gate | passing critical agent test cases / total critical cases | 100% before release | Not measured |

**Additional operating metrics to baseline:** p50/p95 end-to-end latency, average and p95 token cost per workflow, human intervention rate, approval decision turnaround, false escalation rate, successful human override rate, tool availability, context-loss rate, mean time to restore and agent-vs-human task quality.

## 7. Human–AI decision rights: reference policy

| Action class | Agent authority | Human role |
|---|---|---|
| Retrieve/search and draft | May proceed within assigned permissions | Review sampled outputs |
| Recommend or rank options | May propose with evidence and uncertainty | Own consequential decision |
| Edit low-risk draft in sandbox | May edit within versioned workspace | Approve release |
| Change enterprise system of record | No autonomous commit unless explicitly risk-approved | Approve the exact payload and authorize action |
| Make employment, financial, legal or disciplinary decision | Must not autonomously decide | Authorized human decision-maker |
| External irreversible action or disclosure | Block pending consent/approval | Explicit approve/reject with audit trail |

## 8. Deliverables and evidence artifacts

- `README.md` — technical and functional blueprint, skill mapping, controls, methodology and SLAs.
- `metrics/scorecard_template.csv` — reporting template for control effectiveness, quality and response SLAs.
- **Future proof of execution (not yet present):** demo workflow, runnable mock-tool tests, approval-gate negative tests, run traces, signed-off risk matrix and defect-resolution evidence.

## 9. Professional positioning

Relevant to **Agentic AI QA Specialist, AI Agent Evaluator, Responsible AI Specialist, AI Governance Consultant, AI Testing Lead, Human–AI Workflow Architect** and remote full-time/contract roles.

**Confidentiality / evidence note:** This blueprint does not state that a production agent, client-specific control plane or audited SLA has been delivered.  
**Portfolio:** [AI Portfolio](../../) · [Agent tracing and testing](../Agent%20tracing%20and%20testing/) · [Agentic AI development](../Agentic%20AI%20development/).
