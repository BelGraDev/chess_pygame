from Pieces.Pieces import Pieces
from Board.Cell_utils import Cell_utils
import pygame

class Knight(Pieces):
    
    
    def __init__(self, cell, type, board) -> None:

        super().__init__(cell, type, board)
        self.image = pygame.image.load(f"Pieces/images/{type}_knight.png")

    def possible_moves(self, cell_name) -> list:

        row, column = Cell_utils.map_cell_to_index(cell_name)

        move_offsets = [(-2, -1), (-2, 1), (2, -1), (2, 1), 
                        (-1, -2), (-1, 2), (1, -2), (1, 2)]

        possible_moves = []

        for r, c in move_offsets:
            move = self.is_next_possible(cell_name, row + r, column + c)
            if move:
                possible_moves.append(move.next_cell)

        return possible_moves