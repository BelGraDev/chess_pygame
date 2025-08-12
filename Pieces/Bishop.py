from Pieces.Pieces import Pieces
from Board.Cell_utils import Cell_utils
import pygame

class Bishop(Pieces):
    
    def __init__(self, cell, type, board) -> None:

        super().__init__(cell, type, board)
        self.image = pygame.image.load(f"Pieces/images/{type}_bishop.png")

    def possible_moves(self, cell_name):

        row, column = Cell_utils.map_cell_to_index(cell_name)

        possible_moves = []

        upper_left_diagonal = self._check_line(row, column, -1, -1, cell_name)
        upper_right_diagonal = self._check_line(row, column, -1, 1, cell_name)

        lower_left_diagonal = self._check_line(row, column, 1, -1, cell_name)
        lower_right_diagonal = self._check_line(row, column, 1, 1, cell_name)

        possible_moves = upper_left_diagonal + upper_right_diagonal + lower_left_diagonal + lower_right_diagonal
        return possible_moves