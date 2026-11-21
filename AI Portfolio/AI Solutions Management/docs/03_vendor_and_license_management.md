# 03 — Vendor Selection, Contracts, Licensing & Cost Control

## Lifecycle and decision rights
**Source and evaluate → diligence → commercial comparison → negotiate with Procurement → approve → contract → onboard → monitor → renew/retire.** The AI Solutions Manager coordinates product requirements and vendor performance; Procurement owns contracting and commercial approvals, Legal owns contract terms and IT/DPO own their controls.

## Weighted vendor scorecard
| Dimension | Weight | Typical evidence |
|---|---:|---|
| Business fit / functional requirements | 25% | POC outcomes, user stories, acceptance tests |
| Security assurance | 25% | Audit artefacts, IAM, encryption, breach terms |
| Privacy / responsible AI | 20% | DPA, retention, data flow, model-use restrictions |
| Integration and IT operations | 10% | SSO, API, observability, admin and provisioning |
| SLA and support | 10% | Uptime, response time, escalation and credits |
| Commercials and flexibility | 10% | TCO, seat model, notice period, negotiation |

For each dimension: 0–5 scale; weighted score = sum(score × weight). **Security/privacy gates are mandatory and cannot be offset by a high total score.** A sample invented scorecard is in [CSV](../data/vendor_scorecard_synthetic.csv); entries are **not real vendor ratings**.

## RFP / demo question bank
- Which business process and supported use case have been demonstrated, with acceptance evidence?
- How are SSO, RBAC, audit logs, offboarding, API keys and licence provisioning handled?
- What enterprise data are processed/stored; which regions, subprocessors and retention periods apply?
- Are inputs or outputs used for model training, and what is contractually enforceable?
- What are service availability commitments, severity definitions, response/resolution targets and escalation routes?
- Which billing model applies: named seats, usage credits, tokens, minutes, add-ons, API charges, storage?
- How are unexpected cost spikes capped; can licences be reassigned; what are renewal dates and exit terms?
- What features are available under the specific enterprise plan, and which claims require testing?

## Contract control register
Track agreement ID, entity/budget code, start/end, notice deadline, renewal owner, business owner, DPA and SLA link, licences purchased, unit rate and currency, annual commitment, support tier, credit rights, termination/export/deletion terms, escalation contacts and vendor compliance evidence.

## Seat management SOP
1. Capture approved seats, assigned users, active seats and spend monthly.
2. Recertify owners and remove access promptly on transfer/exit.
3. Flag unused seats; reconcile entitlements with vendor invoice and finance ledger.
4. Reallocate subject to licence terms, then right-size 30 days before renewal decisions.
5. Escalate unforecast overage, token/minute over-consumption or shadow AI.
6. Run 90/60/30-day renewal checkpoints: usage, value, risk, pricing alternatives, Procurement approval, termination notice.

## Negotiation points (not assertions about named vendors)
Enterprise price tiers, volume-flex and true-up, portability/export, service credits, breach notification, residency, use of data for training, auto-renewal protection, billing transparency and support escalation.

## Platform-specific watchlist
| Tool named in target brief | Potential product evaluation focus |
|---|---|
| Claude | Privacy, AI-assistant accuracy, enterprise access, token/seat economics |
| Synthesia | Avatar/voice permissions, content approvals, training asset updates |
| Telnyx | Communications pricing, call-recording/legal obligations, service continuity |
| Midjourney | Output/IP rights, permissible use, design review, brand approval |

No direct vendor contract/price/SLA statement is made here; current vendor terms must be checked before procurement.
