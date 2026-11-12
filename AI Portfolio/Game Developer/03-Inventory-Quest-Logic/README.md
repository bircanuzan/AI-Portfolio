# Inventory and Quest State Logic

**Evidence classification:** Independently developed portfolio demonstration based on a **simulated** client/producer inquiry, not commissioned commercial work, a shipped game, or a paid SLA. Acceptance KPIs are targets unless explicitly labeled as measured. Godot editor/visual playtesting has not been verified.

## Client Inquiry
Simulated game-design inquiry: duplicate pickup events must not count toward a quest, and a locked door must only open after collecting required unique gems.

## Our Methodology / Tech Used
Model a unique-ID inventory in GDScript, gate door state using >=3 distinct IDs, expose collect_gem and open_door functions, and define manual state-transition cases for duplicate and early-open attempts.

**Technical components:** Godot | GDScript | Node | Dictionary state | Label.

## Result (KPI / SLA / Metrics)
Acceptance KPI targets: 3 distinct pickups required; 0 duplicate credits; 0 premature door unlocks when fewer than 3 distinct gems exist. Godot integration and playtest remain pending. Proposed QA SLA: document event log and expected/actual states within 1 business day after verification.

## Evidence and Delivery Status
GDScript quest.gd plus detailed reviewer test flow; source code is a prototype, not a production quest system.

## Reproduction / Evaluation
Follow the source files and task acceptance guide in this folder. Capture the input sequence, actual on-screen state, screenshot or screen recording, severity, and pass/fail rationale. Escalate any discrepancy; do not mark simulated targets as achieved.

## Related portfolio
[Game Developer project collection](https://github.com/bircanuzan/AI-in-HR-Portfolio/tree/main/Game%20Developer).
