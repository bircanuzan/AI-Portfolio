# Game Developer | Godot Gameplay Bug & Feature Evaluation

**Portfolio status:** Independent technical demonstration created for a game-development evaluation task. Not a shipped game, client engagement, or claim of professional AAA/indie development experience.

## Mission
Build a tiny Godot 4 interactive counter scene and create an authentic gameplay defect: a held input accidentally triggers multiple pickups instead of one action per press. The evaluator must identify the defect through on-screen behavior, produce a minimal fix, and demonstrate acceptance.

## Files
- `project.godot` and `main.tscn`: self-contained Godot sample scene.
- `broken_main.gd`: intentionally faulty gameplay logic to replace `main.gd` during the test.
- `main.gd`: reference solution with press-edge detection, cooldown and win-state logic.
- `TASK_AND_ACCEPTANCE.md`: input sequence, expected visuals, verifiable state and bug report template.

## Run
Open this folder as a Godot 4 project, press F6 for the main scene, and tap Space three times. To reproduce the bug, copy `broken_main.gd` to `main.gd` and hold Space. Restore the reference solution for the correct one-action-per-press behavior.

**Limitations:** This is a new self-directed scene-level prototype. Godot editor execution and visual playtesting must be performed by the reviewer; no verified engine-run test footage is included.