import unittest
from random import randrange
from lib.tetrino import Tetrino
from lib.game import Game
import lib.constants as constant

class TestTetrino(unittest.TestCase):
    def setUp(self):
        self.game = Game(constant.SMALL)
        rand_location = [randrange(10 - 1), -1]
        set_location = [2, 3]
        shape = 0
        t_id = 0
        self.tetrino1 = Tetrino(self.game, rand_location, shape, t_id)
        self.tetrino2 = Tetrino(self.game, rand_location, shape, t_id + 1)
        self.tetrino3 = Tetrino(self.game, set_location, shape, t_id + 2)
        self.tetrino4 = Tetrino(self.game, set_location, shape + 1, t_id + 3)

    def test_initial_position(self):
        self.assertTrue(self.tetrino1.location_offset[constant.X] 
            <= self.game.screen_size[constant.X] and 
            self.tetrino1.location_offset[constant.X] >= 0)

    def test_update_location(self):
        # location = [2, 3]
        # # Square shape
        # shape = 0
        # tetrino = Tetrino(self.game, location, shape, 0)
        self.tetrino3.update_location()
        self.assertEqual(self.tetrino3.locations[0], [2, 3])
        self.assertEqual(self.tetrino3.locations[1], [3, 3])
        self.assertEqual(self.tetrino3.locations[2], [2, 4])
        self.assertEqual(self.tetrino3.locations[3], [3, 4])
        self.assertTrue(len(self.tetrino3.locations) == 4)
        self.tetrino3.rotate()
        self.assertTrue(len(self.tetrino3.locations) == 4)

    def test_speed_up(self):
        self.assertEqual(self.tetrino1.speed, self.tetrino2.speed)
        self.tetrino2.speed_up()
        self.assertTrue(self.tetrino1.speed > self.tetrino2.speed)
        self.assertTrue(self.tetrino1.speed_count != self.tetrino2.speed_count)

    def test_rotate(self):
        prev = self.tetrino4.locations
        self.tetrino4.rotate()
        self.assertTrue(prev != self.tetrino4.locations)
        self.assertTrue(self.tetrino4.shape_index >= 0)
        self.assertTrue(self.tetrino4.shape_index < 4)
        


if __name__ == '__main__':
    unittest.main()

