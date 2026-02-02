from __future__ import annotations
from typing import TYPE_CHECKING
from Board.Pieces import Piece, Rook, Knight, Bishop, Pawn, PieceValue
from Board import PieceColor
from Utils.Cell_utils import map_cell_to_index, map_index_to_cell
from Utils.Board_Utils import is_cell_empty
import pygame

if TYPE_CHECKING:
    from Board import BoardStatus
    
class King(Piece):
    
    def __init__(self, type: str, board: BoardStatus) -> None:
        super().__init__(type, board)
        self.image = pygame.image.load(f"{self.image_path}{type}_king.png").convert_alpha()
        self.value = PieceValue.KING


    def possible_moves(self, cell_name: str) -> list[str]: 
        row, column = map_cell_to_index(cell_name)

        possible_moves = [move.step.end_cell 
                          for r in range(row - 1, row + 2)
                          for c in range(column - 1, column + 2)
                          if (move := self.is_next_possible(cell_name, r, c))]

        return possible_moves + self.castle_moves(row, column)
    
    
    def castle_moves(self, row: int, col: int) -> list[str]:
        left_goal_col = col - 2
        left_start_col = col - 1
        left_end_col = col - 4

        right_goal_col = col + 2
        right_start_col = col + 1
        right_end_col = col + 3

        return (self._castle_moves(row, left_goal_col, left_start_col, left_end_col) + 
                self._castle_moves(row, right_goal_col, right_start_col, right_end_col))
    

    def _castle_moves(self, row: int, goal_col: int, start_col: int, end_col: int) -> list[str]:  
        castle_moves: list[str] = []
        if not self.has_moved:

            rook_cell: str = map_index_to_cell(row, end_col)
            if is_cell_empty(rook_cell, self.board) or self.board[rook_cell].has_moved:
                return castle_moves
            
            step = 1 if start_col < end_col else -1
            cells_between_rook_and_king = (map_index_to_cell(row, c) for c in range(start_col, end_col, step))

            if all(is_cell_empty(cell, self.board) for cell in cells_between_rook_and_king):
                castle_cell = map_index_to_cell(row, goal_col)
                castle_moves.append(castle_cell)

        return castle_moves
    
    
    def is_on_check(self, cell_name: str) -> bool:
        is_check_possible = [lambda: self._inspect_moves(Knight.possible_moves(self, cell_name), "Knight"),
                            lambda: self._inspect_moves(Rook.possible_moves(self, cell_name), "Queen", "Rook"),
                            lambda: self._inspect_moves(Bishop.possible_moves(self, cell_name), "Queen", "Bishop"),
                            lambda: self._inspect_moves(self.possible_moves(cell_name), "King"),
                            lambda: self._inspect_pawn(cell_name)]
        
        return any(check() for check in is_check_possible)   
    

    def _inspect_moves(self, possible_check: list[str], piece1: str, piece2: None | str = None) -> bool:
        return any(self.board[cell].__class__.__name__ in (piece1, piece2) 
                   for cell in possible_check
                   if not is_cell_empty(cell, self.board))
    
    
    def _inspect_pawn(self, cell_name: str) -> bool:
        row, col = map_cell_to_index(cell_name)
        direction = 1 if self.type == PieceColor.BLACK else -1
        check_pawn_offsets = [(1 * direction, 1), (1 * direction, -1)]

        for r, c in check_pawn_offsets:
            move_cell = map_index_to_cell(row + r, col + c)
            if not is_cell_empty(move_cell, self.board):
                piece = self.board[move_cell]
                if piece.type != self.type and isinstance(piece, Pawn):
                    return True
        return False
