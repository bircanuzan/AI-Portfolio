# Watch the Agent Work — authentic demonstration recording plan

**Video status:** not yet recorded. This is a reproducible scene-by-scene script, not a link to an imaginary MP4.

## Recording outline (2–4 minutes)
**Scene 1 — identity and version (15s):** show repo commit, agent version and read-only scope; explain all data are fictional.

**Scene 2 — six-tool orchestration (45s):** terminal from the project directory:

    python cli.py executive_brief --entity ALL

Show six tool sections: recruitment funnel, employer brand, HC operations, talent, total rewards and workforce intelligence; highlight evidence sections and zero write actions.

**Scene 3 — reward privacy (25s):**

    python cli.py total_rewards --entity CORP

Explain minimum cohort size and explicitly fictional market reference; never show individuals.

**Scene 4 — authentication tests (35s):** run unittest security/API checks; demonstrate unauthenticated HTTP request failing 401 and analyst role denied rewards (403). Use only disposable demo credentials.

**Scene 5 — audit integrity (20s):** demonstrate test detecting a modified SQLite event signature; HMAC key is withheld from screen.

**Scene 6 — benchmark (30s):**

    python scripts/benchmark.py

Show real pass/fail and local in-process runtime results, **not** fabricated production numbers. Read the limitations aloud.

**Scene 7 — sovereign and deployment gaps (25s):** show a model interface and operator-managed HTTPS settings without any live secret; disclose no G42 environment, enterprise deployment or measurable commercial outcome.

## Real recording evidence checklist
Capture full terminal timestamps and exact Git SHA, agent version, commands, unedited results, redacted logs, scenario runner output, machine conditions and signer/author. Do not put actual employee data or credentials on screen.

For G42 consideration, a separate **real production** demo, independent technical validation and enterprise sponsor permissions would still be required.
