from Pieces.Pieces import Pieces
from Pieces.Rook import Rook
from Pieces.Bishop import Bishop
import pygame

class Queen(Rook, Bishop):
    
    
    def __init__(self, cell, type, board) -> None:

        super().__init__(cell, type, board)
        self.image = pygame.image.load(f"Pieces/images/{type}_queen.png")

    def possible_moves(self, cell_name):
        diagonal_moves = Bishop.possible_moves(self, cell_name)
        line_moves = Rook.possible_moves(self, cell_name)

        possible_moves = diagonal_moves + line_moves
        return possible_moves