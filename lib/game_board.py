import lib.constants as constant
from lib.tetrino import Tetrino

class GameBoard():
    def __init__(self):
        self.grid = [[-1 for num in range(10)] for num in range(20)]

    def _clear_board(self):
        self.grid = [[-1 for num in range(10)] for num in range(20)]
    
    def _add_to_board(self, tetrino):
        # I think we will have to change this tetrino instances in the future
        for location in tetrino.locations:
            self.grid[location[constant.Y]][location[constant.X]] = tetrino
    
    def check_movement(self, tetrino):
        left, right, down = True, True, True
        left_array = [False for _ in range(4)]
        right_array = [False for _ in range(4)]
        down_array = [False for _ in range(4)]
        locations = tetrino.locations
        # print(locations)
        for i in range(len(locations)):
            curr_x = locations[i][constant.X]
            curr_y = locations[i][constant.Y]
            if curr_x != 0 and (self.grid[curr_y][curr_x -1] == -1 
                or self.grid[curr_y][curr_x - 1] == tetrino):
                left_array[i] = True
            if curr_x != 9 and (self.grid[curr_y][curr_x + 1] == -1 
                or self.grid[curr_y][curr_x + 1] == tetrino):
                right_array[i] = True
            if curr_y != 19 and (self.grid[curr_y + 1][curr_x] == -1 
                or self.grid[curr_y + 1][curr_x] == tetrino):
                down_array[i] = True
        if sum(left_array) != 4:
            left = False
        if sum(right_array) != 4:
            right = False
        if sum(down_array) != 4:
            down = False
        return left, right, down
    
    # def check_location(self, tetrino):
    #     locations = tetrino.locations

    #     for location in locations:
    #         curr_y = location[constant.Y]
    #         if curr_y + 1 == 19 or curr_y
        
    def update_board(self, tetrino_set):
        self._clear_board()
        for t_id, t in tetrino_set.items():
            self._add_to_board(t)