class Translatable:
    """
    This is a class that functions as a prototype to enable
    daughter classes to convert binary numbers into tetrino 
    shapes
    """
    def translate_shape(self, shape, x_offset, y_offset):
        """
        The function to transform binary number into locations
        on a 2d grid

        Parameters:
            shape (int) : a index that references constants.SHAPES list
            x_offset (int) : x coord for placing shape on 2d grid
            y_offset (int) : y coord for placing shape on 2d grid
        
        Returns:
            block_locations (list) : a list of coordinates for tetrino blocks
                into the requisite shape
        """
        block_locations = []
        tmp_x = x_offset
        binary_number = '{0:016b}'.format(shape)
        for i in range(len(binary_number)):
            if i % 4 == 0 and i != 0:
                y_offset += 1
                tmp_x = x_offset
            if binary_number[i] == '1':
                coords = [tmp_x, y_offset]
                block_locations.append(coords)
            tmp_x += 1
        return block_locations