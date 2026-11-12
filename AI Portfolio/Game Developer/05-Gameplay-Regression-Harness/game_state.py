class TokenGame:
    def __init__(self, target=3):
        self.target = target
        self.count = 0
        self._last_pressed = False

    def advance(self, pressed):
        if pressed and not self._last_pressed and self.count < self.target:
            self.count += 1
        self._last_pressed = bool(pressed)
        return self.count

    @property
    def complete(self):
        return self.count >= self.target
