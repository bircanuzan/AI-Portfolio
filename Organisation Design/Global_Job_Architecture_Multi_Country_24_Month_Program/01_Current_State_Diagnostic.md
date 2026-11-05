# 01 | Current-State Diagnostic: Fragmented Titles, Levels and Structures

## Discovery objective
Inventory role/organisation data before designing a taxonomy. Trace legal entities, countries, HRIS structures, payroll grades, reporting relationships, job descriptions, union/collective agreements where applicable, and workforce planning dependencies.

## Sample multi-country case
Three synthetic markets **Market A / B / C**, not actual sector_organization organisation designs. Local titles such as "Station Lead", "Duty Manager" and "Customer Operations Supervisor" can refer to dissimilar decision scope. A single title string cannot establish an equivalence or grade.

## Required extracts
| Data set | Minimum fields | Owner |
| --- | --- | --- |
| HRIS position/job | Position ID, job code, local title, legal employer, business unit, location, FTE | HRIS |
| Organisational reporting | Parent position, manager position, spans, layer | OD / HRBP |
| Role accountabilities | Current JD, mission, decision rights, financial/operational scope | BU HR |
| Current pay/grade | Local grade code, job evaluation approval, compensation policy | Reward |
| Market obligations | Statutory titles, certification/licence, collective agreements, languages | Local HR / legal |
| Skills / competency | Capability profile, career pathway and critical skills | Talent |
| Change history | Approved exceptions, unresolved legacy titles, vacancies | Governance |

## Diagnostic tests
1. Multiple titles for materially identical role scope.
2. Same title spanning distinct complexity/accountability.
3. Missing or outdated job descriptions and grade approvals.
4. Local grades presented as directly comparable across countries.
5. Duplicate job codes, orphan position/reporting IDs or invalid job families.
6. Hierarchical anomalies: implausible spans/layers, managers reporting to individual contributors.
7. Country-specific professional licence or legal terms omitted from global role.
8. Unowned jobs and uncontrolled changes in HRIS.

## Baseline outputs / actions
- Coverage measures: complete JDs %, valid job codes %, roles evaluated %, grade crosswalk coverage %, exceptions with owner %.
- Heat map by business, country, family and criticality.
- Data steward sign-off and approved issue log **before** job evaluation.
- Prioritise high-volume shared roles, scarce skills, critical operations and regulatory exposure for pilots.

## Stakeholder workshops
CEO/CHRO steering committee sets principles; international operations leaders validate work content; HRBPs confirm local realities; Reward moderates grading; HRIS validates system feasibility; local Legal checks contracts and laws; communications lead maps employee impact.

**Do not conflate organisational layer, position, job, person, grade, salary band or job title.** These are linked but separately governed entities.
