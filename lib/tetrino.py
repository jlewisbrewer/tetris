import lib.constants as constant
from lib.translatable import Translatable

class Tetrino(Translatable):
    """
    This is a class that handles actions on the Tetris shapes.
    
    Attributes:
        id (int) : Id of the tetrino
        num_blocks (int) : the number of blocks in the tetrino (either 4 or 5)
        game_size (int) : the size of the game (small, medium, large)
        shape (int) : index of the shape
        shape_positions (list) : the various shapes when rotated, a list of 
            binary numbers
        shape_index (int) : the index of the shape position that the tetrino
            is currently in
        speed (float) : speed of the block (deprecated)
        speed_count (int) : an int that controls the speed (deprecated)
        location_offset (int, int) : offset of the shape on the 2d grid
        locations (list) : a list of coords for the tetrino blocks
        color (string) : color of the block
        image (string) : file location of the block image
    """

    def __init__(self, location_offset, shape, num_blocks, t_id, game_size):
        """
        The constructor for the Tetrino class.

        Parameters:
            location_offset (int, int) : offset of the shape on the 2d grid
            shape (int) : index of the tetrino shape 
            num_blocks (int) : the numebr of tetrino blocks
            t_id (int) : id of the tetrino
            game_size (int) : the size of the tetrino blocks (small, medium,
                or large)
        """
        self.id = t_id
        self.num_blocks = num_blocks
        self.game_size = game_size
        self.shape = shape
        self.shape_positions = constant.SHAPES[shape]
        self.shape_index = 0
        self.speed = .25
        self.speed_count = 1
        # This is going to be int offset from numbers on the grid array
        self.location_offset = location_offset
        # This will be a list of 4 or 5 block locations
        self.locations = []
        self.color = constant.COLORS[shape]
        self.image = self._get_image()
        self.update_location()
    
    def __str__(self):
        """
        The string representation of the Tetrino class. Displays id, locations
        of the Tetrino blocks, and the offsets.
        """
        return f'Tetrino {self.id}: {self.locations}\nOffset: {self.location_offset}'

    def _get_image(self):
        """
        Constructs the string for the image files.

        Returns:
            f (string) : a file string for the image files
        """

        f = constant.IMGFILE
        if self.game_size == 10:
            f += '/small/'
        if self.game_size == 25:
            f += '/medium/'
        if self.game_size == 50:
            f += '/large/'
        f += f'{self.color}.png'
        return f

    def speed_up(self):
        """
        Speeds up the Tetrino (deprecated)
        """

        if self.speed > 0:
            self.speed -= self.speed_count * .01
            self.speed_count += 1

    def update_location(self):
        """
        Updates all the locations of the Tetrino blocks.
        """

        shape = self.shape_positions[self.shape_index]
        x_offset = self.location_offset[constant.X]
        y_offset = self.location_offset[constant.Y]
        block_locations = self.translate_shape(shape, x_offset, y_offset)
        self.locations = block_locations               

    def rotate(self):
        """
        Rotates the Tetrino shape.
        """

        index = self.shape_index
        self.shape_index = (index + 1) % 4
        self.update_location()
    
    def adjust_locations(self, rc):
        """
        Shifts locations down on the grid. Called whenever a row on the 2d grid
        is removed. This function will adjust all y coordinates.

        Parameters:
            rc (int) : the row of the grid that was removed.
        """

        self.locations =[[_, y + 1] for [_, y] in self.locations if y < rc]
    
    def remove_locations(self, rc, x):
        """
        Removes Tetrino locations if they are taken off the game board.
        
        Parameters:
            rc (int) : the row of the grid that was removed
            x (int) : the x coord that will be removed
        """
        
        if [x, rc] in self.locations:
            self.locations = [[_, y] for [_, y] in self.locations if y != rc]