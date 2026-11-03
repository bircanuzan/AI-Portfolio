# Recruitment quality gates: deterministic QA, Claude skill integrity, and human approval

**Strengthening Project 55** with a coherent QA / release model, not creating a second shortlisting project.

## Existing risk audit (preserved)
- Sixteen synthetic matched candidate-pair scenarios; 32 invented variants.
- Intentionally flawed deterministic scoring mock produces 9 unjustified outcome flips when irrelevant fields change.
- Controlled demonstrator records zero such flips on these limited cases; this **does not** establish job-valid screening, fairness or legal approval.
- Existing 14-item risk register includes 2 explicitly critical synthetic risks.

## New, distinct integration and engineering evidence
- [Versioned 17-skill catalogue](workflow_catalog.json) identifies every original Claude-compatible recruitment workflow.
- [Executable directory-and-SKILL integrity audit](src/catalog_integrity.py) checks source/status, expected folder names, roles and mandatory human-decision restrictions.
- [Executable release assurance report](src/release_assurance.py) aggregates screening audit, critical risks and Claude workflow integrity.
- [Synthetic HOLD evidence](evidence/recruitment_release_gate.json) and [unit tests](tests/test_release_assurance.py) enforce **no external action / no automated hiring**.

```bash
python src/release_assurance.py --out evidence/recruitment_release_gate.json
python -m unittest discover -s tests -v
```

## Risk committee criteria before real usage
- Job analysis and role-related validated assessment, independent review and explainable candidate challenge process.
- Lawful recruitment data, demonstrable accessibility alternative, documented privacy, retention, data security and vendor accountability.
- Suitable independent bias and subgroup assessment only where permissible; do not infer sensitive traits or claim algorithmic neutrality from 16 toy pairs.
- Local country/clinical/immigration rules verified from official/current sources; actual worker/employment conditions confirmed by qualified humans.
- Real ATS integration testing, monitoring, incident owner and appeal process.
- Human-owned employment and offer authorization and signoff.

**Gate:** `HOLD` regardless of controlled toy scorer performance. There is no deployment, release override or employee decision method in this repository.

## Technical truthfulness
This suite tests **Python source, synthetic fixtures and the presence of written SKILL.md constraints**. It does not run Claude, execute prompts on a live language model, inspect vendor ATS bias, verify professional licences or perform legal compliance audits.
