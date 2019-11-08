from random import randrange
import lib.constants as constant
from lib.tetrino import Tetrino


class Game:
    def __init__(self, block_size):
        self.screen_size = width, height = 640, 800
        self.block_size = block_size
        self.background_color = 0, 0, 0
        self.score = 0

    def create_random_tetrino(self):
        # Randomize starting location
        location = x, y = randrange(self.screen_size[constant.X] - self.block_size), 0
        # Randomize the shape
        shape = randrange(constant.NUM_SHAPES)
        return Tetrino(location, self.block_size, shape)

    def return_score(self):
        pass

    def check_blocks(self):
        pass