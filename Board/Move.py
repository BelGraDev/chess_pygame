from Utils.Cell_utils import Cell_utils
from enum import Enum

class MoveType(Enum):

    NOT_AVAILABLE = -1
    EMPTY_CELL = 0
    CAPTURE = 1
    TEAMMATE = 2

class Move:

    def __init__(self, board, prev_cell_name, next_cell_name):
        self.board = board
        self.prev_cell = prev_cell_name
        self.next_cell = next_cell_name
        self.type = self._move_type(prev_cell_name, next_cell_name)

    def _move_type(self, prev_cell_name, next_cell_name) -> int:

        if Cell_utils.is_cell_empty(next_cell_name, self.board):
            return MoveType.EMPTY_CELL
        
        elif Cell_utils.are_teammates(prev_cell_name, next_cell_name, self.board):
            return MoveType.TEAMMATE
        else:
            return MoveType.CAPTURE
