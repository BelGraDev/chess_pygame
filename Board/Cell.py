import pygame

class Cell(pygame.Rect):

    def __init__(self, coord: iter, name: str):
        self.CELL_SIZE = 75
        self.name = name
        pygame.Rect.__init__(self, coord[0], coord[1],  self.CELL_SIZE, self.CELL_SIZE)

    def get_name(self) -> str:
        return self.name
