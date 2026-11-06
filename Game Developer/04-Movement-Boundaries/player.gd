extends Node2D
@export var move_speed := 220.0
const MIN_X := 0.0
const MAX_X := 800.0
const MIN_Y := 0.0
const MAX_Y := 450.0

func _process(delta: float) -> void:
    var movement := Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
    position += movement * move_speed * delta
    position.x = clampf(position.x, MIN_X, MAX_X)
    position.y = clampf(position.y, MIN_Y, MAX_Y)
