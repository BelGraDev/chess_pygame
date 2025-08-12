from Pieces.Pieces import Pieces
from Board.Cell_utils import Cell_utils
import pygame

class Rook(Pieces):
    
    def __init__(self, cell, type, board) -> None:

        super().__init__(cell, type, board)
        self.image = pygame.image.load(f"Pieces/images/{type}_rook.png")

    def possible_moves(self, cell_name) -> list:

        row, column = Cell_utils.map_cell_to_index(cell_name)

        possible_moves = []

        upwards_check = self._check_line(row, column, -1, 0, cell_name)
        downwards_check = self._check_line(row, column, 1, 0, cell_name)

        leftwards_check = self._check_line(row, column, 0, -1, cell_name)
        rightwards_check = self._check_line(row, column, 0, 1, cell_name)

        possible_moves = upwards_check + downwards_check + leftwards_check + rightwards_check
        return possible_moves

