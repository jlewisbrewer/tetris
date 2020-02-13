import lib.constants as constant
from lib.tetrino import Tetrino

class GameBoard():
    """
    This class handles logic associated with 2d game grid.
    """
    def __init__(self):
        """
        Constructor function for GameBoard
        """
        self.grid = [[-1 for num in range(10)] for num in range(20)]

    def __str__(self):
        """
        Display function for GameBoard.

        Returns:
            res (string) : A string that displays grid to console
        """
        res = ''
        for row in self.grid:
            for i in row:
                val = i
                if isinstance(i, Tetrino):
                    val = f't{i.id}'
                res += f'{str(val)} '
            res += '\n'
        return res

    def _clear_board(self):
        """
        Resets the game grid.
        """
        self.grid = [[-1 for num in range(10)] for num in range(20)]
    
    def _add_to_board(self, tetrino):
        """
        Adds a tetrino to the game board.

        Parameters:
            tetrino (Tetrino) : a tetrino
        """
        for location in tetrino.locations:
            try:
                self.grid[location[constant.Y]][location[constant.X]] = tetrino
            except IndexError:
                print(f'Loc: {location}')
    
    def check_movement(self, tetrino):
        """
        Checks whether a tetrino can move to a location.

        Parameters:
            tetrino (Tetrino) : a tetrino
        
        Returns:
            left (bool) : whether can move left
            right (bool) : whether can move right
            down (bool) : whether can move down
            rotate (bool) : whether can roate
        """
        left, right, down, rotate = True, True, True, True
        nb = tetrino.num_blocks
        left_array = [False for _ in range(nb)]
        right_array = [False for _ in range(nb)]
        down_array = [False for _ in range(nb)]
        rotate_array = [False for _ in range(nb)]
        locations = tetrino.locations
        new_tetrino = Tetrino(tetrino.location_offset, \
            tetrino.shape, tetrino.num_blocks, tetrino.id, tetrino.game_size)
        new_tetrino.shape_index = tetrino.shape_index
        new_tetrino.rotate()
        
        for i in range(nb):
            try:
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
        if sum(rotate_array) != nb:
            rotate = False

        return left, right, down, rotate
        
    def update_board(self, tetrino_set):
        """
        Adds tetrinos in tetrino set to the board.
        
        Parameters:
            tetrino_set (dict) : a dictionary of tetrinos
        """
        self._clear_board()
        for _, t in tetrino_set.items():
            self._add_to_board(t)

    def check_board(self, tetrino_set):
        """
        Checks the board to see if there are completed rows

        Parameters:
            tetrino_set (dict) : a dictionary of tetrinos
        
        Returns:
            completed_row_count (int) : the number of rows removed
        """
        completed_row_count = 0
        row_count = 0
        for row in self.grid:
            tetrino_count = 0
            for i in row:
                if isinstance(i, Tetrino):
                    tetrino_count += 1
            if tetrino_count is 10:
                competed_row_count += 1
                rel_x = 0
                for tetrino in row:
                    tetrino.remove_locations(row_count, rel_x)
                    rel_x += 1
                self.adjust_locations(row_count, tetrino_set)
            row_count += 1
        return completed_row_count 

    def adjust_locations(self, row_count, tetrino_set):
        """
        Adjusts the locations lists for affected tetrinos in a tetrino set.

        Parameters:
            row_count (int) : The row number used to find what row the affected
                tetrinos are in.
            tetrino_set (dict) : A set of tetrinos
        """
        t_set = set()
        for _, t in tetrino_set.items():
            for [_, y] in t.locations:
                if y < row_count:
                    t_set.add(t)
        for tetrino in t_set:
            tetrino.adjust_locations(row_count)

    def check_game_over(self):
        """
        Checks if there are any tetrinos in the first row. If there are, the
        game ends.

        Returns:
            (bool) : game end state
        """
        for val in self.grid[0]:
            if val is not -1:
                return True
        return False