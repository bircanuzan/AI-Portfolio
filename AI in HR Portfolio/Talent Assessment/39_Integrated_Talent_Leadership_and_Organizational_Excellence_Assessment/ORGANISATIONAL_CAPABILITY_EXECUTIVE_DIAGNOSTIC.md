# Enterprise Leadership and Organisational Excellence | Evidence Priority Lab

**Project 39’s independent executive specialty is the health of organisation-level leadership/operating systems, not individual candidate scoring.** It does not certify EFQM, ADAEP or any other accreditation.

## Executive use case
A fictional UAE service organisation wants to decide which *evidence gaps* must be investigated before funding skills development, leadership succession, redesign, people-process reform or responsible AI adoption.

The model explicitly **does not produce organisational maturity scores**. It prioritises which missing or incomplete evidence to validate first; higher priority means a **research / governance gap**, not proof an organisation performs poorly.

## Technical artifacts
- [Six fictional enterprise domains](data/synthetic_organisational_evidence.json)
- [Python source / assessment of evidence completeness](src/evidence_priorities.py)
- [Unit tests including negative cases](tests/test_evidence_priorities.py)
- [Reproducible source-grounded executive queue](evidence/evidence_priority_report.json)

Run inside Project 39:
```bash
python src/evidence_priorities.py --out evidence/evidence_priority_report.json
python -m unittest discover -s tests -v
```

## Evidence priority rule (not a published assessment scale)
`review_priority_index = illustrative_impact_weight (1–5) × evidence_gap_factor`.
Gap factors: `missing = 3`, `partial = 2`, `synthetic_documented = 1`. All data is fictitious, and even a documented mock evidence field is *not verified employer proof*. The index is for **investigation order only**. There is no automated employment, promotion, organizational excellence grade or funding decision.

## CHRO / CAIO questions
1. Are critical roles mapped to future operating-model needs and approved capability models?
2. Is leadership development supported by specific observed work and evidence rather than self-reported impressions?
3. Can executives trace workload/capacity, human–AI task allocation and process redesign to actual outcomes?
4. Are governance, privacy, grievance, appeal and assessment assurance accessible and documented?
5. Are skills investments linked to capability deployment, not just training completion?
6. Do finance/HR owners confirm value and risk metrics before scaling?

## Review protocol
Stage 1 document provenance → Stage 2 HR/legal/finance validation → Stage 3 targeted interview and process review → Stage 4 qualified practitioner assessment → Stage 5 options and costed business case → Stage 6 human board/CHRO decision.

This project complements Project 08 (talent strategy), Project 38 (observable individual behavioural assessment) and Project 49 (psychometric test-use evidence).

**No real diagnostic, regulated score, government programme result, client maturity rating or implemented AI organisational redesign is claimed.**
