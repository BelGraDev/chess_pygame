from __future__ import annotations
from typing import TYPE_CHECKING
from Board.Pieces import Rook, Bishop, Piece, PieceValue
import pygame
if TYPE_CHECKING:
    from Board.BoardStatus import BoardStatus
    
class Queen(Piece):
    
    
    def __init__(self, type: str, board: BoardStatus) -> None:

        super().__init__(type, board)
        self.image = pygame.image.load(f"{self.image_path}{type}_queen.png").convert_alpha()
        self.value = PieceValue.QUEEN

    def possible_moves(self, cell_name: str) -> list[str]:
        diagonal_moves: list[str] = Bishop.possible_moves(self, cell_name)
        line_moves: list[str] = Rook.possible_moves(self, cell_name)

        possible_moves: list[str] = diagonal_moves + line_moves
        return possible_moves