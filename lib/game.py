import sys, pygame
import lib.constants as constant
from random import randrange
from time import time
from lib.tetrino import Tetrino
from lib.game_board import GameBoard
from lib.translatable import Translatable

class Game(Translatable):
    """
    This is a class that controls the game logic.

    Attributes:
        game_size (int) : the size of game (small, medium, large)
        screen_size (int, int) : the width and length of the game screen
        game_board (GameBoard) : class for handling game grid information
        background_color (int, int, int) : rgb settings for screen
        tetrino_set (dict) : dictionary of tetrinos
        tetrino_id (int) : initial tetrino id
        score (int) : game score
    """

    def __init__(self, game_size):
        """
        This is a constructor class for the game.

        Parameters:
            game_size (int) : the size of the game
        """

        self.game_size = game_size
        self.screen_size = 10 * self.game_size, 20 * self.game_size
        self.game_board = GameBoard()
        self.background_color = 55, 55, 40
        self.tetrino_set = dict()
        self.tetrino_id = 1
        self.score = 0

    def _update_board(self):
        """
        Calls update board function for the GameBoard class
        """

        self.game_board.update_board(self.tetrino_set)

    def _create_random_tetrino(self):
        """
        Creates a tetrino and adds it to the dictionary

        Returns:
            new_tetrino (Tetrino) : a new tetrino
        """
        shape_index = randrange(constant.NUM_SHAPES)
        shape = constant.SHAPES[shape_index]
        shape_locations = self.translate_shape(shape[0], 0, 0)
        num_blocks = len(shape_locations)
        location = self._create_random_offsets(shape_locations)
        new_tetrino = Tetrino(location, shape_index, \
            num_blocks, self.tetrino_id, self.game_size)
        self.tetrino_set[self.tetrino_id] = new_tetrino
        self.tetrino_id += 1
        return new_tetrino

    def _move_tetrino(self, tetrino, x, y):
        """
        Moves a tetrino by updating Tetrino class location offsets.
        The tetrino class will then update all the locations for the blocks.

        Parameters:
            tetrino (Tetrino) : a tetrino
            x (int) : a relative x position
            y (int) : a relative y position
        """
        tetrino.location_offset[constant.X] += x
        tetrino.location_offset[constant.Y] += y
        tetrino.update_location()
    
    def _create_random_offsets(self, block_locations):
        """
        This creates a random offset for deciding where to drop a shape.
        We can use the block locations to tell us the initial state of the x
        and y offsets. For instance, a square is flush in the upper left 
        quadrant, so the x offset can be between 0 and 8.

        Parameters:
            block_locations (list) : a list of a tetrinos coordinates

        Returns:
            (list) : the x offset and y offset
        """

        min_x, max_x, min_y, _ = self._find_min_and_max_coords(block_locations)
        x_offset = randrange(10 - (max_x - min_x)) - min_x
        y_offset = 0 - min_y
        return [x_offset, y_offset]

    def _find_min_and_max_coords(self, block_locations):
        """
        Finds the min and max numbers in a given coordinate list.

        Parameters:
            block_locations (list) : a list of tetrino coordinates
        
        Returns:
            min_x (int) : min x
            max_x (int) : max x
            min_y (int) : min y
            max_y (int) : max y
        """
        min_x, max_x, min_y, max_y = self.game_size, 0, self.game_size, 0
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

    def _rotate(self, tetrino):
        """
        Calls rotate function for the Tetrino class.
        """
        tetrino.rotate()

    def _calculate_score(self):
        """
        Calculates the total score.
        """
        mul = self._check_board()
        if mul > 0:
            inc = 100 * mul + ((mul - 1) * 25)
            self.score += inc

    def _check_board(self):
        """
        Calls check_board function for GameBoard class
        """
        return self.game_board.check_board(self.tetrino_set)

    def _check_game_over(self):
        """
        Calls check_game_over function for GameBoard class.
        """
        return self.game_board.check_game_over()

    def display_board(self):
        """
        Prints a game board to console.
        """
        print(self.game_board)

    def run(self):
        """
        Runs the game. Contains pygame function logic.
        """
        new_tetrino = True
        interval = .25
        prev_time = time()
        white = (255, 255, 255)     
        
        pygame.init()

        screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption('Pygame Tetris')
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()

            if new_tetrino == True:
                end = self._check_game_over()
                if end:
                    # https://www.geeksforgeeks.org/python-display-text-to-
                    # pygame-window/
                    font = pygame.font.Font('freesansbold.ttf', self.game_size)

                    text = font.render(f'Total score is {self.score}', True, 
                        white)  
                    textRect = text.get_rect()
            
                    # set the center of the rectangular object. 
                    textRect.center = (self.screen_size[0] // 2 , 
                        self.screen_size[1] // 2)
                    while True:
                        screen.blit(text, textRect)
                        for event in pygame.event.get() : 
                            if event.type == pygame.QUIT : 
                                pygame.quit() 
                                sys.exit()
                        pygame.display.update()
                curr = self._create_random_tetrino()
                new_tetrino = False
                self._update_board()

            pressed = pygame.key.get_pressed()
            left_move, right_move, down_move, rotate_move \
                = self.game_board.check_movement(curr)

            if down_move == False:
                # We're at the bottom
                new_tetrino = True
                self._calculate_score()
                print(f'Score: {self.score}')
            if left_move == True:
                if pressed[pygame.K_LEFT] and time() > prev_time + interval:
                    self._move_tetrino(curr, -1, 0)
                    prev_time = time()
            if right_move == True:
                if pressed[pygame.K_RIGHT] and time() > prev_time + interval:
                    self._move_tetrino(curr, +1, 0)
                    prev_time = time()
            if rotate_move == True:
                if pressed[pygame.K_UP] and time() > prev_time + interval:
                    self._rotate(curr)
                    prev_time = time()
            if down_move == True:    
                if pressed[pygame.K_DOWN] and time() > prev_time + interval or \
                    time() > prev_time + interval:
                    self._move_tetrino(curr, 0, +1)
                    prev_time = time()

            screen.fill(self.background_color)
            self._update_board()

            for _, tetrino in self.tetrino_set.items():
                img = pygame.image.load(tetrino.image)
                for location in tetrino.locations:
                    screen.blit(img, (self.game_size * location[constant.X], 
                            self.game_size * location[constant.Y]))

            pygame.display.flip()