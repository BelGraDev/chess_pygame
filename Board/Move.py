from Board.Cell_utils import Cell_utils
from enum import Enum

class MoveType(Enum):

    EMPTY_CELL = 0
    CAPTURE = 1
    TEAMMATE = 2

class Move:

    def __init__(self, board, prev_cell, next_cell):
        self.board = board
        self.prev_cell = prev_cell
        self.next_cell = next_cell
        self.type = self._move_type(prev_cell, next_cell)

    def _move_type(self, prev_cell, next_cell) -> int:

        if Cell_utils.is_cell_empty(next_cell, self.board):
            return MoveType.EMPTY_CELL
        
        elif Cell_utils.is_white_piece(next_cell, self.board) != Cell_utils.is_white_piece(prev_cell, self.board):
            return MoveType.CAPTURE
        
        return MoveType.TEAMMATE