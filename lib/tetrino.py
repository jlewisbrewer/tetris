import lib.constants as constant
from lib.translatable import Translatable

class Tetrino(Translatable):
    def __init__(self, location_offset, shape, num_blocks, t_id):
        self.id = t_id
        self.num_blocks = num_blocks
        # self.block_size = block_size
        self.shape = shape
        self.shape_positions = constant.SHAPES[shape]
        self.shape_index = 0
        self.speed = .25
        self.speed_count = 1
        # This is going to be int offset from numbers on the grid array
        self.location_offset = location_offset
        # This will be a list of 4 or 5 block locations
        self.locations = []
        self.image = 'images/intro_ball.gif'
        self.update_location()
    
    def __str__(self):
        return f'Tetrino {self.id}: {self.locations}\nOffset: {self.location_offset}'

    def speed_up(self):
        if self.speed > 0:
            self.speed -= self.speed_count * .01
            self.speed_count += 1

    def update_location(self):
        # We need to set the current location so we can add to grid.
        shape = self.shape_positions[self.shape_index]
        x_offset = self.location_offset[constant.X]
        # tmp_x = x_offset
        y_offset = self.location_offset[constant.Y]
        block_locations = self.translate_shape(shape, x_offset, y_offset)
        self.locations = block_locations               

    def rotate(self):
        index = self.shape_index
        self.shape_index = (index + 1) % 4
        self.update_location()
    
    def adjust_locations(self, rc):
        self.locations =[[_, y + 1] for [_, y] in self.locations if y < rc]
        print(f'locations after: {self.locations}')
    
    def remove_locations(self, rc, x):
        if [x, rc] in self.locations:
            self.locations = [[_, y] for [_, y] in self.locations if y != rc]