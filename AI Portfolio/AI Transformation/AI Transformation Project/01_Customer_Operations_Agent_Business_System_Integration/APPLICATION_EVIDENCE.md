# myAlfred application questions — accurate project evidence

**Q1 — Personally built an AI agent, AI automation or AI-powered workflow? YES for automation.**
I built the Python customer-operations workflow that performs case ingestion, document checks, exceptions, follow-up drafting, human approval routing and auditing. The executed offline case logic is rules-based, NOT a live generative-AI agent; an optional LLM draft adapter is coded but untested with a real model.

**Q2 — Integrated AI/automation with API, CRM, database, spreadsheet, email or business system? YES for local integrations, not enterprise production.**
CSV spreadsheet-like source -> SQLite relational database -> HTTP/JSON local API -> .eml email draft. Actual API integration and database writes are exercised in repeatable tests. I have NOT connected to a real insurer, CRM, cloud service or email provider and have NOT sent an email.

**Q3 — GitHub portfolio/project demonstrating AI building? YES.**
Executable project, tests, CI, architecture documentation and an end-to-end demo. Specific evidence: the workflow tests assert SQLite records, HTTP authorization, missing-document detection, EML generation, human signoff, expired-policy escalation and no automated send.

**Suggested form phrasing:** "Yes — I personally built and tested a Python business workflow integrating CSV, SQLite, a localhost HTTP API and email-draft generation. It is a synthetic portfolio prototype with mandatory human approval; live enterprise CRM/LLM integration is not claimed."

**Important:** If a recruiter explicitly asks whether you integrated a *live LLM* with a real production CRM or API, the truthful answer is no based solely on this project.
