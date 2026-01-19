from __future__ import annotations
from typing import TYPE_CHECKING
from Utils.Cell_utils import is_cell_empty, are_teammates
from enum import Enum

if TYPE_CHECKING:
    from Pieces import Piece

class MoveType(Enum):
    TIE = -3
    CHECK_MATE = -2
    NOT_AVAILABLE = -1
    EMPTY_CELL = 0
    CAPTURE = 1
    TEAMMATE = 2
    CASTLE = 3
    PAWN_ASCENSION = 4
    PASSANT_PAWN = 5

class Move:

    def __init__(self, board: dict[str, Piece], prev_cell_name: str, next_cell_name: str) -> None:
        self.board = board
        self.prev_cell = prev_cell_name
        self.next_cell = next_cell_name
        self.type = self._move_type(prev_cell_name, next_cell_name)

    def _move_type(self, prev_cell_name: str, next_cell_name: str) -> MoveType:

        if is_cell_empty(next_cell_name, self.board):
            return MoveType.EMPTY_CELL
        
        elif are_teammates(prev_cell_name, next_cell_name, self.board):
            return MoveType.TEAMMATE
        else:
            return MoveType.CAPTURE
