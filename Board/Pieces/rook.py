from Board.Pieces import Piece
from Utils.Cell_utils import map_cell_to_index
import pygame

class Rook(Piece):
    
    def __init__(self, type: str, board) -> None:

        super().__init__(type, board)
        self.image = pygame.image.load(f"{self.image_path}{type}_rook.png").convert_alpha()

    def possible_moves(self, cell_name: str) -> list[str]:

        row, column = map_cell_to_index(cell_name)

        upwards_check: list[str] = self._check_line(row, column, -1, 0, cell_name)
        downwards_check: list[str] = self._check_line(row, column, 1, 0, cell_name)

        leftwards_check: list[str] = self._check_line(row, column, 0, -1, cell_name)
        rightwards_check: list[str] = self._check_line(row, column, 0, 1, cell_name)

        possible_moves: list[str] = upwards_check + downwards_check + leftwards_check + rightwards_check
        return possible_moves

