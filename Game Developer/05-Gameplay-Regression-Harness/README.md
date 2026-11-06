# Gameplay state regression / automated assertion harness

**Evidence:** New independent Godot 4 learning/assessment prototype designed for a micro1-style challenge; NOT professional game-studio delivery or verified engine playtest.

## Objective
Validate representative action sequences in an isolated Python state model: press-edge input, counter limits, completion lock, and boundary cases.

## Reviewer workflow
1. Run python -m unittest discover -s . -p 'test_*.py' -v in this folder.
2. Inspect passing cases and intentionally extend with edge cases.
3. Use this as a reference for manual Godot visual state comparisons.

## Acceptance checks
- A held input increments only once.
- The third deliberate press completes the task.
- Extra presses after completion do not change score.
- Release between presses is required for additional increments.

## Limitations
Python-only state model; it does not exercise Godot scene rendering, input events or engine debugging.
