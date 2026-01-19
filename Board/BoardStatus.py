from .Pieces import Piece, Knight, Bishop, Rook, Pawn, Queen, King
from .Move import *
from .Board_Cells import Board_cells

class BoardStatus:

    def __init__(self):
        self.board: dict[str, Piece] =  {
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
        self.is_end_game = False
    

    def switch_turn(self) -> None:
        self.turn = "b" if self.turn == "w" else "w"
    

    def update_king_cell(self, cell_name: str, king_color: str) -> None:
        piece = self.board[cell_name]
        if isinstance(piece, King):
            if king_color == "w":
                self.w_king_cell = cell_name
            else:
                self.b_king_cell = cell_name


    def is_king_in_check(self, king_color: str) -> bool:
        king_cell = self.w_king_cell if king_color == "w" else self.b_king_cell
        king =  self.board[king_cell]
        return king.is_on_check(king_cell)
    
    def ascension_pieces(self) -> list[Piece]:
        return [Queen(self.turn, self), 
                Knight(self.turn, self), 
                Rook(self.turn, self), 
                Bishop(self.turn, self)]

    def __getitem__(self, cell_name: str) -> Piece:
        return self.board[cell_name]


    def __setitem__(self, cell_name: str, piece: Piece) -> None:
        self.board[cell_name] = piece
    

    def __delitem__(self, cell_name: str) -> None:
        del self.board[cell_name]
    

    def get(self, cell_name: str) -> Piece | None:
        return self.board.get(cell_name)
