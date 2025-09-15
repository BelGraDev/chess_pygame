from Pieces.Pieces import Pieces
from Utils.Cell_utils import Cell_utils
import pygame

class Rook(Pieces):
    
    def __init__(self, type, board) -> None:

        super().__init__(type, board)
        self.image = pygame.image.load(f"Pieces/images/{type}_rook.png").convert_alpha()

    def possible_moves(self, cell_name: str) -> list[str]:

        row, column = Cell_utils.map_cell_to_index(cell_name)

        upwards_check: list[str] = self._check_line(row, column, -1, 0, cell_name)
        downwards_check: list[str] = self._check_line(row, column, 1, 0, cell_name)

        leftwards_check: list[str] = self._check_line(row, column, 0, -1, cell_name)
        rightwards_check: list[str] = self._check_line(row, column, 0, 1, cell_name)

        possible_moves: list[str] = upwards_check + downwards_check + leftwards_check + rightwards_check
        return possible_moves

