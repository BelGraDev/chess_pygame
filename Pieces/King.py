from Pieces.Pieces import Pieces
from Utils.Cell_utils import Cell_utils
import pygame

class King(Pieces):
    
    
    def __init__(self, type, board) -> None:

        super().__init__(type, board)
        self.image = pygame.image.load(f"Pieces/images/{type}_king.png")

    def possible_moves(self, cell_name):

        row, column = Cell_utils.map_cell_to_index(cell_name)

        possible_moves = []

        for r in range(row - 1, row + 2):
            for c in range(column - 1, column + 2):
                move = self.is_next_possible(cell_name, r, c)
                if move:
                    possible_moves.append(move.next_cell)

        return possible_moves