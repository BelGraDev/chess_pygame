from Pieces.Pieces import Pieces
import pygame

class Rook(Pieces):

    
    def __init__(self, cell, type) -> None:

        self.cell = cell
        self.image = pygame.image.load(f"Pieces/images/{type}_rook.png")