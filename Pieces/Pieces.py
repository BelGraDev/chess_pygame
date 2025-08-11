from abc import ABC, abstractmethod
from Board.Cell_utils import Cell_utils
from Board.MoveType import MoveType
import pygame

class Pieces(ABC, pygame.Rect):

    def __init__(self, cell, type, board) -> None:
        self.cell = cell
        self.type = type
        self.board = board
        self.has_moved = False
        

    def is_next_possible(self, prev_cell_name, row, col):

        try:
            print(f"row: {row}, column: {col}")
            self.board.cells[row, col]
            next_cell_name = Cell_utils.map_index_to_cell(row, col)
            move = self.board.in_next_cell(prev_cell_name, next_cell_name)

            match move:
                case MoveType.EMPTY_CELL | MoveType.CAPTURE:
                    return next_cell_name
                case _:
                    return None
        except IndexError:
            print("Index error")
            return None
        

            
    @abstractmethod
    def possible_moves(self, cell_name) -> list:
        pass
    