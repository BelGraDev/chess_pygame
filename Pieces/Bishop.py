from Pieces.Pieces import Pieces
from Utils.Cell_utils import Cell_utils
import pygame

class Bishop(Pieces):
    
    def __init__(self, type: str, board) -> None:

        super().__init__(type, board)
        self.image = pygame.image.load(f"Pieces/images/{type}_bishop.png").convert_alpha()

    def possible_moves(self, cell_name: str) -> list[str]:

        row, column = Cell_utils.map_cell_to_index(cell_name)

        upper_left_diagonal: list[str] = self._check_line(row, column, -1, -1, cell_name)
        upper_right_diagonal: list[str] = self._check_line(row, column, -1, 1, cell_name)

        lower_left_diagonal: list[str] = self._check_line(row, column, 1, -1, cell_name)
        lower_right_diagonal: list[str] = self._check_line(row, column, 1, 1, cell_name)

        possible_moves: list[str] = upper_left_diagonal + upper_right_diagonal + lower_left_diagonal + lower_right_diagonal
        return possible_moves