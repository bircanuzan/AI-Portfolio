# 07 | Responsible AI-Assisted HR Policy Drafting Protocol

## Use case and governance stance
AI can accelerate **first drafts**, compare document versions, extract clause inventories and surface inconsistencies. It must not autonomously interpret current employment law, make employee rights decisions, approve employment documents or release policy changes.

## Allowed / prohibited uses
| Allowed with controls | Prohibited |
|---|---|
| Suggest plain-language rewrite of previously approved concepts | Invent statutory obligations or cite nonexistent regulations |
| Compare draft/approved policy versions and propose redline summary | Treat AI output as local Legal sign-off |
| Classify issues for human review using synthetic / authorized data | Send employee contracts or personal data to unauthorized AI services |
| Produce employee FAQ draft from counsel-approved sources | Automatically alter pay/benefits or respond with binding legal advice |
| Identify missing jurisdiction placeholders | Publish without approvals, translation and HRIS UAT |

## Human-led pipeline
1. HR Policy defines issue, policy scope and intended employee audience.
2. Retrieve authorized source documents from controlled storage; record provenance, publication date and version.
3. Remove/avoid personal and confidential data unless expressly authorized in a compliant enterprise environment.
4. Ask model to propose drafts **with source-to-claim mapping and explicit unknowns**.
5. HR Policy reviews clarity, internal consistency, employee experience and contract alignment.
6. Local counsel verifies applicability, law, language and contractual/consultation implications.
7. Payroll/HRIS/privacy/operations approve relevant dependencies.
8. Authorized sponsor signs approved version; system records immutable history; employees receive correct country version.

## Example reusable prompt (draft-only)
```text
ROLE: HR policy drafting assistant. You are not a lawyer or approval authority.
TASK: Compare the two supplied, authorized policy documents and propose
clear employee-facing wording for a DRAFT only.
REQUIRED OUTPUT:
1. Revised draft with change-tracking markers.
2. Clause-by-clause source mapping to the supplied evidence.
3. Questions for qualified country employment counsel.
4. Contract, handbook, payroll, HRIS, privacy, safety and consultation impacts.
5. Conflicts, uncertainties and missing local addenda.
RULES: Never invent laws, legal citations, approval status or current facts.
If the evidence is incomplete, mark NOT VERIFIED; do not fill with guesses.
Do not insert employee personal data. Do not finalize or release documents.
```

## Acceptance checks before human review
- Every substantive legal claim traceable to an approved source / marked unverified.
- No false claim of global applicability; local addenda remain required.
- Effective dates, owner, policy ID, version and superseded references consistent.
- Compensation/benefits and working-time implications flagged for specialist review.
- No missing privacy/retention/access controls.
- Draft label visibly present; no employee-facing auto-publication.

## Model-risk test scenarios
1. AI invents a leave entitlement → source validation fails.
2. AI applies one country's rule globally → jurisdiction gate fails.
3. AI omits consultation step → checklist catches omission.
4. AI paraphrases away an employee protection → legal redline rejects.
5. AI suggests sending employee data externally → privacy gate rejects.
6. AI drafts a contract variation without consent analysis → Legal holds.
7. AI overstates financial ROI → Finance rejects until reconciled.
8. AI labels an unsigned policy "approved" → status/approval check rejects.

**Evidence status:** Proposed process and authored safeguards; no real AI benchmark, regulatory monitoring service, legal evaluation dataset, employee-data processing or production agent deployment is claimed.
