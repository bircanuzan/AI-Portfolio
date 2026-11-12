extends Node2D

const TARGET: int = 3
var token_count: int = 0
var finished: bool = false
@onready var status_label: Label = $Status

func _ready() -> void:
    update_display()

func _process(_delta: float) -> void:
    if finished:
        return
    if Input.is_action_just_pressed("ui_accept"):
        token_count += 1
        if token_count >= TARGET:
            finished = true
        update_display()

func update_display() -> void:
    if finished:
        status_label.text = "SUCCESS: 3/3 tokens collected"
    else:
        status_label.text = "Tokens %d/%d - press Space once per token" % [token_count, TARGET]
