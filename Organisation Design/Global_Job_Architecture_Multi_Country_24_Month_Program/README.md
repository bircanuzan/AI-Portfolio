# Global Job Architecture and Organisation Design Transformation

**Independent 24-month implementation simulation** inspired by the requirements of an international aviation-services organisation. No dnata or Emirates Group internal information was used.

## Target outcomes
1. Clear job family/subfamily taxonomy across operations, commercial, technology and corporate functions.
2. Transparent individual contributor / manager career levels and comparable work expectations.
3. Defensible job evaluation and **locally compliant grade crosswalk**, never automatic pay harmonisation.
4. Standard job profiles, title controls, organisation design principles and defined exceptions.
5. Auditable HRIS migration, adoption, calibration cadence and BAU governance.

## Work product
1. [Discovery and current-state diagnostic](01_Current_State_Diagnostic.md).
2. [Families, career levels and role profiles](02_Job_Families_Levels_and_Profiles.md).
3. [Job evaluation / grade calibration](03_Job_Evaluation_and_Grade_Crosswalk.md).
4. [24-month delivery roadmap](04_24_Month_Implementation_and_RACI.md).
5. [Governance, OD, HRIS, adoption and handover](05_Organisation_Design_Governance_and_Change.md).
6. [Executive decision and KPI board pack](06_Executive_Reporting_and_Evidence.md).
7. [Synthetic role inventory](data/synthetic_role_inventory.csv), [provisional grade map](data/illustrative_grade_crosswalk.csv), [data QA script](src/validate_roles.py), [unit tests](tests/test_validate_roles.py).

## Delivery mechanism
Collect -> map -> evaluate -> calibrate -> pilot -> migrate -> adopt -> govern. Maintain distinct global architecture identifiers and local job/legal/payroll attributes so one geography does not overwrite country requirements.

## Local smoke test
From this project folder: **python src/validate_roles.py data/synthetic_role_inventory.csv** then **python -m unittest discover -s tests -v**. Python standard library only.

## Honest evidence boundary
The CSV is synthetic; job levels and factor weights are demonstrative and require organisation-approved evaluation. The program is a credible implementation blueprint **not proof of a real multinational rollout**.
