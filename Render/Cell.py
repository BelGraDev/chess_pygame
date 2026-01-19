import pygame

class Cell(pygame.Rect):
    CELL_SIZE = 75
    def __init__(self, coord: tuple[float, float], name: str, color: tuple[int, int, int, int]) -> None:

        self.name = name
        self.color = color
        pygame.Rect.__init__(self, coord[0], coord[1],  self.CELL_SIZE, self.CELL_SIZE)
