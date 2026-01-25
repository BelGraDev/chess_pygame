from __future__ import annotations
from typing import TYPE_CHECKING
from Board.Pieces import Piece, PieceValue
from Utils.Cell_utils import map_cell_to_index
from Board.boardCells import Position
import pygame
if TYPE_CHECKING:
    from Board.BoardStatus import BoardStatus

class Rook(Piece):
    
    def __init__(self, type: str, board: BoardStatus) -> None:

        super().__init__(type, board)
        self.image = pygame.image.load(f"{self.image_path}{type}_rook.png").convert_alpha()
        self.value = PieceValue.ROOK

    def possible_moves(self, cell_name: str) -> list[str]:

        row, column = map_cell_to_index(cell_name)
        start = Position(row, column)
        
        upwards_check = self._check_line(start, Position(-1, 0), cell_name)
        downwards_check = self._check_line(start, Position(1, 0), cell_name)

        leftwards_check = self._check_line(start, Position(0, -1), cell_name)
        rightwards_check = self._check_line(start, Position(0, 1), cell_name)

        possible_moves = upwards_check + downwards_check + leftwards_check + rightwards_check
        return possible_moves

