from __future__ import annotations
from typing import TYPE_CHECKING, NamedTuple
from dataclasses import dataclass, field
from Utils.Cell_utils import is_cell_empty, are_teammates
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

    def _move_type(self) -> MoveType:

        if is_cell_empty(self.step.end_cell, self.board):
            return MoveType.EMPTY_CELL
        
        elif are_teammates(self.step.start_cell, self.step.end_cell, self.board):
            return MoveType.TEAMMATE
        else:
            return MoveType.CAPTURE
