from __future__ import annotations
from typing import TYPE_CHECKING
from Board.Pieces import Piece
from Board.boardCells import Position
from Utils.Cell_utils import map_cell_to_index
import pygame
if TYPE_CHECKING:
    from Board.BoardStatus import BoardStatus

class Bishop(Piece):
    
    def __init__(self, type: str, board: BoardStatus) -> None:

        super().__init__(type, board)
        self.image = pygame.image.load(f"{self.image_path}{type}_bishop.png").convert_alpha()

    def possible_moves(self, cell_name: str) -> list[str]:

        row, column = map_cell_to_index(cell_name)
        start = Position(row, column)
        
        upper_left_diagonal = self._check_line(start, Position(-1, -1), cell_name)
        upper_right_diagonal = self._check_line(start, Position(-1, 1), cell_name)

        lower_left_diagonal = self._check_line(start, Position(1, -1), cell_name)
        lower_right_diagonal = self._check_line(start, Position(1, 1), cell_name)

        possible_moves = upper_left_diagonal + upper_right_diagonal + lower_left_diagonal + lower_right_diagonal
        return possible_moves