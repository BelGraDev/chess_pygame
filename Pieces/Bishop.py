from Pieces.Pieces import Pieces
import pygame

class Bishop(Pieces):
    
        def __init__(self, cell, type) -> None:

            self.cell = cell
            self.image = pygame.image.load(f"Pieces/images/{type}_bishop.png")