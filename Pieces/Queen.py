from Pieces.Pieces import Pieces
import pygame

class Queen(Pieces):
    
    
    def __init__(self, cell, type, board) -> None:

        super().__init__(cell, type, board)
        self.image = pygame.image.load(f"Pieces/images/{type}_queen.png")

    def possible_moves(self, cell_name):
        pass