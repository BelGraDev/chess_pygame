from abc import ABC, abstractmethod
import pygame

class Pieces(ABC, pygame.Rect):

    def __init__(self, cell, type) -> None:
        self.cell = cell
        self.type = type
        self.has_moved = False
        


    @abstractmethod
    def possible_moves(cell) -> list:
        pass
    