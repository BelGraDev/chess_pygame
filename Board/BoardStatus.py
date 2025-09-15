from Pieces.Rook import Rook
from Pieces.Bishop import Bishop
from Pieces.Pawn import Pawn
from Pieces.King import King
from Pieces.Queen import Queen
from Pieces.Knight import Knight
from .Move import *
from .Board_Cells import Board_cells

class BoardStatus:

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
        self.w_king_cell = "e1"
        self.b_king_cell = "e8"
        self.turn = "w"
        self.cells = Board_cells(8,8)
        self.is_check = False
        self.is_check_mate = False


