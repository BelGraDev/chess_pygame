from Pieces.Rook import Rook
from Pieces.Bishop import Bishop
from Pieces.Pawn import Pawn
from Pieces.King import King
from Pieces.Queen import Queen
from Pieces.Knight import Knight
from Board.Move import *
from Board.Board_Cells import Board_cells
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

    def move(self, prev_cell_name: str, next_cell_name) -> int | None:
        prev_piece = self.board[prev_cell_name]
        possible_moves = prev_piece.possible_moves(prev_cell_name)

        move = Move(self, prev_cell_name, next_cell_name)
        
        if next_cell_name in possible_moves:
            self.board[next_cell_name] = prev_piece
            del self.board[prev_cell_name]

        elif not Cell_utils.are_teammates(prev_cell_name, next_cell_name, self):
            return MoveType.NOT_AVAILABLE
        
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