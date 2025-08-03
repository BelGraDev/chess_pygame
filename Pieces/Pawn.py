from .Pieces import Pieces
import pygame


class Pawn(Pieces):

    def __init__(self, position) -> None:

        self.image = pygame.image.load("Pieces/images/pawn.png")
        self.position = position

    def render_piece(self, screen) -> None:
        image = self.image
        screen.blit(image, self)

    def move(cell: str) -> str:
        pass

