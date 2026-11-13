# Turkish Language AI Evaluation — Rubric and QA Framework

## Scoring anchors (human-judged)
Score each dimension from **0 to 3**, with a short evidence-based explanation for any score below 3.

| Dimension | 0 — Critical | 1 — Poor | 2 — Acceptable with revision | 3 — Meets standard |
|---|---|---|---|---|
| Instruction alignment | Wrong intent / complete message drift | Material omission or addition | Minor deviation | Fully addresses instruction |
| Coherence / consistency | Internally contradictory or nonsensical | Significant gaps | Mostly coherent | Clear and internally consistent |
| Factuality / groundedness | Fabricated high-impact factual claim | Multiple unsupported details | Some claims need sourcing | All material claims supported or clearly qualified |
| Turkish fluency | Unintelligible language | Many grammatical/naturalness issues | Minor stylistic issues | Natural, grammatical Turkish |
| Cultural nuance / tone | Offensive, severely inappropriate, or clearly wrong context | Register/context mismatch | Minor localization issue | Appropriate register and cultural context |

The scores represent **human annotation judgments**, not automatic model-derived truth. Where evidence is missing, annotate `needs_verification` instead of assuming facts are accurate. Use `visual_attribute_mismatch` only when an image description or trusted metadata has been supplied; do not infer image content from text alone.

## Error taxonomy
- `message_drift`: deviations from user instructions or required message.
- `unsupported_claim`: fabricated claims, incorrect facts, invented attributes or ungrounded details.
- `contradiction`: response conflicts with itself, trusted instructions, or verified context.
- `visual_attribute_mismatch`: textual response contradicts provided visual reference metadata.
- `fluency`: Turkish spelling, grammar, morphology, awkward phrasing or unnatural expressions.
- `tone_cultural_nuance`: culturally inappropriate phrasing, formality, idiom, localization.
- `needs_verification`: material factual claim lacking an accessible reliable source.
- `other`: issue requiring a free-text description.

## Review process
1. Read the Turkish instruction and provided evidence.
2. Review output without assuming intended meaning; cite the specific problematic span.
3. Record dimension scores, errors, severity (`low`, `medium`, `high`, `critical`) and an actionable Turkish or English note.
4. If a factual claim cannot be independently verified, mark `needs_verification` and request evidence.
5. Escalate critical cases, reviewer disagreement or uncertain culturally sensitive material for adjudication.
6. Retest corrected outputs against the same rubric and preserve the change history.

## Proposed QA indicators (targets only)
| KPI | Definition | Illustrative target |
|---|---|---|
| Annotation completeness | Complete required fields / total records | 100% |
| Cross-review agreement | Same issue/no-issue category after paired reviewer checks | >= 90% |
| Critical error escalation | Critical findings routed for review / critical findings | 100% |
| Actionability | Reviewed annotations with specific issue/evidence/fix / reviewed annotations | >= 95% |
| Turnaround time | Time from task receipt to completed human review | Within agreed project SLA |
| Hallucination detection recall | Adjudicated unsupported claims found / all adjudicated unsupported claims | Set after gold dataset calibration |
| Message drift detection precision | True drift flags / all drift flags on adjudicated set | Set after gold dataset calibration |
| Cultural consistency | Passing localized examples / adjudicated sampled examples | Set against approved rubric |

**Evidence and ethics:** Do not claim accuracy against an external model or historical delivery SLAs from synthetic examples. Preserve privacy, account for dialect/register variation, and escalate decisions with real-world impact.
