import numpy as np
class Board_cells:
    def __init__(self, row, col):
        self.cells = np.zeros((row, col))

    def __getitem__(self, index):
        
        if isinstance(index, tuple):
            row, col = index
            if row < 0 or col < 0:
                raise IndexError("Not possible to access negative instances on the board")
        
        return self.cells[index]