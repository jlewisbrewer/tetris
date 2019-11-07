from random import randrange

class Tetrino:
    def __init__(self, game_size):
        self.size = 10
        self.speed = .25
        self.speed_count = 1
        self.x = randrange(game_size[0] - self.size)
        self.y = game_size[1]
        self.image = 'images/intro_ball.gif'

    def speed_up(self):
        if self.speed > 0:
            self.speed -= self.speed_count * .01
            self.speed_count += 1
        
    def rotate(self):
        pass