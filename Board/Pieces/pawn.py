from __future__ import annotations
from typing import TYPE_CHECKING
from Board.Pieces import Piece, PieceValue
from Board.Move import MoveType, Step
from Utils.Cell_utils import map_cell_to_index, map_index_to_cell
import pygame
if TYPE_CHECKING:
    from Board.BoardStatus import BoardStatus

class Pawn(Piece):


    def __init__(self, type: str, board: BoardStatus) -> None:
        super().__init__(type, board)
        self.image = pygame.image.load(f"{self.image_path}{type}_pawn.png").convert_alpha()
        self.value = PieceValue.PAWN
        self.is_passant = False
    

    def possible_moves(self, cell_name: str) -> list[str]:
        row, column = map_cell_to_index(cell_name)   
        possible_moves: list[str] = []
        direction: int = 1 if self.type == "w" else -1

        for col in range(column - 1, column + 2):
            move = self.is_next_possible(cell_name, row - 1 * direction, col)
            if move:
                match move.type:
                    case MoveType.CAPTURE:
                        if col == column: continue
                    case _:
                        if col != column: continue
                possible_moves.append(move.step.end_cell)

        if not self.has_moved:
            first_move = self._two_steps_move(cell_name, row - 1 * direction, row - 2 * direction, column)
            if first_move:
                possible_moves.append(first_move)  

        return possible_moves + self._passant_pawn(cell_name)
    

    def _two_steps_move(self, cell_name: str, one_step_row: int, two_step_row: int, column: int) -> str | None:
        move_one_step = self.is_next_possible(cell_name, one_step_row, column)
        if move_one_step and move_one_step.type is MoveType.EMPTY_CELL:

            move = self.is_next_possible(cell_name, two_step_row, column)
            if move and move.type == MoveType.EMPTY_CELL:
                return move.step.end_cell
            
        return None
    

    def is_two_steps_move(self, step: Step) -> bool:
        if self.has_moved: 
            return False
        prev_row = map_cell_to_index(step.start_cell)[0]
        next_row = map_cell_to_index(step.end_cell)[0]
        return abs(prev_row - next_row) == 2
    

    def _passant_pawn(self, cell_name: str) -> list[str]:
        passant_moves: list[str] = []
        row, col = map_cell_to_index(cell_name)
        for c in range(col - 1, col + 2, 2):
            contiguous_cell_name: str = map_index_to_cell(row, c)
            contiguous_piece = self.board.get(contiguous_cell_name)
            if isinstance(contiguous_piece, Pawn) and contiguous_piece.type != self.type:
                if contiguous_piece.is_passant:
                    direction: int = 1 if self.type == "w" else - 1
                    possible_move: str = map_index_to_cell(row - 1 * direction, c)
                    passant_moves.append(possible_move)

        return passant_moves
