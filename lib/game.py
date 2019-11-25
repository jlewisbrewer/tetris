from random import randrange
import lib.constants as constant
from lib.tetrino import Tetrino
from lib.game_board import GameBoard

# The screen must be 2:1, 10 blocks wide
class Game:
    def __init__(self, block_size):
        self.block_size = block_size
        self.screen_size = width, height = 10 * self.block_size, 20 * self.block_size
        self.game_board = GameBoard()
        self.background_color = 0, 0, 0
        self.tetrino_set = dict()
        self.tetrino_id = 1
        self.score = 0

    def update_board(self):
        self.game_board.update_board(self.tetrino_set)

    def create_random_tetrino(self):
        # Creates a tetrino and adds it to the dictionary
        # We will put it in a random place on the grid
        # We should find the shape first, and then find the boundaries of the
        # shape to determine the offset.
        location = [randrange(10 - 1), 0]
        # Randomize the shape
        shape = randrange(constant.NUM_SHAPES)
        new_tetrino = Tetrino(self, location, 1, self.tetrino_id)
        self.tetrino_set[self.tetrino_id] = new_tetrino
        self.tetrino_id += 1
        return new_tetrino

    def move_tetrino(self, tetrino, x, y):
        # x and y will be relative positions
        tetrino.location_offset[constant.X] += x
        tetrino.location_offset[constant.Y] += y
        tetrino.update_location()

    def rotate(self, tetrino):
        tetrino.rotate()

    def return_score(self):
        pass

    def check_blocks(self):
        pass