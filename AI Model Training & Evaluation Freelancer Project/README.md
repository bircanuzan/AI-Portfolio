# AI Model Training & Evaluation Freelancer Project

**Independent consulting work sample | Management consulting × AI response evaluation × client-ready deliverables**

> **Evidence classification:** Self-directed portfolio simulation using entirely fictional organizations, synthetic interview notes and assumed financials. No client engagement, paid evaluation contract, external model access, measured model improvement or production implementation is implied.

## Purpose
Design a repeatable way to **create, test, diagnose and improve AI-generated consulting deliverables**: documents, structured Excel models and leadership presentations. The emphasis is on whether the output can support an executive decision, not whether it merely reads well.

## Six practical consulting assignments

| ID | Workflow | Required output | Main failure modes |
| --- | --- | --- | --- |
| B01 | Executive steering committee strategy | Six-slide decision narrative | Missing decision, inconsistent KPIs, unowned actions |
| B02 | Market entry and competitive positioning | Two-page recommendation and competitor matrix | Unsupported market size, false precision, no options |
| B03 | Target operating model redesign | Workflows, ownership model and RACI | Unowned approvals, conflicting accountability |
| B04 | Sensitivity-tested business case | Formula-driven XLSX, scenarios, NPV, payback | Formula errors, hidden assumptions, unit mismatches |
| B05 | Stakeholder interview synthesis | Evidence-linked diagnosis and thematic findings | Invented quotes, unsupported consensus, omitted dissent |
| B06 | Implementation roadmap and change | 30/60/90 plan, RAID, adoption scorecard | No dependencies, baselines, owners or decision gates |

## What's in the folder
- [Charter](docs/01_Project_Charter.md) — scope, audience, data boundaries and workflow
- [Benchmark specifications](docs/02_Benchmark_Specifications.md) — task-by-task expected structure and adversarial checks
- [Evaluation rubric](docs/03_Evaluation_Rubric.md) — weighted 100-point rubric, critical-defect gates and reviewer calibration
- [Review protocol](docs/04_Review_Protocol.md) — repeatable prompt-to-revision procedure
- [Evidence and limits](docs/05_Evidence_and_Limitations.md) — self-directed work vs claims that need external validation
- [Benchmark prompts/data](data/benchmark_tasks.json) — six independent synthetic assignments
- [Human review example](data/reviewer_ratings.csv) — illustrative ratings, not verified model accuracy
- [Sensitivity assumptions](data/business_case_assumptions.json) — transparent assumed values
- [Evaluation script](src/evaluate.py) — validates human ratings, calculates weighted scores and critical gates
- [Business-case engine](src/financial_model.py) — independently recomputes NPV, payback and sensitivity cases
- [Office artifact generator](src/build_client_assets.py) — makes an editable DOCX, XLSX and PPTX with optional packages
- [Sample deliverables](samples/) — steering committee storyline, RACI, interview synthesis and change roadmap
- [Defect-log template](templates/defect_log.csv) — traceable issue/repair workflow
- [Unit tests](tests/) — local, deterministic checks

## Quick start
Python 3.10+ for the standard-library evaluation tools:

```bash
python -m unittest discover -s tests -v
python src/evaluate.py --ratings data/reviewer_ratings.csv --tasks data/benchmark_tasks.json --out evaluation_results.csv
python src/financial_model.py --assumptions data/business_case_assumptions.json
```

Generate **editable Office examples** (requires optional libraries):

```bash
python -m pip install -r requirements.txt
python src/build_client_assets.py --output-dir generated
```

The generated outputs are `client_memo.docx`, `sensitivity_business_case.xlsx` and `steering_committee_deck.pptx`. They are synthetic illustrative artifacts, not verified professional deliverables for a real client.

## Evaluation logic
Six review dimensions total 100 possible points: problem structuring 20; evidence traceability 20; quantitative accuracy 20; document/deck craft 15; implementability 15; governance and safety 10. Each human reviewer awards a **0–4** grade per dimension and records cited evidence. `src/evaluate.py` aggregates grades, applies critical-defect gates, and exports the decisions. **The script does not assess semantic correctness by itself**.

## Portfolio walkthrough
1. Read the six tasks and synthetic source data.
2. Review the sample answer structures, financial-model logic and examples.
3. Score candidate outputs against the anchored rubric, with at least one evidence note per rating.
4. Recompute financial claims and inspect assumptions/formulas.
5. Flag severe defects; revise; compare original and revision with a reproducible issue log.
6. Treat all portfolio ratings as demonstrations until independently blinded, replicated and calibrated.

**Tools:** Python, JSON/CSV, Excel/openpyxl, PowerPoint/python-pptx, Word/python-docx, human review, structured problem solving, scenario modeling and quality control.

**Maintainer:** Bircan Uzan | HumanEvoX Talent Consultancy | [Portfolio homepage](https://github.com/bircanuzan/AI-in-HR-Portfolio)

