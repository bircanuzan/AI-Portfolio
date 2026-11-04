# Enterprise Organizational Transformation | Integrated Advisory Case

**Scenario:** Northstar Clean Energy Services (NCES), a fictional 600-person clean-energy services organization operating in the UAE, Saudi Arabia and Qatar. NCES is expanding from traditional engineering services into digital energy solutions, but its fragmented operating model, capability profile, culture and HR delivery limit execution.

**Assignment:** Develop a CEO / CHRO / Transformation Steering Committee decision package linking strategy, structure, skills, behaviors, performance, HR and value realization.

**Status:** Independent synthetic case and runnable scoring prototype; NOT live client work, validated employee feedback, commercially proven savings or an implemented restructure.

## Executive problem and advisory hypothesis
- **Strategy:** Scale cross-border customer delivery and a digital product offering without creating duplicated accountability.
- **Organization:** Separate commercial, delivery and digital activities lack clear end-to-end ownership; approvals cross functions.
- **Capability:** Digital service leadership, skills visibility, manager coaching and HR data stewardship lag target proficiency.
- **Culture:** Functional optimization and low challenge/feedback undermine collaboration.
- **Performance:** Output KPIs do not consistently reward customer outcomes, cross-functional contribution or coaching.
- **HR:** Multiple inconsistent employee journeys and weak case ownership impair service confidence.

**Advisory hypothesis:** A value-stream-aligned matrix with clear process ownership, a capability academy, manager-led behavior change, enterprise performance calibration and redesigned HR services can improve speed and accountability. This remains a hypothesis until tested with evidence.

## Five linked advisory workstreams

| Workstream | Decision document | Measurable output |
| --- | --- | --- |
| 1. Organization redesign | [02 — Operating model and redesign](02_Organization_Redesign_and_Operating_Model.md) | Accountability map, design options, approval gates and transition dependencies |
| 2. Capability-gap assessment | [03 — Capability assessment](03_Capability_Gap_Assessment.md) | Prioritized skills and operating capabilities; evidence confidence gates |
| 3. Cultural transformation | [04 — Culture playbook](04_Cultural_Transformation_Playbook.md) | Defined behavior standards, adoption and psychological-safety indicators |
| 4. Performance framework | [05 — Performance architecture](05_Performance_Framework.md) | Strategy-to-role cascades, calibration controls, check-in cadence |
| 5. HR transformation | [06 — HR transformation roadmap](06_HR_Transformation_Roadmap.md) | HR target operating model, employee service improvements, HRIS governance |

## Advisory materials
- [01 — Transformation charter and fact base](01_Transformation_Charter.md)
- [07 — Benefits, risk and governance](07_Benefits_Risk_and_Governance.md)
- [08 — CEO / SteerCo decision memo](08_Executive_SteerCo_Decision_Memo.md)
- [Synthetic capability baseline](data/capability_gap_baseline.csv)
- [Illustrative operating-model option economics](data/operating_model_options.csv)
- [Benefits tracking register](data/benefits_register.csv)
- [Scoring tool](src/score_capabilities.py) and [unit tests](tests/test_score_capabilities.py)

## Reproducible scoring

From repository root:

```bash
python "Organizational Transformation Advisory/Enterprise_Transformation_Advisory_Case/src/score_capabilities.py" > capability_priorities.csv
python -m unittest discover -s "Organizational Transformation Advisory/Enterprise_Transformation_Advisory_Case/tests" -v
```

Formula: **priority = MAX(0, target maturity − current maturity) × business criticality**, where maturity is 0–5 and criticality is 1–5. The tool labels weak sample evidence for revalidation rather than treating the scores as fact. Scripts produce a review queue, **never** employee-level judgments, restructuring actions or promotion decisions.

## Governance and milestones
- **Days 0–30:** mandate, confidential interviews, business value-stream mapping, capability evidence plan, employee consultation design.
- **Days 31–90:** compare alternative organization designs, prioritize gaps, test new performance scorecard, run culture pulse baseline and HR employee-journey diagnostics.
- **Months 4–6:** controlled process pilots, manager enablement, data remediation, governance and legal approvals.
- **Months 7–12:** phased deployment only if gates pass; monthly value tracking and independent employee impact review.

### Outcomes to demonstrate
This portfolio demonstrates *a documented approach and runnable assessment tool*; no numerical improvement, cost saving, employee opinion, or customer outcome is represented as actually achieved. See the benefits register for modeled targets and verification rules.
