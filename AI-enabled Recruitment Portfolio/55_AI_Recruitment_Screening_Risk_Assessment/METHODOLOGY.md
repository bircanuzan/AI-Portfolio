# Assessment design — 16 metamorphic paired tests + risk register

## Hypothetical client problem
An employer wants to adopt a ranking tool for CV screening but lacks transparent proof that it responds consistently to job-relevant evidence and does not reject qualified people based on incidental document or personal-signal changes.

## Test method
- A fictional deterministic ranker serves as the **system under test**; no actual ATS, LLM or vendor model is invoked.
- 16 paired synthetic profiles = **32 profile variants**; in each pair exactly one input field changes.
- **13** pairs vary non-job-related inputs (format, gap, name-token placeholder, keyword frequency, optional profile fields, typography/volunteering). Expected decision = **stable**.
- **3** pairs vary job-relevant skills, work sample or an explicitly required fictional licence. A decision change is permitted.
- Compare a deliberately flawed score (which penalises irrelevant fields) against a simplified controlled reference score (skills/work sample/required licence only).
- A **decision flip** means ADVANCE becomes REVIEW or vice versa. REVIEWS are not automatic rejections.
- Count unjustified flips on expected-stable pairs, inspect all mismatches, and propose remediation.

## Important limitations
The token "B" is an **abstract fabricated non-job identifier**, not a statement of nationality, gender or any protected class. Metamorphic stability is one QA control only; it is **not** fairness/disparate-impact measurement or legal compliance certification. A real assessment would need transparent job analysis, datasets with appropriate legal/privacy basis, valid sample design, subgroup analysis where lawful and justified, qualified independent review and appeal/redress.

## Risk process
The 14-item register covers accessibility and format, breaks, proxy use, skills validation, document relevance, transparency, privacy/retention, appeal, monitoring and supplier governance. Severity is an *illustrative proposed category*. A real organization must approve likelihood/impact scoring and control owners.

## Release criteria
**HOLD** the flawed mock if any irrelevant-feature decision changes remain. The controlled reference illustrates a remediation concept but is **not approved for production** without external and job-specific validation.
