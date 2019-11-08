import sys, pygame
from lib.game import Game
from lib.tetrino import Tetrino
import lib.constants as constant

pygame.init()

size = width, height = 640, 800
speed = [2, 2]
black = 0, 0, 0
MOTION = .25
DESCENT = .1

game = Game(constant.MEDIUM)
print(game.block_size)
screen = pygame.display.set_mode(game.screen_size)

tetrino = game.create_random_tetrino()
x = tetrino.location[constant.X]
y = tetrino.location[constant.Y]
print(x, y)
ball = pygame.image.load(tetrino.image)
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pressed = pygame.key.get_pressed()
    if y < 650:      
        if pressed[pygame.K_DOWN]: y += MOTION
        if pressed[pygame.K_LEFT]: x -= MOTION
        if pressed[pygame.K_RIGHT]: x += MOTION
        y += DESCENT
    



    # ballrect = ballrect.move(speed)
    # if ballrect.left < 0 or ballrect.right > width:
    #     speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > height:
    #     speed[1] = -speed[1]

    screen.fill(game.background_color)
    screen.blit(ball, (x,y))
    pygame.display.flip()