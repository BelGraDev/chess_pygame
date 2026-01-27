from __future__ import annotations
from typing import TYPE_CHECKING
from Board.Pieces import Piece, PieceValue
from Utils.Cell_utils import map_cell_to_index
import pygame

if TYPE_CHECKING:
    from Board.BoardStatus import BoardStatus\
    
class Knight(Piece):
    
    
    def __init__(self, type: str, board: BoardStatus) -> None:

        super().__init__(type, board)
        self.image = pygame.image.load(f"{self.image_path}{type}_knight.png").convert_alpha()
        self.value = PieceValue.KNIGHT



    def possible_moves(self, cell_name: str) -> list[str]:

        row, column = map_cell_to_index(cell_name)

        move_offsets: list[tuple[int, int]] = [(-2, -1), (-2, 1), (2, -1), (2, 1), 
                                            (-1, -2), (-1, 2), (1, -2), (1, 2)]

        possible_moves = [move.step.end_cell
                          for r, c in move_offsets
                          if (move := self.is_next_possible(cell_name, row + r, column + c))]

        return possible_moves