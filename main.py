import sys
import lib.constants as constant
from lib.game import Game
from time import time


try:
    inp = sys.argv[1]
except IndexError:
    print('Must specify game size. Please consult README.')
    sys.exit()

if inp == 'medium':
    size = constant.MEDIUM
if inp == 'large':
    size = constant.LARGE
if inp == 'small':
    size = constant.SMALL

try:
    game = Game(size)
    game.run()
except NameError:
    print('Size not input correctly. Please consult README')
    sys.exit()