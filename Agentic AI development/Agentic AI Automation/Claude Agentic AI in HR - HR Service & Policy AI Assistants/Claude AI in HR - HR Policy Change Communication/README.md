# Claude AI in HR - HR Policy Change Communication

> **Status: original design / Claude-compatible skill; NOT a verified Claude run, production agent, client deployment or copied product asset.**

**HR function:** Employee communications  
**Project ID:** CAI-HR-31  
**Human owner:** HR Communications  
**Platform concept:** Claude.ai / Claude Code / Claude Cowork with optional organisation-approved connectors. No integration is claimed.

## Client problem
Translate approved policy changes into accessible employee updates. In an anonymised UAE X-industry scenario, HR Communications needs an auditable way to turn approved inputs into a consistent, reviewable output.

## Goal and deliverable
- **Deliverable:** Change notice, manager brief, and questions to clarify.
- **Required inputs:** approved old and new policy; effective date; audience.
- **Success metric:** unverified policy claim count.
- **Human accountability:** HR Communications reviews, corrects, and approves the artifact before use.

## Methodology — intake → draft → test → handoff
1. **Intake:** enumerate the approved inputs, owners, effective dates, and source versions. Missing information must be labelled `MISSING`.
2. **Validation:** separate facts from assumptions, check conflicting fields, and reject unknown or unverified legal/policy claims.
3. **Claude work:** invoke the original instructions in [SKILL.md](SKILL.md) and supply the fictional [case input](examples/synthetic_case.json).
4. **Evidence:** draft `hr-policy-change-communication_output.md` with fields `fact/source_id`, `assumption`, `missing`, `risks`, `proposed_artifact`, `reviewer_decision`.
5. **Quality control:** run the [acceptance checklist](tests/acceptance.md) against real outputs **when available**; do not mark hypothetical expected behavior as a pass.
6. **Human handoff:** HR Communications checks appropriateness and confirms any external communication, employment action, payment, or legal conclusion.

## Intended workflow
```text
Approved HR inputs + source register
       ↓
Schema/consistency check → MISSING or conflict? → Human clarification
       ↓
Claude skill draft (no authority to decide)
       ↓
Evidence references + risks + confidence limitations
       ↓
HR Communications review / revision
       ↓
Approved change notice, manager brief, and questions to clarify (only after human sign-off)
```

## Synthetic exercise
The [sample JSON](examples/synthetic_case.json) contains fictional work requests with labeled synthetic source placeholders. **Expected outcome:** a traceable change notice, manager brief, and questions to clarify, or a stop-and-escalate response when required facts are missing. An LLM-produced response is **not** included because this skill has not been executed in Claude.

## Measurement and risks
Track: unverified policy claim count; number of unsupported facts; missing-field detection; reviewer corrections; policy citation errors; human approval status; prompt/version and test date. Risks: confidential people data, inaccurate policies, jurisdictional assumptions, biased inferences, unapproved outbound actions, and reviewer overreliance. Use synthetic or expressly approved data only.

## Runbook
1. Create a Claude project in an organisation-approved account and load `SKILL.md`.
2. Paste the synthetic input from `examples/synthetic_case.json` and request the specified output schema.
3. Save the **unaltered** model response locally and record model/version, prompt/version, time, source versions, and reviewer.
4. Apply the acceptance tests and record actual results; update this README only after real evidence is available.

## Evidence statement
**Prepared:** 2026-11-02. The files prove workflow design and test planning, **not live Claude agent performance**. No confidential customer/employee records, proprietary Gumroad materials, paid assets, or invented evaluation results are included.

## Attribution and independence
Inspired by public high-level coverage of *The Claude HR Department* ([product page](https://kumail.gumroad.com/l/HR)) and general HR use cases. The seller's individual agent/skill documents were not accessible and this project is independently authored, **not a reproduction or claimed exact match**.
