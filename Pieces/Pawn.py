from .Pieces import Pieces
from Board.Move import MoveType
from Utils.Cell_utils import Cell_utils
import pygame

class Pawn(Pieces):

    def __init__(self, type: str, board) -> None:

        super().__init__(type, board)
        self.image = pygame.image.load(f"Pieces/images/{type}_pawn.png").convert_alpha()
        self.is_passant = False
    
    def possible_moves(self, cell_name: str) -> list:

        row, column = Cell_utils.map_cell_to_index(cell_name)   

        possible_moves = []

        direction = 1 if self.type == "w" else -1

        for col in range(column - 1, column + 2):
            move = self.is_next_possible(cell_name, row - 1 * direction, col)
            if move:
                match move.type:
                    case MoveType.CAPTURE:
                        if col == column: continue
                    case _:
                        if col != column: continue
                possible_moves.append(move.next_cell)

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
                return move.next_cell
            
        return None
    
    def is_two_steps_move(self, prev_cell_name: str, next_cell_name: str) -> bool:
        if self.has_moved: 
            return False
        prev_row = Cell_utils.map_cell_to_index(prev_cell_name)[0]
        next_row = Cell_utils.map_cell_to_index(next_cell_name)[0]
        return abs(prev_row - next_row) == 2
    
    def _passant_pawn(self, cell_name: str) -> list:
        passant_moves = []
        row, col = Cell_utils.map_cell_to_index(cell_name)
        for c in range(col - 1, col + 2, 2):
            contiguous_cell_name = Cell_utils.map_index_to_cell(row, c)
            contiguous_piece = self.board.board.get(contiguous_cell_name)
            if isinstance(contiguous_piece, Pawn):
                if contiguous_piece.is_passant:
                    direction = 1 if self.type == "w" else -1
                    possible_move = Cell_utils.map_index_to_cell(row - 1 * direction, c)
                    passant_moves.append(possible_move)

        return passant_moves
