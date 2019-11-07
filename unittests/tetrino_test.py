import unittest
from classes.tetrino import Tetrino
from classes.game import Game

class TestTetrino(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.tetrino1 = Tetrino(self.game.size)
        self.tetrino2 = Tetrino(self.game.size)

    def test_initial_position(self):
        self.assertTrue(self.tetrino1.x <= self.game.size[1] and self.tetrino1.x >= 0)
    
    def test_speed_up(self):
        self.assertEqual(self.tetrino1.speed, self.tetrino2.speed)
        self.tetrino2.speed_up()
        self.assertTrue(self.tetrino1.speed > self.tetrino2.speed)
        self.assertTrue(self.tetrino1.speed_count != self.tetrino2.speed_count)



if __name__ == '__main__':
    unittest.main()

