extends Node
const REQUIRED_GEMS := 3
var gems := {}
var door_open := false
@onready var status_label: Label = $Status

func collect_gem(gem_id: int) -> void:
    if not gems.has(gem_id):
        gems[gem_id] = true
    refresh_status()

func open_door() -> bool:
    if gems.size() >= REQUIRED_GEMS:
        door_open = true
    refresh_status()
    return door_open

func refresh_status() -> void:
    status_label.text = "Gems %d/%d | Door %s" % [gems.size(), REQUIRED_GEMS, "OPEN" if door_open else "LOCKED"]
