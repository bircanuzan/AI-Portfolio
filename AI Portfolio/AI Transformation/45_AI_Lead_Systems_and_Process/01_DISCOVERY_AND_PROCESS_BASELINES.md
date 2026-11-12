# A — Process Analysis & Opportunity Discovery

## Discovery objective
Understand the current **handover document verification and approval workflow** across Sales Administration, Customer Care, Project Delivery, Finance, Compliance and IT for a fictional property development group.

### Proposed discovery workshops
| Workshop | Participants (illustrative) | Key questions | Output |
|---|---|---|---|
| W1 — Intake and customer journey (90m) | Customer Care, Handover Coordinator, Sales Admin | What triggers handover readiness? Which documents are needed? Where are cases lost? | SIPOC and draft AS-IS |
| W2 — Controls and exceptions (90m) | Legal/Compliance, Finance, Project Delivery | Which decisions are irreversible? Who approves exceptions? How are documents retained? | Decision rights, data controls, exception taxonomy |
| W3 — Data and tools (60m) | IT, Data, Workflow Owners | What system is source of truth? Can data be accessed by API? Is document extraction viable? | Integration assumptions, data quality checklist |
| W4 — Redesign and prioritization (90m) | All workstream owners, Director of AI | Which pain points justify automation? What remains human-owned? | TO-BE design, RACI, pilot charter, ranked use cases |

**Workshop artifacts to collect if this were real:** sample redacted submissions, process timestamps, approval policy, exception volumes, queue aging, customer complaints, SOP versions, document retention schedule, API list and security requirements. **None are presented as obtained.**

## SIPOC (illustrative)
| Supplier | Input | Process | Output | Customer |
|---|---|---|---|---|
| Sales Admin | unit/customer reference, contract status | Collect handover packet | Case accepted or deficiencies flagged | Handover Coordinator |
| Customer Care | proof of contact, service request | Validate completeness and communications | Customer action request | Customer |
| Project Delivery | readiness and inspection information | Check readiness | Human decision needed for any disputed/safety item | Project Manager |
| Finance | payment clearance flag | Verify financial clearance | Approved / unresolved clearance exception | Handover & Finance |
| Compliance | document policy and retention requirements | Enforce controls | Logged compliance exceptions | Internal audit |

## AS-IS hypothetical journey
1. Customer sends PDF/images/email to shared mailbox.
2. Coordinator manually renames downloads, enters a tracker and checks each document.
3. Missing fields cause repeated emails; attachments and tracker become unsynchronized.
4. Finance and delivery approvals happen across disconnected messages.
5. Coordinator manually compiles status and customer notification; evidence of decisions is difficult to reconstruct.

### Pain-point hypotheses to validate
| ID | Hypothesized pain | Evidence to request | Suggested intervention |
|---|---|---|---|
| P01 | Incomplete submissions | Missing document count and rework rate | Guided intake + completeness rules |
| P02 | Long approval queues | Timestamped queue aging per approver | SLA reminders and controlled escalation |
| P03 | Duplicate case records | Duplicate unit/reference frequency | Unique ID and duplicate review |
| P04 | Unclear ownership | Sample disputed cases | RACI and explicit human approvals |
| P05 | Low confidence in system status | Manual status reconciliation count | Shared case state and event history |
| P06 | AI hallucination/PII concerns | Risk assessment and access matrix | Extraction confidence gates; no autonomous approval |

## Synthetic baseline (for business-case modelling, not measured)
- Volume: **500** handover packs per month.
- Administrative handling: **22 minutes** average per pack, excluding approver elapsed queue time.
- Rework: **30%** need at least one correction.
- Baseline manual effort = 500 × 22 / 60 = **183.3 hours/month**.
- Proposed target (not evidence): **13 minutes** average handling and **15%** rework.
- Data quality precondition: coverage of all required case fields, consistent document taxonomy, appropriate consent/privacy basis and event timestamps.

### Discovery exit gate
Process owner confirms AS-IS, current policy owner validates approval matrix, IT confirms technical feasibility, data privacy owner signs off pilot data use, and finance validates the *method* for calculating savings. No production procurement or deployment before those signatures.
