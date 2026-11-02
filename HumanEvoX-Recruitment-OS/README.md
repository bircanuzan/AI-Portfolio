# HumanEvoX Recruitment OS — local-first functional pilot

**Status:** Source-validated, auditable single-user demonstration. Core Python logic and data-flow tests passed; the Streamlit graphical interface could not be launched in the isolated build environment because the package was not available. Runtime installation is required on a computer with package access. This is an original implementation separate from the browser-local [HumanEvoX Talent Workspace pilot](https://humanevox-talent-workspace.bircandxb.chatgpt.site). **Not** a production SaaS or a validated recruitment assessment. No payment, AI phone calls, email sending, ATS integration, live LLM, client deployment or protected multi-tenant database is claimed.

## Features

| Module | Working pilot capability | Explicit limitation |
|---|---|---|
| Resume screening | PDF/DOCX/TXT extraction, role requirements, aliases, evidence snippets, gaps, 0–100 keyword-coverage indicator | Does not infer skills or make suitability decisions; scanned PDFs need OCR |
| Candidate assessment | Human-entered 0–4 rubric ratings, evidence notes, assessor trail | No psychometric validity or autonomous assessment |
| Workflow | SQLite roles/candidates, per-role duplicate email detection, manual stages, due-date tasks, audit events | No ATS connection or automatic follow-ups |
| Communications | Draft-only invitation and follow-up emails, tentative `.ics` interviews, optional human-led conversation guide | No email sending, calls, dialing, recording or speech AI |
| Governance | Consent/lawful-basis acknowledgement, CSV formula protection, minimized CV storage, erasure, exports | Not a substitute for UAE PDPL/privacy counsel, access control or penetration testing |

**Important:** `coverage_percent` represents *the fraction of required/preferred keywords mentioned in an uploaded document*, weighted 70/30 when both groups exist. It must never be presented as a verified skill, competence, hiring probability or candidate fit score. Use independent, job-related human review; do not auto-reject based on it.

## Quick start

Requirements: Python 3.11+.

```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
streamlit run app.py
```

Open the local URL shown by Streamlit (usually `http://localhost:8501`). The SQLite database lives outside this folder at `~/.humanevox_recruitment_os/workspace.sqlite3`; override with `HUMANEVOX_DB=/path/to/workspace.sqlite3`. Use `sample_data/synthetic_cv.txt` and create a role with `recruitment, stakeholder management, excel` essentials and `python, power bi, workday` preferences. The dataset is fictional.

Load a fictional record set using `python demo_seed.py`. Re-running the command will not duplicate the sample.

For Windows, you can double-click `START_WINDOWS.bat` after installing Python; it creates a local environment and starts the app on `127.0.0.1` (first use needs internet to install dependencies).

Tests:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

## Data model / workflow

`Role -> Candidate -> Document keyword evidence -> Human competency assessment -> Manual pipeline stage -> Task / communication draft / tentative interview -> CSV reporting -> Audit and erasure`.

Stored: name, email, role, document filename, short matched snippets, coverage summary, consent checkbox, recruiter notes, ratings and log. **Full extracted CV text is not persisted** by default; original uploads are parsed in memory. SQLite writes are parameterized. Exports are downloaded by the operator, not transmitted to external services. No network AI services or email connectors are called.

## Production readiness gaps

Do **not** publicly host with live CVs yet. Before any client/personal-data use: set up secure authentication, role-based access, isolated client tenants, encrypted data and backups, secret management, consent/legitimate-interest process and privacy notices, retention scheduling, defensible audit controls, access logging, recruitment fairness/accuracy evaluation, deletion propagation, integrations and load/security testing. Consult applicable UAE privacy law and clients' rules. See `SECURITY.md`.

## Roadmap

1. Add SSO, protected backend API, private object storage, tenant separation, audited retention controls.
2. Build opt-in Microsoft 365/Google Workspace email/calendar drafts requiring explicit send approval.
3. Add document-grounded AI extraction and evaluations **only** with approved privacy and signed contracts; retain human assessment.
4. Add client dashboards and paid SaaS licensing after real-world security validation.
5. Live AI voice calling is **not** in this build and would require separate explicit approval and lawful notice/consent.

HumanEvoX brand: black `#000`, gold `#C6A052`, white `#FFF`, Inter.
