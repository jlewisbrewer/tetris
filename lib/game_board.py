import lib.constants as constant
from lib.tetrino import Tetrino

class GameBoard():
    def __init__(self):
        self.grid = [[-1 for num in range(10)] for num in range(20)]

    def _clear_board(self):
        self.grid = [[-1 for num in range(10)] for num in range(20)]
    
    def _add_to_board(self, tetrino):
        for location in tetrino.locations:
            try:
                self.grid[location[constant.Y]][location[constant.X]] = tetrino
            except IndexError:
                print(f'Loc: {location}')
    
    def check_movement(self, tetrino):
        left, right, down, rotate = True, True, True, True
        nb = tetrino.num_blocks
        left_array = [False for _ in range(nb)]
        right_array = [False for _ in range(nb)]
        down_array = [False for _ in range(nb)]
        rotate_array = [False for _ in range(nb)]
        locations = tetrino.locations
        # new_shape = (tetrino.shape_index + 1) % 4
        new_tetrino = Tetrino(tetrino.location_offset, \
            tetrino.shape, tetrino.num_blocks, tetrino.id)
        new_tetrino.rotate()
        print(new_tetrino)
        for i in range(nb):
            curr_x = locations[i][constant.X]
            curr_y = locations[i][constant.Y]
            if curr_x != 0 and (self.grid[curr_y][curr_x -1] == -1 \
                or self.grid[curr_y][curr_x - 1] == tetrino):
                left_array[i] = True
            if curr_x != 9 and (self.grid[curr_y][curr_x + 1] == -1 \
                or self.grid[curr_y][curr_x + 1] == tetrino):
                right_array[i] = True
            if curr_y != 19 and (self.grid[curr_y + 1][curr_x] == -1 \
                or self.grid[curr_y + 1][curr_x] == tetrino):
                down_array[i] = True
            
            try:
                new_x = new_tetrino.locations[i][constant.X]
                new_y = new_tetrino.locations[i][constant.Y]
                grid_val = self.grid[new_y][new_x]
                if new_x >= 0 and new_x <= 9 and new_y >= 0 and new_y <= 19:
                    if grid_val == -1 or grid_val == tetrino:
                        rotate_array[i] = True

            except IndexError:
                continue

        if sum(left_array) != nb:
            left = False
        if sum(right_array) != nb:
            right = False
        if sum(down_array) != nb:
            down = False
        # Keep it as true for now
        if sum(rotate_array) != nb:
            rotate = False

        return left, right, down, rotate
        
    def update_board(self, tetrino_set):
        self._clear_board()
        for _, t in tetrino_set.items():
            self._add_to_board(t)