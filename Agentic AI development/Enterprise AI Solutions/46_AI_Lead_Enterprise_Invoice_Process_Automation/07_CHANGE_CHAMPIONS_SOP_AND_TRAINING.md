# C — Adoption and Change: Communications, AI Champions, SOP and Training

## Change objective
Move from invisible email follow-up to a controlled case queue and accountable human review. The human role **changes** from copying invoice fields to quality/exception decisioning; it is not replaced by AI. A user who distrusts extraction needs a clear override and escalation path, not a forced acceptance workflow.

## Stakeholder impact and ADKAR-style response
| Role | Current experience | Future experience | Barrier | Intervention |
|---|---|---|---|---|
| AP clerk | email intake/rekeying | verify extraction + exceptions | fear of being deskilled; workload peaks | show human authority and time saved; supervised clinic |
| AP manager | manual spreadsheet chase | queue quality + SLA owner | data mismatch | pilot dual-run and reconcile |
| Procurement | ad-hoc PO emails | tracked mismatches | exception volume | standardized reason codes, shared handoff |
| Controller | high-value requests via email | formally delegated approvals | audit/regulatory risk | hard-stop demo and access review |
| Vendor master team | bank changes via messages | independent verification queue | increased verification effort | exception SOP and fraud checklist |
| Executive sponsor | qualitative improvement claims | measured benefit dashboard | financial overstatement | agree baseline and realization definitions |

## 30/60/90-day proposed adoption plan
| Time | Activities | Accountable outcome | Exit evidence |
|---|---|---|---|
| Days 1–30: awareness and design | pulse interviews, 3 workshops, baseline, champion nominations by entity, process-owner walkthroughs | signed AS-IS and BRD targets | discovery notes, champion roster, baseline sampling |
| Days 31–60: ability | role-specific demos, AP and controller simulations, draft SOP, integration/UAT rehearsal, accessibility check, FAQs | 100% pilot cohort trained before launch | training attendance, knowledge checks, UAT signatures |
| Days 61–90: reinforcement | monitored pilot, office hours, weekly exception huddles, adoption heatmap and adjustments | sustainable safe routing (targets validated) | dashboard trend, defect resolution, go/no-go committee |

**This is a proposed timeline; no real users were trained.**

## AI champions network
- Nominate at least one AP, Procurement, IT, Finance and business-unit champion for pilot entities (pilot size TBD).
- Weekly 20-minute stand-up: top 3 friction points, rejected AI fields, new exception patterns and single owner per action.
- Monthly champion council with AI Lead + L&D: policy updates, training refresh, evidence of workarounds.
- Track champion coverage, response time to queries, ideas adopted and unresolved blockers. Avoid grading individual employees using opaque AI scores.

## Communication kit
**Sponsor pre-launch note:** “We are testing a new invoice workflow that suggests field values and tracks approvals. It will not make payments, change supplier bank data or replace delegated human approvals. Pilot users can correct fields, flag errors and use a manual fallback.”

**AP launch micro-message:** “Verify supplier, invoice number, amount, VAT and PO. Never assume an AI-extracted field is correct. If confidence is low, the invoice is a suspected duplicate or banking has changed, use the exception queue and follow SOP.”

**Vendor note (draft, approval pending):** “Please use the nominated submission channel and include invoice number, supplier reference, PO and required tax details. We will contact you through verified channels if clarification is needed. Do not share bank changes in unsecured replies.”

## SOP v0.1 — Invoice exception handling (proposed)
1. Check user identity, entity scope and inbound case ID.
2. Compare extracted field suggestions **against the source document**, never only against AI output.
3. If duplicate flag: HOLD; locate prior invoice and escalate to AP control reviewer.
4. If bank change: STOP processing and refer to master-data fraud verification. Never accept change based on email alone.
5. For missing PO/mismatch/VAT issues: assign to named owner and record supporting decision.
6. For accepted matched cases: send to appropriate **human** approver by delegation limit.
7. If approval is rejected: record rationale and notify supplier with approved template only.
8. If approved: route posting request to ERP-authorised AP user, not automated payment.
9. If integration fails: log incident and move to secure manual queue; ensure no silent duplicate handling.
10. Record each event and feedback category; weekly quality check against original invoices.

## Training design and reinforcement
| Module | Audience | Duration | Assessment |
|---|---|---:|---|
| 1. Why the workflow changes; AI boundaries | all pilot users | 20 min | 5-question knowledge check |
| 2. Verify extraction and route exceptions | AP and Procurement | 45 min | 4 supervised scenarios |
| 3. Approval delegations and fraud flags | Finance/controllers | 30 min | replay high-risk case |
| 4. Dashboard and issue ownership | managers, champions | 30 min | diagnose 3 KPI trends |
| 5. Integration recovery and auditing | IT support | 30 min | recovery exercise |

Training artefacts are design assets, not training delivery claims.

## Adoption barriers and intervention triggers
- **Shadow approvals in email:** >5% of approval decisions bypass queue → supervisor coaching + workflow fix.
- **Low extraction trust:** manual correction rate >15% in a sampled category → isolate document layout, retrain vendor template and re-evaluate AI.
- **SLA deterioration:** p90 time worsens for 2 weeks → inspect backlog and staffing, stop expanding pilot.
- **Fraud/control incident:** any unauthorized bank-data amendment or approval bypass → emergency stop and formal incident review.
- **Champion fatigue:** unresolved feedback >10 working days → assign action owner and close loop.
Thresholds provisional; process owners must validate.