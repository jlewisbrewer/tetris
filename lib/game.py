import sys, pygame
import lib.constants as constant
from random import randrange
from time import time
from lib.tetrino import Tetrino
from lib.game_board import GameBoard
from lib.translatable import Translatable

class Game(Translatable):
    def __init__(self, block_size):
        self.block_size = block_size
        self.screen_size = 10 * self.block_size, 20 * self.block_size
        self.game_board = GameBoard()
        self.background_color = 55, 55, 40
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
            num_blocks, self.tetrino_id, self.block_size)
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
        x_offset = randrange(10 - (max_x - min_x)) - min_x
        y_offset = 0 - min_y
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

    def display_board(self):
        print(self.game_board)

    def calculate_score(self):
        mul = self.check_board()
        if mul > 0:
            inc = 100 * mul + ((mul - 1) * 25)
            self.score += inc

    def check_board(self):
        return self.game_board.check_board(self.tetrino_set)

    def check_game_over(self):
        return self.game_board.check_game_over()

    def run(self):
        new_tetrino = True
        interval = .25
        prev_time = time()
        white = (255, 255, 255)     
        
        pygame.init()
        # # https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
        # font = pygame.font.Font('freesansbold.ttf', self.block_size)

        # text = font.render(f'Total score is {self.score}', True, white)  
        # textRect = text.get_rect()
  
        # # set the center of the rectangular object. 
        # textRect.center = (self.screen_size[0] // 2 , self.screen_size[1] // 2) 
        # #https://stackoverflow.com/questions/43503995/pygame-key-get-pressed-
        # # how-to-add-interval
        screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption('Pygame Tetris')
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()

            if new_tetrino == True:
                end = self.check_game_over()
                if end:
                    # https://www.geeksforgeeks.org/python-display-text-to-
                    # pygame-window/
                    font = pygame.font.Font('freesansbold.ttf', self.block_size)

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
                curr = self.create_random_tetrino()
                new_tetrino = False
                self.update_board()

            pressed = pygame.key.get_pressed()
            left_move, right_move, down_move, rotate_move \
                = self.game_board.check_movement(curr)

            if down_move == False:
                # We're at the bottom
                new_tetrino = True
                self.calculate_score()
                print(f'Score: {self.score}')
            if left_move == True:
                if pressed[pygame.K_LEFT] and time() > prev_time + interval:
                    self.move_tetrino(curr, -1, 0)
                    prev_time = time()
            if right_move == True:
                if pressed[pygame.K_RIGHT] and time() > prev_time + interval:
                    self.move_tetrino(curr, +1, 0)
                    prev_time = time()
            if rotate_move == True:
                if pressed[pygame.K_UP] and time() > prev_time + interval:
                    self.rotate(curr)
                    prev_time = time()
            if down_move == True:    
                if pressed[pygame.K_DOWN] and time() > prev_time + interval or \
                    time() > prev_time + interval:
                    self.move_tetrino(curr, 0, +1)
                    prev_time = time()

            screen.fill(self.background_color)
            self.update_board()

            for _, tetrino in self.tetrino_set.items():
                img = pygame.image.load(tetrino.image)
                for location in tetrino.locations:
                    screen.blit(img, (self.block_size * location[constant.X], 
                            self.block_size * location[constant.Y]))

            pygame.display.flip()