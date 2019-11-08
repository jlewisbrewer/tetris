import unittest
from lib.tetrino import Tetrino
from lib.game import Game
import lib.constants as constant

class TestTetrino(unittest.TestCase):
    def setUp(self):
        self.game = Game(constant.SMALL)
        location = 0, 0
        shape = 0
        self.tetrino1 = Tetrino(self.game.screen_size, location, shape)
        self.tetrino2 = Tetrino(self.game.screen_size, location, shape)

    def test_initial_position(self):
        self.assertTrue(self.tetrino1.location[constant.X] 
            <= self.game.screen_size[constant.Y] and 
            self.tetrino1.location[constant.X] >= 0)
    
    def test_speed_up(self):
        self.assertEqual(self.tetrino1.speed, self.tetrino2.speed)
        self.tetrino2.speed_up()
        self.assertTrue(self.tetrino1.speed > self.tetrino2.speed)
        self.assertTrue(self.tetrino1.speed_count != self.tetrino2.speed_count)



if __name__ == '__main__':
    unittest.main()

