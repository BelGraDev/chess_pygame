from abc import ABC, abstractmethod
from Utils.Cell_utils import Cell_utils
from Board.Move import MoveType
from Board.Move import Move
import pygame

class Pieces(ABC, pygame.Rect):

    def __init__(self, type, board) -> None:
        self.type = type
        self.board = board
        self.has_moved = False
        
    def is_next_possible(self, prev_cell_name: str, row: int, col: int) -> int | None:

        try:
            self.board.cells[row, col]

            next_cell_name = Cell_utils.map_index_to_cell(row, col)
            move = Move(self.board, prev_cell_name, next_cell_name)

            match move.type:
                case MoveType.EMPTY_CELL | MoveType.CAPTURE:
                    return move
                case _:
                    return None
        except IndexError:
            return None
        
    def _check_line(self, start_row: int, start_col: int, step_row: int, step_col: int, current_cell_name: str) -> list:

        possible_moves = []
        current_row = start_row + step_row
        current_col = start_col + step_col

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
    def possible_moves(self, cell_name: str) -> list:
        pass

