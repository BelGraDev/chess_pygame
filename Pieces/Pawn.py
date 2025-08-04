from .Pieces import Pieces
import pygame


class Pawn(Pieces):

    def __init__(self, cell, type) -> None:

        super().__init__(cell, type)
        self.image = pygame.image.load(f"Pieces/images/{type}_pawn.png")

    def move(self, cell: str) -> str:
        self.cell = cell

