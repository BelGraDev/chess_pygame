from Pieces.Pieces import Pieces
import pygame

class Queen(Pieces):
    
    
    def __init__(self, cell, type) -> None:

        super().__init__(cell, type)
        self.image = pygame.image.load(f"Pieces/images/{type}_queen.png")