import lib.constants as constant


class Tetrino:
    def __init__(self, location, block_size, shape):
        self.block_size = block_size
        self.shape_positions = constant.SHAPES[shape]
        self.shape_index = 0
        self.speed = .25
        self.speed_count = 1
        self.location = location
        self.block_locations = []
        self.image = 'images/intro_ball.gif'

        self.set_locations()


    def speed_up(self):
        if self.speed > 0:
            self.speed -= self.speed_count * .01
            self.speed_count += 1
    
    def set_locations(self):
        # Interprets the locations into a graphic
        for number in self.shape_positions:
            locations = []
            y_offset = 0
            x_offset = 0
            binary_number = '{0:016b}'.format(number)
            for i in range(len(binary_number)):
                if i % 4 == 0:
                    y_offset += self.block_size
                    x_offset = 0
                x_offset += self.block_size
                if binary_number[i] == '1':
                    coordinates = (self.location[constant.X] + x_offset,
                            self.location[constant.Y] + y_offset)
                    locations.append(coordinates)
            self.block_locations.append(locations)                

    def rotate(self):
        pass