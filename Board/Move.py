from __future__ import annotations
from typing import TYPE_CHECKING, NamedTuple
from dataclasses import dataclass, field
from Utils.Cell_utils import is_cell_empty, are_teammates,is_cell_centered, is_cell_advanced
from enum import Enum

if TYPE_CHECKING:
    from .BoardStatus import BoardStatus

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


class Step(NamedTuple):
    start_cell: str
    end_cell: str


@dataclass
class Move:
    board: BoardStatus
    step: Step
    type: MoveType = field(init=False)


    def __post_init__(self) -> None:
        self.type = self._move_type()
        self.move_cost = self._calculate_move_cost()


    def _move_type(self) -> MoveType:
        if is_cell_empty(self.step.end_cell, self.board):
            return MoveType.EMPTY_CELL
        elif are_teammates(self.step.start_cell, self.step.end_cell, self.board):
            return MoveType.TEAMMATE
        else:
            return MoveType.CAPTURE
    

    def _calculate_move_cost(self) -> int:
        move_cost = int(is_cell_centered(self.step.end_cell))
        move_cost += 2 if is_cell_advanced(self.step.end_cell, self.board) else 0
        if self.type == MoveType.CAPTURE:
            piece = self.board[self.step.end_cell]
            move_cost += piece.value
        return move_cost
