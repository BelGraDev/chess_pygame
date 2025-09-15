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

    def possible_moves(self, cell_name: str) -> list[str]: 
        row, column = Cell_utils.map_cell_to_index(cell_name)

        possible_moves: list[str] = []

        for r in range(row - 1, row + 2):
            for c in range(column - 1, column + 2):
                move = self.is_next_possible(cell_name, r, c)
                if move:
                    possible_moves.append(move.next_cell)

        possible_moves = possible_moves + self.castle_moves(row, column)
        return possible_moves
    
    def castle_moves(self, row: int, col: int) -> list[str]:
        return self._castle_move_left(row, col) + self._castle_move_right(row, col)

    def _castle_move_right(self, row: int, col: int) -> list[str]:
        castle_moves: list[str] = []
        if not self.has_moved:

            rook_cell: str = Cell_utils.map_index_to_cell(row, col + 3)
            if Cell_utils.is_cell_empty(rook_cell, self.board) or self.board.board[rook_cell].has_moved:
                return castle_moves
            
            c: int = col + 1
            while c <= col + 2:
                cell_name = Cell_utils.map_index_to_cell(row, c)
                if not Cell_utils.is_cell_empty(cell_name, self.board): break
                c += 1
            if c > col + 2:
                castle_moves.append(cell_name) 
        return castle_moves  
    
    def _castle_move_left(self, row: int, col: int) -> list[str]:  
        castle_moves: list[str] = []
        if not self.has_moved:

            rook_cell: str = Cell_utils.map_index_to_cell(row, col - 4)
            if Cell_utils.is_cell_empty(rook_cell, self.board) or self.board.board[rook_cell].has_moved:
                return castle_moves
            
            c: int = col - 1
            while c >= col - 3:
                cell_name = Cell_utils.map_index_to_cell(row, c)
                if not Cell_utils.is_cell_empty(cell_name, self.board): break
                c -= 1
            if c < col - 3:
                castle_cell = Cell_utils.map_index_to_cell(row, col - 2)
                castle_moves.append(castle_cell)
        return castle_moves
    
    def is_on_check(self, cell_name: str) -> bool:

        check_horizontal: list[str] = Rook.possible_moves(self, cell_name)
        check_diagonal: list[str] = Bishop.possible_moves(self, cell_name)
        check_knight: list[str] = Knight.possible_moves(self, cell_name)
        check_king: list[str] = self.possible_moves(cell_name)

        if self._inspect_moves(check_knight, "Knight"):
            return True
                
        if self._inspect_moves(check_horizontal, "Queen", "Rook"):
            return True

        if self._inspect_moves(check_diagonal, "Queen", "Bishop"):
            return True
        
        if self._inspect_moves(check_king, "King"):
             return True
        
        if self._inspect_pawn(cell_name):
            return True
        
        return False
    
    def _inspect_moves(self, possible_check, piece1, piece2 = None) -> bool:
        for move_cell in possible_check:
            if not Cell_utils.is_cell_empty(move_cell, self.board):
                piece = self.board.board[move_cell]
                if piece.__class__.__name__ == piece1 or piece.__class__.__name__ == piece2:
                    return True
        return False
    
    def _inspect_pawn(self, cell_name: str) -> bool:
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
