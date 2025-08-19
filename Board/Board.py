from Pieces.Rook import Rook
from Pieces.Bishop import Bishop
from Pieces.Pawn import Pawn
from Pieces.King import King
from Pieces.Queen import Queen
from Pieces.Knight import Knight
from Board.Move import *
from Board.Board_Cells import Board_cells
from Utils.Board_Utils import Board_Utils
class Board:

    def __init__(self):

        self.board =  {
            "a1": Rook("w", self),
            "b1": Knight("w", self),
            "c1": Bishop("w", self),
            "d1": Queen("w", self),
            "e1": King("w", self),
            "f1": Bishop("w", self),
            "g1": Knight("w", self),
            "h1": Rook("w", self),
            "a2": Pawn("w", self),
            "b2": Pawn("w", self),
            "c2": Pawn("w", self),
            "d2": Pawn("w", self),
            "e2": Pawn("w", self),
            "f2": Pawn("w", self),
            "g2": Pawn("w", self),
            "h2": Pawn("w", self),
            "a8": Rook("b", self),
            "b8": Knight("b", self),
            "c8": Bishop("b", self),
            "d8": Queen("b", self),
            "e8": King("b", self),
            "f8": Bishop("b", self),
            "g8": Knight("b", self),
            "h8": Rook("b", self),
            "a7": Pawn("b", self),
            "b7": Pawn("b", self),
            "c7": Pawn("b", self),
            "d7": Pawn("b", self),
            "e7": Pawn("b", self),
            "f7": Pawn("b", self),
            "g7": Pawn("b", self),
            "h7": Pawn("b", self)
        }
        self.turn = "w"
        self.cells = Board_cells(8,8)

    def move(self, prev_cell_name: str, next_cell_name) -> int:

        move = Move(self, prev_cell_name, next_cell_name)

        if move.type != MoveType.TEAMMATE:
            if not self._is_valid_move(prev_cell_name, next_cell_name):
                return MoveType.NOT_AVAILABLE
            else: 
                Board_Utils.move_piece_in_board(self.board, prev_cell_name, next_cell_name)
                if self._opponent_under_check_mate():
                    return MoveType.CHECK_MATE
                
        return move.type

    def move_to_cell(self, cell_name: str) -> None:
        piece = self.board[cell_name]
        if not piece.has_moved:
            piece.has_moved = True

        self._switch_turn()

    def _switch_turn(self) -> None:
        self.turn = "b" if self.turn == "w" else "w"

    def can_color_play(self, cell_name: str) -> bool:

        prev_cell_piece = self.board[cell_name]
        is_same_turn = prev_cell_piece.type == self.turn
        return True if is_same_turn else False

    def _is_valid_move(self, prev_cell_name: str, next_cell_name: str) -> bool:

        original_next_piece = self.board.get(next_cell_name)
        prev_piece = Board_Utils.move_piece_in_board(self.board, prev_cell_name, next_cell_name)

        if prev_piece is not None:
            king_is_in_check = self._is_king_in_check(prev_piece.type)
            Board_Utils.restore_last_state(self.board, prev_piece, original_next_piece, prev_cell_name, next_cell_name)
            return not king_is_in_check
        else:
            return False
       
    def _is_king_in_check(self, king_color: str) -> bool:

        king_cell = None
        for cell, piece in self.board.items():
            if piece.__class__.__name__ == "King" and piece.type == king_color:
                king_cell = cell
                break
        opponent_color = "b" if king_color == "w" else "w"
        for cell, piece in self.board.items():

            if piece.type == opponent_color:
                if king_cell in piece.possible_moves(cell):
                    return True 
        return False

    def _opponent_under_check_mate(self) -> bool:
        opponent_color = "w" if self.turn == "b" else "b"
        for cell_name, piece in self.board.items():
            if piece.type == opponent_color:
                possible_moves = piece.possible_moves(cell_name)
                for move in possible_moves:
                    is_valid = self._is_valid_move(cell_name, move)
                    if is_valid:
                        print("Not mate") 
                        return False
        print("CHECK MATE")
        return True