import numpy as np

class GridMap:
    """
    GridMap class

    Convention: top left cell is (0,0), immediate right is (1,0). Cell index is 0 == (0,0), 1 == (1,0).
    """

    def __init__(self, width, height, resolution, center_x, center_y, init_val=0):
        """__init__

        :param width: number of grid for width
        :param height: number of grid for heigth
        :param resolution: grid resolution [m]
        :param center_x: center x position  [m]
        :param center_y: center y position [m]
        :param init_val: initial value for all grid
        """
        self.width = width
        self.height = height
        self.resolution = resolution
        self.center_x = center_x
        self.center_y = center_y

        self.top_left_x = self.center_x - self.width / 2.0 * self.resolution
        self.top_left_y = self.center_y + self.height / 2.0 * self.resolution

        self.ndata = self.width * self.height
        self.data = [init_val] * self.ndata

    def get_cell_from_xy_pos(self, x_pos, y_pos):
        """
        :param x_pos: UAV local x position in m
        :param y_pos: UAV local y position in m
        :out cell_index: UAV cell index
        """
        num_cols = int(np.floor((x_pos - self.top_left_x) / self.resolution))
        num_rows = int(np.floor(np.abs((y_pos - self.top_left_y) / self.resolution)))
        cell_index = num_rows*self.width + num_cols

        if cell_index<0 or cell_index>=self.ndata:
            return None
        else: 
            return cell_index
    
    def get_value_from_xy_pos(self, x_pos, y_pos):
        cell_index = self.get_cell_from_xy_pos(x_pos, y_pos)
        return self.data[cell_index]
    
    def get_xy_pos_from_xy_index(self, x_index, y_index):
        x_pos = self.top_left_x + self.resolution/2 + x_index*self.resolution
        y_pos = self.top_left_y - (self.resolution/2 + y_index*self.resolution)
        return (x_pos, y_pos)
    
    def set_cell_visited(self, cell_index):
        self.data[cell_index] = 1


    
