# Expert review rubric — instructional design and learning experience quality

This guide is for **human judgment** of actual AI-generated educational recommendations. The local Python harness only checks authored Boolean fixtures. It does not automatically grade pedagogy or verify accessibility conformance.

## Scoring (0–2 each, total /12)

| Dimension | 0 — Inadequate | 1 — Partial | 2 — Meets expert standards |
|---|---|---|---|
| Objective and activity alignment | No measurable objective or activity mismatch | Partial alignment, vague evidence | Observable objective; relevant guided practice, feedback and transfer |
| Assessment validity | Recall used for applied skill; no rubric | Some authentic evidence but weak scoring | Appropriate knowledge/skills assessment mapped to objective; transparent criteria |
| Accessibility and inclusion | Unaddressed exclusion, e.g. mouse-only, missing relevant captions | Alternatives mentioned but unverified | Known accessibility needs explicitly considered; documented validation plan |
| Digital learning delivery | Unrealistic platform/access assumptions | Suitable with omissions | Mobile, bandwidth, interaction, privacy and support considerations appropriate to context |
| Evidence / pedagogical reasoning | Unsupported absolute claims or invented research | Limited citations / assumptions | Evidence traceability, appropriate uncertainty and justified choice |
| Evaluation and improvement | Completion presented as proof of skills | Measures reaction/knowledge only | Appropriate learning and job-performance measures; analysis and refinement plan |

**Review sequence:** Identify learning objectives, audience and constraints → assess response's plan → compare with reference and professional guidance → annotate concrete errors and evidence gaps → assign six rubric scores → propose a corrected recommendation → second-review high-severity cases → adjudicate reviewer disagreement → produce a versioned evaluation record.

## Failure taxonomy

- Objective / assessment mismatch
- Invalid competency evidence
- Unsupported pedagogical or scientific claims
- Accessibility barriers: captioning, keyboard use, alternatives, readability
- Unusable mobile / bandwidth / LMS assumptions
- Unjustified inference from completion or satisfaction to workplace improvement
- Hallucinated standards, unverified legal requirements, inequitable assessment

## Review process and sample release criteria (targets only)

- Target at least 95% of scenarios with traceable rationale and clear scoring anchors.
- Require zero unresolved **critical** safety/accessibility findings before a proposed release gate.
- Set a target of ≥85% agreement between independent reviewers on major severity; measure on real dual-reviewed data.
- Require assessment validity and accessibility checks for every relevant use case.
- Treat above as proposed acceptance gates, **not achieved KPIs**.

## Standards and references to consult

- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) — relevant accessible web content success criteria, including prerecorded captions and keyboard operability. Conformance is not claimed by this project.
- [CAST Universal Design for Learning Guidelines 3.0](https://udlguidelines.cast.org/) — planning engagement, representation, and action/expression options.
- Bloom's revised taxonomy — choosing objectives/assessment tasks at the right cognitive level.
- ADDIE — analysis, design, development, implementation, evaluation (iterative instructional workflow).
- Kirkpatrick Four Levels — distinguish reaction, learning, behavior and results; do not interpret completion alone as behavior change.
- SCORM / xAPI, LMS/LXP learning analytics — architectural concepts for future reporting; no LMS integration is implemented.

All design decisions require context-specific expert review; frameworks are *tools* rather than proof of learning outcomes.
