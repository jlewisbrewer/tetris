import lib.constants as constant


class Tetrino:
    def __init__(self, location, block_size, shape):
        self.block_size = block_size
        self.shape_positions = constant.SHAPES[shape]
        self.shape_index = 0
        self.speed = .25
        self.speed_count = 1
        self.location = location
        self.image = 'images/intro_ball.gif'


    def speed_up(self):
        if self.speed > 0:
            self.speed -= self.speed_count * .01
            self.speed_count += 1
        
    def rotate(self):
        pass