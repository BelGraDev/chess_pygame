from abc import ABC, abstractmethod
import pygame

class Pieces(ABC, pygame.Rect):

    #Since each cell is 75 px * 75 p
    PIECE_HEIGHT: float = 75
    PIECE_WIDTH: float = 75

    def __init__(self, coord: tuple) -> None:

        pygame.Rect.__init__(self, coord[0], coord[1], self.PIECE_WIDTH, self.PIECE_HEIGHT)

    @abstractmethod
    def move(cell) -> str:
        pass

    @abstractmethod
    def possible_moves(cell) -> list:
        pass
    