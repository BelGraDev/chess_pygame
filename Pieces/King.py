from Pieces.Pieces import Pieces
import pygame

class King(Pieces):
    
    
    def __init__(self, cell, type, board) -> None:

        super().__init__(cell, type, board)
        self.image = pygame.image.load(f"Pieces/images/{type}_king.png")