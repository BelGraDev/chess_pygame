import numpy as np
from typing import NamedTuple

class Position(NamedTuple):
    row: int
    col: int
    
class BoardCells:
    def __init__(self, row: int, col: int):
        self.cells = np.zeros((row, col))

    def __getitem__(self, index: tuple[int, int]):
        row, col = index
        if row < 0 or col < 0:
            raise IndexError("Not possible to access negative instances on the board")
        return self.cells[index]