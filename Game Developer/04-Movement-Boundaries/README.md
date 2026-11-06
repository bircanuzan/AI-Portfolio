# Player movement / boundary defect challenge

**Evidence:** New independent Godot 4 learning/assessment prototype designed for a micro1-style challenge; NOT professional game-studio delivery or verified engine playtest.

## Objective
Create a deterministic movement controller that clamps a character within world boundaries rather than allowing out-of-bounds drift.

## Reviewer workflow
1. Attach player.gd to a Node2D with player visuals.
2. Use ui_left/right/up/down actions to move.
3. Hold directional input toward each border.
4. Verify position and corner behavior under different delta values.

## Acceptance checks
- Character x remains between 0 and 800.
- Character y remains between 0 and 450.
- Movement uses frame delta, not raw per-frame increments.
- Diagonal movement uses normalized direction to avoid unintended speedup.

## Limitations
Standalone movement script; Godot editor/run testing and scene collision integration remain future work.
