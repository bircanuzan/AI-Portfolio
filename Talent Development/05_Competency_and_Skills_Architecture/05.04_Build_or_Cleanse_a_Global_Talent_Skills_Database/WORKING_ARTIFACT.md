# Skills Data Dictionary and Cleansing Rules
**Project:** 05.04 — Build or Cleanse a Global Talent Skills Database

> **Independent, interview-aligned sample work product — SYNTHETIC.** This does not describe completed work at clean_energy_group.

## Executive decision
Normalize skill IDs validate expiry and assign records to owners.

## Worked fictional scenario
**Operational signal:** Regional employee records have duplicate certification names and expired licenses.

| Evidence field | Illustrative design / decision entry |
|---|---|
| Business problem | Regional employee records have duplicate certification names and expired licenses |
| Decision supported | Normalize skill IDs validate expiry and assign records to owners |
| Proposed approach | ESCO; SFIA; entity matching; Oracle HCM or approved skills platform |
| Mandatory validation | Employee right to correct inferred skills |
| Primary effectiveness measure | Skills record completeness validity and freshness |
| Executive owner | Business sponsor with Head of Talent Development as process owner |
| Implementation status | Design / decision proposal — not implemented |
| Review gate | Data validated -> impacted owners consulted -> Finance or risk review as needed -> sponsor decision -> follow-up |

## Reusable operating worksheet
| Case ID | Evidence / source | Gap or trigger | Recommendation | Owner | Milestone | Status |
|---|---|---|---|---|---|---|
| 05.04-CASE-01 | To be confirmed with authorized process/data owner | Regional employee records have duplicate certification names and expired licenses | Normalize skill IDs validate expiry and assign records to owners | Named business sponsor | First quarterly review | Proposed |
| 05.04-CASE-02 | Validate with business owner, HRIS and SMEs | Measure against: Skills record completeness validity and freshness | Reassess after controlled pilot | Head of Talent Development | Next quarterly review | Awaiting evidence |

## Decision-quality checklist
- [ ] Confirm whether training, process change, resource allocation, system configuration or hiring is the correct intervention.
- [ ] Confirm baseline, population, relevant operational risk and data provenance before presenting results.
- [ ] Define decision rights, financial owner, control evidence and risk acceptance explicitly.
- [ ] Record evidence at baseline and at an agreed follow-up; report variance and uncertainties.
- [ ] Escalate any safety, privacy, fairness or materially adverse workforce impact to qualified reviewers.

## Evidence needed to make this real
A signed requirements brief; lawful dataset access; validated baselines; approved business sponsor; tested controls; implementation/change records; post-intervention outcome evidence.
No completion, impact, vendor implementation or certification is claimed in this demo.
