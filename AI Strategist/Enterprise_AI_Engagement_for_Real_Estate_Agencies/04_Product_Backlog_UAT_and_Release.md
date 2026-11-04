# 04 | AI Product Owner Backlog, Engineering Estimates and UAT

## Two-engineer delivery plan
| Priority | User story / acceptance criteria | Owner | Indicative effort |
| --- | --- | --- | --- |
| P0 | As a CRM owner, I ingest leads idempotently and preserve agency boundaries | Engineer A | 3–5 days |
| P0 | As compliance, I suppress all contact drafts when consent is false | Engineer B | 1–2 days |
| P0 | As an agent, I see verified listing facts with source/last-updated | Engineer B | 4–6 days |
| P0 | As an agent, I can approve, edit or reject suggested messages | Engineer B | 4–6 days |
| P0 | As analytics, I can reconstruct assignment and response events | Engineer A | 3–5 days |
| P1 | As a director, I can review cohort-level funnel trends | Engineer A + Analytics | 3–5 days |
| P1 | As operations, I can fall back to manual routing on incident | Both | 2–3 days |
| P2 | As Product, I can compare reusable agency configurations | Both | 2–4 days |

Effort figures are challenge prompts for estimation; not engineering commitments. Dependencies: API access, event quality, approved listing source, client training and privacy approval.

## UAT scenarios
| ID | Input | Expected result |
| --- | --- | --- |
| UAT-01 | Consent absent/false | No outbound draft, no send |
| UAT-02 | Lead duplicated by webhook retry | One canonical lead and one audit trail |
| UAT-03 | Listing missing price | Abstain on price claim; request human confirmation |
| UAT-04 | Customer text injects system instructions | Injection ignored, escalation logged |
| UAT-05 | Unsupported language | Human fallback and explicit notification |
| UAT-06 | Cross-agency listing identifier | Access denied; security alert |
| UAT-07 | Agent rejects draft | No CRM outbound update |
| UAT-08 | Connector outage | Queue visible, manual workflow usable |
| UAT-09 | Missing response timestamp | Missing-data count, not zero SLA |
| UAT-10 | Agent approves factual draft | Approval audit ID and approved message persisted |

## Release gates
Dev -> masked-data integration test -> security/privacy approval -> agent UAT -> limited cohort -> guarded scale. Release checklist: rollback switch tested, contact permissions validated, factuality/consent pass rate recorded, on-call and manual fallback defined.

## Definition of done
No work item closes solely because the model generated text. It closes when measurable workflow outcomes, logging, consent protections, adoption training and sponsor acceptance are complete.
