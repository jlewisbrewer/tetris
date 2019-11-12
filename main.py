import sys, pygame
from lib.game import Game
from lib.tetrino import Tetrino
import lib.constants as constant

pygame.init()

# size = width, height = 1000, 2000
# speed = [2, 2]
black = 0, 0, 0


game = Game(constant.MEDIUM)
screen = pygame.display.set_mode(game.screen_size)
motion = game.screen_size[constant.X]/10000
descent = game.screen_size[constant.Y]/20000

tetrino = game.create_random_tetrino()
# x = tetrino.location[constant.X]
# y = tetrino.location[constant.Y]
locations = tetrino.block_locations[tetrino.shape_index]
x_coors = [loc[constant.X] for loc in locations]
y_coors = [loc[constant.Y] for loc in locations]


y = max(y_coors)
x = min(x_coors)

ball1 = pygame.image.load(tetrino.image)
ball2 = pygame.image.load(tetrino.image)
ball3 = pygame.image.load(tetrino.image)
ball4 = pygame.image.load(tetrino.image)
# ballrect = ball.get_rect()



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    pressed = pygame.key.get_pressed()
    if y < game.screen_size[constant.Y] - game.block_size:      
        if pressed[pygame.K_DOWN]: 
            y_coors = [y + descent for y in y_coors]
            y += descent
        if x <= game.screen_size[constant.X] - game.block_size:
            if pressed[pygame.K_RIGHT]: 
                x_coors = [x + game.block_size for x in x_coors]
                x += game.block_size
        if x >= 0:
            if pressed[pygame.K_LEFT]:
                x_coors = [x - motion for x in x_coors]
                x -= motion
            
        y_coors = [y + descent for y in y_coors]
        y += descent
    



    # ballrect = ballrect.move(speed)
    # if ballrect.left < 0 or ballrect.right > width:
    #     speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > height:
    #     speed[1] = -speed[1]

    screen.fill(game.background_color)
    screen.blit(ball1, (x_coors[0], y_coors[0]))
    screen.blit(ball2, (x_coors[1], y_coors[1]))
    screen.blit(ball3, (x_coors[2], y_coors[2]))
    screen.blit(ball4, (x_coors[3], y_coors[3]))

    pygame.display.flip()