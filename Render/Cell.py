import pygame

class Cell(pygame.Rect):
    CELL_SIZE = 75
    def __init__(self, coord: iter, name: str, color: tuple) -> None:

        self.name = name
        self.color = color
        pygame.Rect.__init__(self, coord[0], coord[1],  self.CELL_SIZE, self.CELL_SIZE)
