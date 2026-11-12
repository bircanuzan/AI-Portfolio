# Repeatable Quality Assurance & Revision Protocol

## Phase 1 — Construct
Freeze the task brief, source pack and acceptance criteria. Label all source provenance as supplied, derived, assumed or unavailable. Keep the underlying benchmark out of the model output, when evaluating real systems.

## Phase 2 — Generate
Capture prompt version, response text, model/configuration (only when actually used), timestamp and any file-generated formulas. Do not invent an invocation log for a model that was not run.

## Phase 3 — Verify
- **Documents:** check decision framing, fact-to-source links, contradictory passages, missing alternatives, accessibility and final recommendation.
- **Spreadsheets:** inspect typed inputs, formulas vs hard-codes, units, sign convention, NPV/payback, sensitivity, scenario toggles and hidden-sheet assumptions.
- **Slides:** reconcile every displayed KPI with financial model; ensure chart labels, clear slide headlines, board ask and one accountable next step.
- **Interviews:** preserve dissent and speaker separation; quotes only with exact text present in the fictional source notes.
- **Operating models:** check ownership, handoffs, workflow exceptions and explicit human sign-off.
- **Roadmaps:** test dependencies, baseline metrics, risk owner and stop/go criteria.

## Phase 4 — Grade
Use `docs/03_Evaluation_Rubric.md`. Enter dimension scores and a defensible rationale in the ratings CSV. Use `critical_defects` as a pipe-delimited list of allowed codes or leave blank. A reviewer should cite an output section or cell; broad praise is not evidence.

## Phase 5 — Repair
Create one defect-log record per discrete fault with severity, reproduction step, expected vs observed, root-cause hypothesis, owner, proposed change and status. Recheck related content after each fix to avoid regression.

## Phase 6 — Release
Export transparent results from `src/evaluate.py` and include open issues. No artifacts can be certified as 'client ready' solely because a deterministic script returns a high score.

## Data and confidentiality
Everything in this project is fictional. Before any real engagement, obtain authorization, redact sensitive data, define permissible AI usage and retention, and have a human owner approve final documents.

