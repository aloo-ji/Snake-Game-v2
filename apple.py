import random
from config import Config

class Apple():
    def __init__(self):
        self.apple_position = random.randrange(Config['game']['bumper_size'], Config['game']['width'] - Config['game']['bumper_size'] - Config['apple']['width'] + 1, 10), random.randrange(Config['game']['bumper_size'], Config['game']['height'] - Config['game']['bumper_size'] - Config['apple']['height'] + 1, 10)
        self.apple_spawn = True

    def get_apple_position(self):
        return self.apple_position

    def get_apple_spawn(self):
        return self.apple_spawn