# Gameplay ability cooldown / state handling

**Evidence:** New independent Godot 4 learning/assessment prototype designed for a micro1-style challenge; NOT professional game-studio delivery or verified engine playtest.

## Objective
Implement a cooldown-bound ability: activate on a single button press, ignore subsequent requests during cooldown, then restore availability.

## Reviewer workflow
1. Attach ability.gd to a Godot 4 Node2D instance.
2. Map ui_accept to Space (Godot defaults are usually configured).
3. Run test scene with Label node named Status.
4. Compare cooldown behavior against acceptance checks.

## Acceptance checks
- Initial state READY; first press switches to COOLING DOWN.
- Holding Space never causes repeated activations.
- Pressing during cooldown does not trigger activation.
- After 2 seconds, ability returns to READY; can activate again.

## Limitations
GDScript script + task specification, no verified end-to-end playtest recorded.
