from Board.Pieces import Rook, Bishop
import pygame

class Queen(Rook, Bishop):
    
    
    def __init__(self, type: str, board) -> None:

        super().__init__(type, board)
        self.image = pygame.image.load(f"{self.image_path}{type}_queen.png").convert_alpha()

    def possible_moves(self, cell_name: str) -> list[str]:
        diagonal_moves: list[str] = Bishop.possible_moves(self, cell_name)
        line_moves: list[str] = Rook.possible_moves(self, cell_name)

        possible_moves: list[str] = diagonal_moves + line_moves
        return possible_moves