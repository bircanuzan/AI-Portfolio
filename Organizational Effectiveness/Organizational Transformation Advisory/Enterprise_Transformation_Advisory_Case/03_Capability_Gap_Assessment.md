# 03 | Evidence-Led Capability Gap Assessment

## Purpose
Translate target operating-model demands into **organization/role-family capability investment decisions**. This is not a psychological test, a ranking of people, or an automated employment decision.

## Assessment method
1. Define critical outcomes and value-stream activities; produce a skills and capabilities taxonomy.
2. Set target maturity and criticality through business/CHRO calibration.
3. Triangulate **structured interviews, task evidence, process KPIs, work samples and anonymized survey themes**.
4. Apply the original illustrative rubric and document assessor, sample size, date and confidence.
5. Rank gaps for learning, redesign, hiring, tooling or process action; validate low-confidence cells before decisions.
6. Reassess at 90 and 180 days using consistent evidence criteria.

### Maturity rubric, 0–5
| Level | Observable maturity |
| --- | --- |
| 0 | Capability absent / no repeatable evidence |
| 1 | Ad hoc and person-dependent |
| 2 | Defined in pockets; inconsistent application |
| 3 | Documented and generally repeatable |
| 4 | Measured, managed, broadly adopted |
| 5 | Optimized with sustained outcomes and independent review |

Intermediate scores can be used when assessors agree a capability falls between adjacent anchors. **Confidence is evidence quality, not employee competence.** Low confidence and fewer than 10 supporting observations are flagged for review.

## Computational specification
- Columns: id, domain, capability, accountable owner, maturity score, target, criticality, impacted-role count, sample size and evidence confidence.
- **Gap:** max(0, target − current).
- **Priority score:** gap × criticality, range 0–25. The score is a **triage heuristic** and must never become a basis for individual adverse employment decisions.
- **Bands:** high >= 8, medium >= 4, otherwise low.
- **Evidence gate:** REVALIDATE when confidence is low OR supporting sample size < 10.
- If multiple capabilities tie, sort by larger affected population then capability ID. Business judgment and budget constraints override a simplistic arithmetic rank.

## Worked baseline
See [synthetic register](data/capability_gap_baseline.csv). Example: Performance calibration and coaching **2.0 → 4.2**, criticality 5, yields a 2.2 gap and **11.0** priority. Critical skills mapping **2.3 → 4.3**, criticality 5, yields **10.0**. Both require further qualitative review and validation.

## From gap to intervention
| Gap class | Example intervention | Success evidence |
| --- | --- | --- |
| Structural / decision rights | RACI redesign, accountable owner, escalation SLA | Reduced exceptions and cycle time |
| Digital and data | Data steward appointments, data-quality controls, HRIS training | Reconciled records, audit pass rate |
| Critical skill coverage | Role-based assessment, reskill cohort, hiring mix | Validated proficiency and mobility |
| Manager effectiveness | Coaching, 1:1 templates, calibration practice | Check-in quality and fairness audits |
| Cross-functional culture | Joint OKRs, retrospectives, sponsor role-modeling | Cross-team adoption and trust pulse |

## Responsible use
Document consent/appropriate legal basis, minimize personal data, include employee representatives where appropriate, and separate de-identified aggregate organizational diagnostic material from individual employment decisions. No individual-level inference is made here.
