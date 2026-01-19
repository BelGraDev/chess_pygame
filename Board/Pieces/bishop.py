from Board.Pieces import Piece
from Utils.Cell_utils import map_cell_to_index
import pygame

class Bishop(Piece):
    
    def __init__(self, type: str, board) -> None:

        super().__init__(type, board)
        self.image = pygame.image.load(f"{self.image_path}{type}_bishop.png").convert_alpha()

    def possible_moves(self, cell_name: str) -> list[str]:

        row, column = map_cell_to_index(cell_name)

        upper_left_diagonal: list[str] = self._check_line(row, column, -1, -1, cell_name)
        upper_right_diagonal: list[str] = self._check_line(row, column, -1, 1, cell_name)

        lower_left_diagonal: list[str] = self._check_line(row, column, 1, -1, cell_name)
        lower_right_diagonal: list[str] = self._check_line(row, column, 1, 1, cell_name)

        possible_moves: list[str] = upper_left_diagonal + upper_right_diagonal + lower_left_diagonal + lower_right_diagonal
        return possible_moves