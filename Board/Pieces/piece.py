from __future__ import annotations
from abc import ABC, abstractmethod
from Utils.Cell_utils import map_index_to_cell
from Board.Move import MoveType, Move
from pygame import Rect
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Board.BoardStatus import BoardStatus

class Piece(ABC, Rect):

    def __init__(self, type: str, board: BoardStatus) -> None:
        self.type = type
        self.board = board
        self.has_moved = False
        self.image_path = "Board/Pieces/images/"

    def is_next_possible(self, prev_cell_name: str, row: int, col: int) -> Move | None:

        try:
            self.board.cells[row, col]

            next_cell_name = map_index_to_cell(row, col)
            move = Move(self.board.board, prev_cell_name, next_cell_name)

            match move.type:
                case MoveType.EMPTY_CELL | MoveType.CAPTURE:
                    return move
                case _:
                    return None
        except IndexError:
            return None
        
    def _check_line(self, start_row: int, start_col: int, step_row: int, step_col: int, current_cell_name: str) -> list[str]:

        possible_moves: list[str] = []
        current_row: int = start_row + step_row
        current_col: int = start_col + step_col

        while (current_row < 8 and current_col < 8) and (current_row >= 0 and current_col >= 0):
            move = self.is_next_possible(current_cell_name, current_row, current_col)
            if move:
                possible_moves.append(move.next_cell)
                if move.type == MoveType.CAPTURE:
                    break
            else:
                break
            current_row += step_row
            current_col += step_col

        return possible_moves
        
    @abstractmethod
    def possible_moves(self, cell_name: str) -> list[str]:
        pass

