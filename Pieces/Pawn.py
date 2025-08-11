from .Pieces import Pieces
from Board.Cell_utils import Cell_utils
from Board.MoveType import MoveType
import pygame


class Pawn(Pieces):

    def __init__(self, cell, type, board) -> None:

        super().__init__(cell, type, board)
        self.image = pygame.image.load(f"Pieces/images/{type}_pawn.png")
    
    def possible_moves(self, cell_name) -> list:

        row, column = Cell_utils.map_cell_to_index(cell_name)   

        possible_moves = [self.is_next_possible(cell_name, row - 1, col) for col in range(column - 1, column + 2)]
        possible_moves = [move for move in possible_moves if move is not None]
        print(possible_moves)

        if not self.has_moved:
            next_move = Cell_utils.map_index_to_cell(row - 2, column)
            possible_moves.append(next_move)  

        return possible_moves

