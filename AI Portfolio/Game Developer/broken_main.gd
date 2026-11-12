extends Node2D

const TARGET: int = 3
var token_count: int = 0
@onready var status_label: Label = $Status

func _ready() -> void:
    status_label.text = "Tokens 0/3"

func _process(_delta: float) -> void:
    # BUG: a held key is counted every rendered frame.
    if Input.is_action_pressed("ui_accept"):
        token_count += 1
        status_label.text = "Tokens %d/3" % token_count
