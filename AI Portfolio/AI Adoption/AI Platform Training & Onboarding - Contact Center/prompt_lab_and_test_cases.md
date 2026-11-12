# AI Image/Video Prompt Lab — Scripts and Expected QA

**Important:** Prompts below are test inputs and expected outcomes; no AI provider was executed for this repository. Do not present them as actual model responses.

## Test 1 — Clear image prompt
**Task:** Create fictional 16:9 customer-support help graphic for package-status education.

```text
Create a clean 16:9 vector-style illustration for a fictional help-center article titled 'How to check a parcel status'. Show an abstract package icon, a generic laptop with a blank tracking interface, and a three-stage progress motif. Use navy, white and teal. No text inside the illustration, no brand marks, no realistic people, no customer names, no personal data. High readability, generous whitespace, suitable for accessible help content.
```

**Expected acceptance:** right canvas and composition, no hallucinated UI text/brand, readable steps and appropriate contrast. **Potential defects:** illegible pseudo-text, inconsistent icon geometry, unapproved branding. **Reviewer:** facilitator + brand owner.

## Test 2 — Weak-to-strong prompt revision
Weak: `Make a realistic client support poster with a happy customer.`
Rewrite: define fictional audience, permitted style, intended outcome, aspect ratio, exclusions, consistency constraints and acceptance criteria. Compare weak and revised prompts; assess controllability, not aesthetic preference.

## Test 3 — Video storyboard (15 seconds)
**Goal:** Explain generic issue escalation without real contact-center data.
- Shot A 0–3s: fictional support icon, static establishing composition.
- Shot B 3–7s: simple sequence of generic issue indicators, no real UI.
- Shot C 7–11s: a human reviewer checks an issue card.
- Shot D 11–15s: approved resolution path, simple transition.
**Continuity prompt template:** Maintain identical icon style, lighting/palette, camera perspective and abstract layout across all four shots; no text generation, no trademarks, no identifiable individuals; 16:9 framing, smooth low-motion transitions.
**Expected checks:** consistent visual identity, no temporal warping or unsafe reveal, appropriate length, readable motion and approved audio/caption plan.

## Test 4 — Reference image policy
Reference is a **self-produced fictional graphic** supplied with explicit rights. Ask learner to identify reference provenance, disclosure/consent, copyrighted marks and disallowed human likeness before use. Block any confidential client image.

## Test 5 — Unsuccessful generation
Simulated issue: the tool produces inconsistent colors across successive renders. Capture request, parameter settings, tool version, non-sensitive output artifact and attempts. Retry with fixed palette/reference settings; after agreed retry threshold escalate to technical owner. Never invent model error codes.

## Exercise submission log
`scenario_id, platform/version, prompt, references/rights, safety checks, expected, actual, pass/fail, operator, reviewer, timestamp`. Actual outputs should remain blank until a real authorized test is performed.

## Practical tool validation (future)
For Runway/Firefly/Canva or equivalent: independently confirm export, aspect ratio, edit/refine controls, image/video mode, reference rules, prompt moderation, accessibility supports and commercial-use policies before claiming competency.
