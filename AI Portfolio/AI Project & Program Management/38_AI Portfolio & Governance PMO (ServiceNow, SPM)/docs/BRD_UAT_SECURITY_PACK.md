# BRD, UAT and Security Evidence — Example PMO Pack (Fictional)

## BRD excerpt: AI demand governance
**BRD-001:** Demand records must retain owner, category, strategy alignment, benefit hypothesis and approval evidence.  
**BRD-002:** The portfolio board must see the projected cost, approved funding and financial gap separately.  
**BRD-003:** A demand cannot become a live AI-enabled product before UAT, security and ownership sign-offs.  
**BRD-004:** Rejected/deferred demands must retain disposition rationale and next review date.  
**BRD-005:** All exceptions must have responsible owner, escalation deadline and a tracked closure decision.  
**BRD-006:** All data in the pipeline report must be refreshable from designated canonical records.

## UAT scenarios
| ID | Test | Expected result | Evidence |
|---|---|---|---|
| UAT-01 | New demand without sponsor | Flag incomplete; do not qualify | Missing-field exception |
| UAT-02 | Approved demand missing finance sign-off | Funding gate HOLD | Approval exception |
| UAT-03 | Cost forecast above approved funds | Report shortfall separately | Financial exception |
| UAT-04 | Deferred demand | Preserve reason and revisit date | Pipeline disposition entry |
| UAT-05 | Convert approved demand to project | Link original demand and record approvals | Crosswalk |
| UAT-06 | Pilot go-live | Require product owner, security, acceptance | Product handover |
| UAT-07 | Critical RAID unresolved | Escalate to VP forum | RAID record |
| UAT-08 | Product retirement | Verify archive, access shutdown and benefit closure | EOL evidence |

## Audit-ready document checklist
Signed demand/business case, BRD and acceptance criteria, design and data assessment, risk/impact assessment, security/privacy decision, UAT evidence and defect retest, financial and funding sign-off, governance meeting decision, RAID and change log, closure acceptance, benefit review.

## Security approvals
The example records mark some reviews PENDING; **no security test or penetration test was executed**, and no real product go-live approval is claimed.
