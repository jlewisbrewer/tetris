class Translatable:
    def translate_shape(self, shape, x_offset, y_offset):
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