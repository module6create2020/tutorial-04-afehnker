class KeyboardHandler:
    def __init__(self):
        self.pressed = set()

    def get_key_pressed(self, key):
        return key in self.pressed

    def key_pressed(self, key):
        self.pressed.add(key)

    def key_released(self, key):
        self.pressed.remove(key)
