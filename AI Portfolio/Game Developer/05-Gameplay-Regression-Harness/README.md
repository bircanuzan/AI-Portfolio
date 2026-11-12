# Gameplay Regression Test Harness

**Evidence classification:** Independently developed portfolio demonstration based on a **simulated** client/producer inquiry, not commissioned commercial work, a shipped game, or a paid SLA. Acceptance KPIs are targets unless explicitly labeled as measured. Godot editor/visual playtesting has not been verified.

## Client Inquiry
Simulated technical-lead inquiry: repetitive pickup inputs need regression checks that catch hold-to-repeat, score overshoot, and completion-lock defects before scene QA.

## Our Methodology / Tech Used
Implement a deterministic Python 3 TokenGame state model and unittest coverage for a held input over 20 frames, three press/release cycles and ten redundant presses. Retain explicit expected versus actual assertions.

**Technical components:** Python 3 | unittest | deterministic state simulation | edge-trigger input model.

## Result (KPI / SLA / Metrics)
Measured local result (6 Nov 2026): 3/3 Python unittest cases passed, 0 failed, execution reported 0.000s for the tiny model. Acceptance targets: maximum score 3, exactly 1 increment per press edge, and locked completion state. This validates a Python state model only; Godot scene behavior remains unverified. Proposed QA SLA: run the three-case suite on every script change and share findings within 1 business day.

## Evidence and Delivery Status
Published game_state.py and test_game_state.py; tests also reproduced and executed locally with Python unittest on 6 Nov 2026.

## Reproduction / Evaluation
Follow the source files and task acceptance guide in this folder. Capture the input sequence, actual on-screen state, screenshot or screen recording, severity, and pass/fail rationale. Escalate any discrepancy; do not mark simulated targets as achieved.

## Related portfolio
[Game Developer project collection](https://github.com/bircanuzan/AI-in-HR-Portfolio/tree/main/Game%20Developer).
