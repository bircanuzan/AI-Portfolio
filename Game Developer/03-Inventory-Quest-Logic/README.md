# Inventory and quest state consistency

**Evidence:** New independent Godot 4 learning/assessment prototype designed for a micro1-style challenge; NOT professional game-studio delivery or verified engine playtest.

## Objective
Build a two-system interaction: collect exactly three gems, unlock a door once, and reject duplicate pickups.

## Reviewer workflow
1. Attach quest.gd to a Node and create a Label child named Status.
2. Trigger collect_gem with gem identifiers 101, 102 and 103 from a scene or test harness.
3. Repeat gem 101 to test duplicate prevention.
4. Try open_door before and after collecting all three gems.

## Acceptance checks
- Duplicate gem identifiers do not increment the inventory.
- Door remains closed until 3 unique gems have been collected.
- Door opening is idempotent after achievement.
- Status text reflects unique count and door state.

## Limitations
Logic-only GDScript sample; no art assets, UI scene, integration harness or engine-run proof.
