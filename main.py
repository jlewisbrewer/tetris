import sys, pygame
import lib.constants as constant
from lib.game import Game
from time import time


game = Game(constant.MEDIUM)
new_tetrino = True
interval = .25
prev_time = time()


#https://stackoverflow.com/questions/43503995/pygame-key-get-pressed-how-to-add-interval

# Need to convert the game grid into pygame
screen = pygame.display.set_mode(game.screen_size)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if new_tetrino == True:
        curr = game.create_random_tetrino()
        new_tetrino = False
        game.update_board()

    pressed = pygame.key.get_pressed()
    left_move, right_move, down_move, rotate_move \
         = game.game_board.check_movement(curr)

    if down_move == False:
        # We're at the bottom
        new_tetrino = True

    if left_move == True:
        if pressed[pygame.K_LEFT] and time() > prev_time + interval:
            game.move_tetrino(curr, -1, 0)
            prev_time = time()
    if right_move == True:
        if pressed[pygame.K_RIGHT] and time() > prev_time + interval:
            game.move_tetrino(curr, +1, 0)
            prev_time = time()
    if rotate_move == True:
        if pressed[pygame.K_UP] and time() > prev_time + interval:
            print('pressed up')
            print(curr.locations)
            curr.rotate()
            print(curr.locations)
            prev_time = time()


    if down_move == True:    
        if pressed[pygame.K_DOWN] and time() > prev_time + interval or \
            time() > prev_time + interval:
            game.move_tetrino(curr, 0, +1)
            prev_time = time()

    screen.fill(game.background_color)
    
    for _, tetrino in game.tetrino_set.items():
        img = pygame.image.load(tetrino.image)
        for location in tetrino.locations:
            screen.blit(img, (game.block_size * location[constant.X], 
                    game.block_size * location[constant.Y]))


    pygame.display.flip()