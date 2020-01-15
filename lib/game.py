from random import randrange
import lib.constants as constant
from lib.tetrino import Tetrino
from lib.game_board import GameBoard
from lib.translatable import Translatable

# The screen must be 2:1, 10 blocks wide
class Game(Translatable):
    def __init__(self, block_size):
        self.block_size = block_size
        self.screen_size = 10 * self.block_size, 20 * self.block_size
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
        shape_index = randrange(constant.NUM_SHAPES)
        shape = constant.SHAPES[shape_index]
        shape_locations = self.translate_shape(shape[0], 0, 0)
        num_blocks = len(shape_locations)
        location = self.create_random_offsets(shape_locations)
        # Randomize the shape
        new_tetrino = Tetrino(location, shape_index, \
            num_blocks, self.tetrino_id)
        self.tetrino_set[self.tetrino_id] = new_tetrino
        self.tetrino_id += 1
        return new_tetrino

    def move_tetrino(self, tetrino, x, y):
        # x and y will be relative positions
        tetrino.location_offset[constant.X] += x
        tetrino.location_offset[constant.Y] += y
        tetrino.update_location()
    
    def create_random_offsets(self, block_locations):
        # We can use the block locations to tell us the initial state of the x
        # and y offsets. For instance, a square is flush in the upper left 
        # quadrant, so the x offset can be between 0 and 8.
        min_x, max_x, min_y, _ = self.find_minimum_coords(block_locations)
        print(f'Min x: {min_x}')
        print(f'Max x: {max_x}')
        x_offset = randrange(10 - (max_x - min_x)) - min_x
        y_offset = 0 - min_y
        print(f'X offset: {x_offset}')
        print(f'Y offset:{y_offset}')
        return [x_offset, y_offset]

    def find_minimum_coords(self, block_locations):
        min_x, max_x, min_y, max_y = self.block_size, 0, self.block_size, 0
        for coord in block_locations:
            x = coord[constant.X]
            y = coord[constant.Y]
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y
        return min_x, max_x, min_y, max_y

    def rotate(self, tetrino):
        tetrino.rotate()

    def return_score(self):
        pass

    def check_blocks(self):
        pass