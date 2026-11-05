# Portfolio architecture | CHRO × CTO decision record

## Strategic intent
Unify a formerly fragmented portfolio into **15 competency-based main categories**.
Role titles and one-off interview demonstrations are subprojects, not top-level categories.
Model, dataset, README, test and control artifacts stay inside their respective project subtrees.

## CHRO content boundaries
- Corporate HR strategy / job architecture / transformation: distinct from talent acquisition and talent development.
- People Analytics owns workforce evidence; HR Technology owns HR systems and integration.
- HR Operations owns delivery controls and policy mechanics.
- Workforce Transformation owns Human–AI capacity, organization design interfaces and agent workforce governance.

## CTO technical boundaries
- Agentic AI development owns runnable agent/integration patterns; AI Adoption owns human rollout.
- Model Training & Evaluation owns data quality and evaluation; Responsible AI owns risk controls and assurance.
- AI Transformation owns business value and process change; AI PMO owns project execution.
- Preserve relative imports/data paths, repository test workflows and project-level READMEs.

## Navigation / migration
- Migrated **843 files** from legacy top-level project folders into competency portfolios.
- Updated links in **123 text files** based on their original source and destination paths.
- Retained all original project bytes unless a source file's relative documentation links needed correction.
- Legacy one-page relocation pointers are preserved under functional category Legacy Navigation folders.
- Previous externally shared direct GitHub folder URLs may need replacement; GitHub does not automatically redirect directory moves.
- CI workflows need a deliberate review of changed working-directory and test paths before promotion.

## Quality gates
- Run privacy/identity scan, existing CI suites and broken-link checks on the proposed branch.
- Require clean project inventory and no unresolved path collisions before merging.
- A green smoke test does not guarantee production readiness or real client deployment.
