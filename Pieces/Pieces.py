from abc import ABC, abstractmethod
import pygame

class Pieces(ABC, pygame.Rect):

    def __init__(self, coord: tuple) -> None:

        #Since each cell is 75 px * 75 px
        self.PIECE_HEIGHT: float = 75
        self.PIECE_WIDTH: float = 75
        self.graveyard: list = []

        pygame.Rect.__init__(self, coord[0], coord[1], self.PIECE_WIDTH, self.PIECE_HEIGHT)
        
    @abstractmethod
    def render_piece(screen) -> None:
        pass

    @abstractmethod
    def move(cell) -> str:
        pass

    @abstractmethod
    def possible_moves(cell) -> list:
        pass
    
class King: 
    pass
class Queen:
    pass
class Pawn:
    pass
class Knight:
    pass
class Rook:
    pass
class Bishop:
    pass