# Evaluation evidence and demo instructions

Testable offline functions: role criteria normalization, whole-word/alias keyword checks, required/preferred weighting, negative test for `JavaScript != Java`, 0–4 human rubric, timezone-correct `.ics`, duplicate candidate rejection, consent gate, pipeline tasks, activity records and active-record deletion.

Run `python -m pytest -q` and record the actual outcome; never advertise a test as run until verified. These are deterministic unit/integration tests, **not** measured fairness/psychometric validation or tested hiring outcomes.

## Suggested 10-minute demonstration (synthetic data only)

1. Create **AI-enabled Talent Intelligence Consultant** with essentials `recruitment, stakeholder management, excel` and preferred `python, power bi, workday`.
2. Upload `sample_data/synthetic_cv.txt`, enter fictional email `aisha@example.test`, acknowledge synthetic permission and save.
3. Show keyword evidence snippets and any missing mentions; explain that the coverage indicator is not candidate fit.
4. Enter a human assessment of `Stakeholder engagement` (0–4) with a factual fictional example and assessor `Demo Reviewer`.
5. Move the candidate from **New** to **Review**, add a manual task, generate but do not send an invitation and download a tentative calendar file.
6. Export an audit CSV, then erase the fictional candidate and verify the active records are gone.

## Pre-commercial acceptance criteria (not yet met)

- Client-approved, role-relevant assessment rubrics and no misleading language about verified skills.
- De-identified sample sets that cover sparse CVs, aliases, multilingual resumes, PDFs with no text, duplicated records, injected content and fairness concerns.
- Auth, least-privilege, tenant boundaries, encryption, retention, incident response and security review.
- Human approval logs, integrated but disabled-by-default sending, quality monitoring, fault handling and rollback.
