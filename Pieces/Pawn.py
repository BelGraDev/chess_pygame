from .Pieces import Pieces
from Board.Move import MoveType
from Utils.Cell_utils import Cell_utils
import pygame


class Pawn(Pieces):

    def __init__(self, type, board) -> None:

        super().__init__(type, board)
        self.image = pygame.image.load(f"Pieces/images/{type}_pawn.png").convert_alpha()
    
    def possible_moves(self, cell_name) -> list:

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
            first_move = self._two_steps_move(cell_name, row - 2 * direction, column)
            if first_move:
                possible_moves.append(first_move)  

        return possible_moves
    
    def _two_steps_move(self, cell_name, next_row, column) -> str | None:

        move = self.is_next_possible(cell_name, next_row, column)
        if move and move.type == MoveType.EMPTY_CELL:
            return move.next_cell
            
        return None
