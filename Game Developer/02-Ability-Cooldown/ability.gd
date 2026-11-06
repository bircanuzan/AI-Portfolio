extends Node2D
const COOLDOWN_SECONDS := 2.0
var time_left := 0.0
var activated_count := 0
@onready var status_label: Label = $Status

func _process(delta: float) -> void:
    time_left = maxf(0.0, time_left - delta)
    if Input.is_action_just_pressed("ui_accept") and time_left <= 0.0:
        activated_count += 1
        time_left = COOLDOWN_SECONDS
    status_label.text = "Activations %d | %s" % [activated_count, "READY" if time_left == 0.0 else "COOLDOWN"]
