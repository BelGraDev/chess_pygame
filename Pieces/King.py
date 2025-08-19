from Pieces.Pieces import Pieces
from Pieces.Bishop import Bishop
from Pieces.Rook import Rook
from Pieces.Knight import Knight
from Utils.Cell_utils import Cell_utils
import pygame

class King(Pieces):
    
    
    def __init__(self, type, board) -> None:

        super().__init__(type, board)
        self.image = pygame.image.load(f"Pieces/images/{type}_king.png").convert_alpha()

    def possible_moves(self, cell_name):

        row, column = Cell_utils.map_cell_to_index(cell_name)

        possible_moves = []

        for r in range(row - 1, row + 2):
            for c in range(column - 1, column + 2):
                move = self.is_next_possible(cell_name, r, c)
                if move:
                    possible_moves.append(move.next_cell)

        return possible_moves
    
    def is_on_check(self, cell_name):

        check_horizontal = Rook.possible_moves(self, cell_name)
        check_diagonal = Bishop.possible_moves(self, cell_name)
        check_knight = Knight.possible_moves(self, cell_name)

        if self._inspect_moves(check_knight, "Knight"):
            return True
                
        if self._inspect_moves(check_horizontal, "Queen", "Rook"):
            return True

        if self._inspect_moves(check_diagonal, "Queen", "Bishop"):
            return True
        
        if self._inspect_pawn(cell_name):
            return True
        
        return False
    
    
    def _inspect_moves(self, possible_check, piece1, piece2 = None):
        for move_cell in possible_check:
            if not Cell_utils.is_cell_empty(move_cell, self.board):
                piece = self.board.board[move_cell]
                if piece.__class__.__name__ == piece1 or piece.__class__.__name__ == piece2:
                    return True
        return False
    
    def _inspect_pawn(self, cell_name):

        row, col = Cell_utils.map_cell_to_index(cell_name)
        direction = 1 if self.type == "b" else -1
        check_pawn_offsets = [(1 * direction, 1), (1 * direction, -1)]

        for r, c in check_pawn_offsets:
            move_cell = Cell_utils.map_index_to_cell(row + r, col + c)
            if not Cell_utils.is_cell_empty(move_cell, self.board):
                piece = self.board.board[move_cell]
                if piece.type != self.type and piece.__class__.__name__ == "Pawn":
                    return True
        return False