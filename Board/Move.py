from Board.Cell_utils import Cell_utils
from enum import Enum

class MoveType(Enum):

    NOT_AVAILABLE = -1
    EMPTY_CELL = 0
    CAPTURE = 1
    TEAMMATE = 2

class Move:

    def __init__(self, cell, type):
        self.next_cell = cell
        self.type = type

    def move_type(self, prev_cell, next_cell) -> int:

        if Cell_utils.is_cell_empty(next_cell, self):
            return MoveType.EMPTY_CELL
        
        elif Cell_utils.is_white_piece(next_cell, self) != Cell_utils.is_white_piece(prev_cell, self):
            return MoveType.CAPTURE
        
        return MoveType.TEAMMATE