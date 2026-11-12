# 05 | Organisation Design, Governance, HRIS, Change and BAU Handover

## Organisation design principles
Design around strategic operating capability and accountable decision rights, not an attractive org chart. Review process ownership, spans and layers, site complexity, safety-critical segregation of duties, central vs local services and critical skills before changing roles.

**Span/layer evidence:** benchmark function and risk context; do not impose universal span targets on operational or regulated teams. Separate **position redesign** from **employee assessment/redeployment** and ensure local legal/consultation process.

## Target HRIS object model
- Global job profile: unique job code, family, subfamily, level, track, version, valid-from/to, owner.
- Local position: position ID, country, entity, unit, manager position, approved local title and local obligations.
- Grade mapping: jurisdiction, local grade, evaluated global profile, effective date, approval reference.
- Incumbent assignment: person/position link handled with appropriate access; **not stored in this public repository**.
- Change log: requester, rationale, version diff, approvers, effective date and next review.

### Integration governance
Use role-based controls and four-eye approval for grade updates. Establish ERP/HRIS source of truth, upstream payroll dependencies, integration reconciliation, negative tests for invalid codes, and rollback / dual-run as required.

## Operating governance
**Job Architecture Council (monthly):** OD chairs, Reward owns grade decisions, local HR validates market variants, functional leaders approve role accountabilities, IT/HRIS applies controlled configuration.

**Trigger events:** new role, material responsibility change, structural redesign, reorganisation, acquisition, legal changes, biennial refresh.

**Change control workflow:** ticket -> role content review -> level / evaluation impact -> Reward + local legal approval -> title/profile version -> HRIS UAT -> effective date -> communicate -> post-change audit.

## Country-specific design controls
Local title may differ from global title if approved; local statutory qualifications preserved; local compensation structures are not automatically equalized; maintain records for collective agreements, licensing and privacy. Apply documented exception expiry and annual review.

## Change management
- Sponsors: CHRO plus local business head, with visible reason for change.
- HRBP enablement: calibration training, JD clinic and manager Q&A.
- Manager communications: what changes, what does not, who decides, grade-related escalation.
- Employee messages: no assumption of changed compensation, contract or status; route individual questions through local HR.
- Adoption: weekly pilot office hours, monthly governance review, role profile usage tracking, exception trend dashboard.

## Sustainable handover
Publish versioned policy, system dictionary, RACI, calibration decision log, training videos, master role catalogue, change forms, QA script, audit checklist, ownership sign-offs and 30/60/90-day BAU reviews.

**Non-negotiable:** no automated changes to pay, grades or reporting lines based solely on string-title matching or an unreviewed algorithm.
