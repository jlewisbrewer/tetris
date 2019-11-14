import lib.constants as constant


class Tetrino:
    def __init__(self, game, location_offset, shape, t_id):
        self.id = t_id
        self.block_size = game.block_size
        self.shape_positions = constant.SHAPES[shape]
        self.shape_index = 0
        self.speed = .25
        self.speed_count = 1
        # This is going to be int offset from numbers on the grid array
        self.location_offset = location_offset
        # This will be a list of 4 block locations
        self.locations = []
        self.image = 'images/intro_ball.gif'

        self.update_location()
        # self.set_locations()


    def speed_up(self):
        if self.speed > 0:
            self.speed -= self.speed_count * .01
            self.speed_count += 1

    def update_location(self):
        # We need to set the current location so we can add to grid.
        shape = self.shape_positions[self.shape_index]
        block_locations = []
        x_offset = self.location_offset[constant.X]
        tmp_x = x_offset
        y_offset = self.location_offset[constant.Y]
        binary_number = '{0:016b}'.format(shape)
        for i in range(len(binary_number)):
            if i % 4 == 0:
                y_offset += 1
                tmp_x = x_offset
            if binary_number[i] == '1':
                coords = [tmp_x, y_offset]
                block_locations.append(coords)
            tmp_x += 1
        self.locations = block_locations



    # def set_locations(self):
    #     # Interprets the locations into a graphic
    #     for number in self.shape_positions:
    #         locations = []
    #         y_offset = 0
    #         x_offset = 0
    #         binary_number = '{0:016b}'.format(number)
    #         for i in range(len(binary_number)):
    #             if i % 4 == 0:
    #                 y_offset += self.block_size
    #                 x_offset = 0
    #             x_offset += self.block_size
    #             if binary_number[i] == '1':
    #                 coordinates = (self.location[constant.X] + x_offset,
    #                         self.location[constant.Y] + y_offset)
    #                 locations.append(coordinates)
    #         self.block_locations.append(locations)                

    def rotate(self):
        pass