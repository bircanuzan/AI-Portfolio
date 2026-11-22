# Instructional Design Expert

## AI Evaluation | Learning Experience Design | Accessibility | Digital Delivery

**Portfolio project:** Instructional design quality and AI response evaluation, using synthetic learning scenarios and a runnable, offline benchmark. **Evidence status:** Independent educational demonstration, not an employer/client commission, production system, completed accessibility audit, or verified model-training result.

### Business requirement

A fictional enterprise learning team wants to review AI-generated instructional design recommendations before they are used in workplace learning. AI responses can sound persuasive while mismatching objectives to assessments, making unsupported pedagogical claims, overlooking disability access or assuming an unrealistic digital delivery environment. Build an expert-led evaluation process that identifies consequential errors, documents how a better answer should reason, and creates consistent evaluation data for future AI improvement.

### Project objectives

1. Evaluate domain-expert responses about **learning activities, accessibility, digital delivery and educational evaluation**.
2. Identify **misaligned objectives, invalid assessment assumptions, unsubstantiated claims and accessibility risks**.
3. Create **reference answers, anchored scoring criteria, and precise correction rationales**.
4. Provide **structured AI quality feedback**: error severity, domain, expected decision and improvement action.
5. Separate **synthetic evaluation-fixture checks** from real LLM results and human pedagogical assessment.

### Use cases and dataset

| Case | Business/learning problem | Evaluation focus |
| --- | --- | --- |
| ID-001 | Leadership course promises applied change analysis but tests glossary recall only | Learning objective alignment and assessment validity |
| ID-002 | Mandatory prerecorded training video has no captions | Media accessibility and inclusion |
| ID-003 | AI claims universal 90% performance improvement without evidence | Unsupported pedagogical claims and traceability |
| ID-004 | Remote professional learning uses an authentic assessed case and accessible format choices | Valid design and recognition of a strong solution |
| ID-005 | Programme completion count presented as proof of on-job improvement | Outcome evaluation, transfer and inference |
| ID-006 | Mouse-only drag-and-drop assessment | Keyboard access and digital interaction |
| ID-007 | Field workforce with poor connectivity receives streaming-only learning | Mobile-first, low-bandwidth delivery and access |
| ID-008 | Flexible assessed formats and multimodal learning with a clear rubric | Universal Design for Learning and fair assessment |

Source scenarios and both strong / deliberately flawed response fixtures are in [data/evaluation_cases.jsonl](data/evaluation_cases.jsonl). **All eight examples are fictional and written for this portfolio. No LLM responses are represented as actual model outputs.**

### Methodology — end-to-end workflow

**1. Learning needs and performance analysis** — Clarify audience, professional context, measurable skill gaps, job tasks, accessibility requirements, device/network conditions and constraints.

**2. Instructional architecture** — Map competencies to observable learning outcomes and suitable activities. Use **ADDIE**, **Bloom's revised taxonomy**, authentic performance scenarios, adult learning concepts and feedback loops where appropriate.

**3. Accessibility and inclusion review** — Examine captions, keyboard access, alternatives and inclusive participation using applicable **WCAG 2.2** success criteria and **UDL 3.0** principles. These are **evaluation references, not a claim of certified compliance**.

**4. AI evaluation scenario design** — Author realistic task prompts; define a locked reference decision before judging responses; document what evidence makes a response defensible.

**5. Evaluation rubric and response comparison** — Apply six human-review dimensions (objective alignment, assessment validity, accessibility, digital delivery, evidence quality, evaluation strategy). The offline script independently checks structured Boolean fixture labels.

**6. Error analysis and feedback** — Identify exact errors/edge cases, severity, unsupported claims, likely learner impact, evidence gaps and practical corrections with a traceable rationale.

**7. Measurement and iteration** — Propose improvements to the case dataset, calibration process and model QA. Actual model comparisons require collecting versioned model outputs and a separately performed human review.

**8. Audit and governance** — Document reviewer disagreements, high-severity learner-impact risks, appropriate approval and correction ownership before real use.

### Skills and expertise

Instructional design; learning experience design (LXD); needs analysis; performance consulting; measurable learning objectives; curriculum architecture; learning activity design; professional case-based learning; business simulations; competency-based assessment; item quality; formative and summative evaluation; accessibility and inclusive learning; WCAG/UDL review concepts; digital learning delivery; LMS/LXP architectural awareness; learning analytics; ADDIE; Bloom; Kirkpatrick; human-centered evaluation; reference answer writing; evaluation rubrics; adversarial/edge-case authoring; AI model response review; evidence verification; failure taxonomy; structured feedback; reviewer calibration; responsible AI in education.

### AI / software / technology

| Technology | Project use | Evidence level |
| --- | --- | --- |
| **Python 3** | Local evaluation and error-detection logic | Executable source code |
| **JSON / JSONL** | Synthetic scenarios, model-output-style fixtures and reference decisions | Included dataset |
| **CSV** | Machine-readable export of findings for audit or spreadsheet analysis | Implemented in script |
| **Python unittest** | Evaluate schema validation and deliberate failure detection | Included tests; execute to verify |
| **Prompt engineering and rubric frameworks** | Definition of expert tasks and reference answers | Written specification |
| **WCAG 2.2, UDL 3.0** | Accessibility and inclusive-design review references | Design methodology, not an audit |
| **ADDIE, Bloom's taxonomy, Kirkpatrick** | Instructional architecture, assessment level and outcome evaluation | Domain-methodology examples |
| **Excel, Power Query, Power BI** | Possible dashboard for exported QA data | Suggested extension; no integration claimed |
| **LMS/LXP, SCORM, xAPI** | Digital-learning metadata and analytics vocabulary | Conceptual architecture |
| **LLM APIs / model comparison** | Optional future actual model-response evaluation | Not integrated; no calls made |

### Deliverables

- [**Expert evaluation dataset**](data/evaluation_cases.jsonl) — eight synthetic educational-design prompts with reference labels, strong and flawed answers, explanatory evidence and corrections.
- [**Python evaluation engine**](evaluate_instructional_design.py) — structured scoring, severity taxonomy and JSON/CSV reporting.
- [**Unit tests**](test_evaluate_instructional_design.py) — test suite for dataset schema, candidate comparisons, deliberate errors and invalid response fields.
- [**Expert review rubric**](EXPERT_RUBRIC.md) — six scored dimensions, 0–2 scale, review process and proposed QA gates.
- [**Technology & methodology**](TECHNOLOGY_AND_METHODOLOGY.md) — skills map, technology boundaries, end-to-end workflow, deliverables and KPIs.

### Run the demonstration

Python 3.10+; no paid accounts, external model API, GPU or external dependencies.

```bash
cd "AI Portfolio/Instructional Design Expert"
python -m unittest -v test_evaluate_instructional_design.py
python evaluate_instructional_design.py
```

Outputs are written locally to `outputs/evaluation_report.json` and `outputs/evaluation_report.csv`. These outputs are excluded from Git version control; they describe authored test cases **not model accuracy**.

### KPI framework — measure rather than invent

**Portfolio fixture checks:** valid structured case count, 6-field schema compliance, match of authored strong answers to reference judgments, detection of injected wrong fields, and unit-test success (only after local execution).

**Proposed KPIs for an actual project, not achieved:** model response accuracy against independently validated expert rubrics; weighted severity rate; critical accessibility error rate; objective/assessment alignment; unsupported claim rate; inter-rater agreement and adjudication turnaround; model-version regression rate; response correction acceptance; instructional quality indicators and actual learning transfer where supported by appropriately collected evidence.

Do **not** equate synthetic fixture correctness with improvements in model reasoning, a paid project or measurable learner outcomes.

### Case study summary

**Business requirement:** Ensure AI-produced instructional recommendations are accurate, defensible, assessable, accessible and digitally deliverable.

**Methodology:** Audience and needs analysis → objective/assessment mapping → synthetic scenario and reference creation → quality scoring rubric → structured response comparison → expert correction → proposed benchmarking and governance.

**Technology:** Python, JSONL, CSV, unit tests, structured expert rubrics, WCAG/UDL guidance, instructional-design evaluation.

**Results:** Version-controlled portfolio dataset and executable QA demonstration, with reporting formats and human-review protocol. No client-specific operational KPI or independently measured model improvement is asserted.

### Technical sources

- [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [CAST — Universal Design for Learning Guidelines 3.0](https://udlguidelines.cast.org/)

[Back to AI Portfolio](../README.md) · [AI model training, expert feedback, and model improvement](../AI%20model%20training%2C%20expert%20feedback%2C%20and%20model%20improvement/)
