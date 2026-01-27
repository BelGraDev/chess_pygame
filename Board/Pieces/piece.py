from __future__ import annotations
from abc import ABC, abstractmethod
from Utils.Cell_utils import map_index_to_cell
from Board.Move import MoveType, Move, Step
from Board.boardCells import Position
from pygame import Rect, Surface
from typing import TYPE_CHECKING
from enum import IntEnum

if TYPE_CHECKING:
    from Board.BoardStatus import BoardStatus

class PieceValue(IntEnum):
    PAWN = 1
    KNIGHT = BISHOP = 3
    ROOK = 5
    QUEEN = 9
    KING = 0

class Piece(ABC, Rect):

    image: Surface
    value: PieceValue
    def __init__(self, type: str, board: BoardStatus) -> None:
        self.type = type
        self.board = board
        self.has_moved = False
        self.image_path = "Board/Pieces/images/"


    def is_next_possible(self, prev_cell_name: str, row: int, col: int) -> Move | None:

        try:
            self.board.cells[row, col]

            next_cell_name = map_index_to_cell(row, col)
            step = Step(prev_cell_name, next_cell_name)
            move = Move(self.board, step)

            match move.type:
                case MoveType.EMPTY_CELL | MoveType.CAPTURE:
                    return move
                case _:
                    return None
        except IndexError:
            return None
        
    def _check_line(self, start: Position, step: Position, current_cell_name: str) -> list[str]:

        possible_moves: list[str] = []
        current_row = start.row + step.row
        current_col = start.col + step.col

        while 0 <= current_row < self.board.num_rows and 0 <= current_col < self.board.num_col:
            move = self.is_next_possible(current_cell_name, current_row, current_col)
            if move:
                possible_moves.append(move.step.end_cell)
                if move.type == MoveType.CAPTURE:
                    break
            else:
                break
            current_row += step.row
            current_col += step.col

        return possible_moves
        
    @abstractmethod
    def possible_moves(self, cell_name: str) -> list[str]:
        pass

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(type={self.type!r})'

    def __repr__(self) -> str:
        return self.__str__()

