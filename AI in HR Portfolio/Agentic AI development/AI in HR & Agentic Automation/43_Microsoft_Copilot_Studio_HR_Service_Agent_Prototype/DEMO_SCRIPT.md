# Recruiter-friendly demo — what is real vs next

## Local demonstration (already supported)
1. Run `python3 -m http.server 8000` from this folder and open `http://localhost:8000/` or open `index.html` directly in a browser.
2. Enter `What is the annual leave policy?`. Show the versioned sample-policy citation and on-screen trace.
3. Enter `What's my remaining leave balance?`. Show `HUMAN_ESCALATION` and the privacy boundary.
4. Enter `I need an employment confirmation letter.`. Show `APPROVAL_REQUIRED`. **No approval is sent**.
5. Enter `Can I have my holiday quota?` and explain why the missed synonym is recorded as an evaluation failure, not hidden.
6. Open [test evidence](evidence/2026-10-29_test_run.json) to show actual outputs and failed cases.

## Recommended screen captures when recording the demo
Capture from the **actual running local browser**: (a) cited FAQ answer; (b) restricted request escalation; (c) letter approval status; (d) evaluation results. Do not use invented Copilot Studio screenshots. No screenshots are claimed as captured in the present commit.

## Career claim (safe wording)
> Built and tested a local HR policy service prototype with 28 documented prompt tests, sample-policy citation, risk routing and a reproducible decision scorecard; defined a Microsoft Copilot Studio / Power Automate implementation path with human-approval gates. Working on live Microsoft tenant validation.

Do **not** claim deployed Copilot Studio, Microsoft certification, enterprise security validation or measured savings.
