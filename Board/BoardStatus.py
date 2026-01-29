from .Pieces import Piece, Knight, Bishop, Rook, Pawn, Queen, King
from . import PieceColor, BoardCells
from collections.abc import MutableMapping
from typing import Iterator, cast, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from Board.Move import MoveType


class BoardStatus(MutableMapping[str, Piece]):

    def __init__(self):
        self._board: dict[str, Piece] =  {
            "a1": Rook(PieceColor.WHITE, self),
            "b1": Knight(PieceColor.WHITE, self),
            "c1": Bishop(PieceColor.WHITE, self),
            "d1": Queen(PieceColor.WHITE, self),
            "e1": King(PieceColor.WHITE, self),
            "f1": Bishop(PieceColor.WHITE, self),
            "g1": Knight(PieceColor.WHITE, self),
            "h1": Rook(PieceColor.WHITE, self),
            "a2": Pawn(PieceColor.WHITE, self),
            "b2": Pawn(PieceColor.WHITE, self),
            "c2": Pawn(PieceColor.WHITE, self),
            "d2": Pawn(PieceColor.WHITE, self),
            "e2": Pawn(PieceColor.WHITE, self),
            "f2": Pawn(PieceColor.WHITE, self),
            "g2": Pawn(PieceColor.WHITE, self),
            "h2": Pawn(PieceColor.WHITE, self),
            "a8": Rook(PieceColor.BLACK, self),
            "b8": Knight(PieceColor.BLACK, self),
            "c8": Bishop(PieceColor.BLACK, self),
            "d8": Queen(PieceColor.BLACK, self),
            "e8": King(PieceColor.BLACK, self),
            "f8": Bishop(PieceColor.BLACK, self),
            "g8": Knight(PieceColor.BLACK, self),
            "h8": Rook(PieceColor.BLACK, self),
            "a7": Pawn(PieceColor.BLACK, self),
            "b7": Pawn(PieceColor.BLACK, self),
            "c7": Pawn(PieceColor.BLACK, self),
            "d7": Pawn(PieceColor.BLACK, self),
            "e7": Pawn(PieceColor.BLACK, self),
            "f7": Pawn(PieceColor.BLACK, self),
            "g7": Pawn(PieceColor.BLACK, self),
            "h7": Pawn(PieceColor.BLACK, self)
        }
        self.w_king_cell = "e1"
        self.b_king_cell = "e8"
        self.turn = PieceColor.WHITE
        self.num_rows = self.num_col = 8
        self.cells = BoardCells(self.num_rows,self.num_col)
        self.end_game: Optional[MoveType] = None
    

    def switch_turn(self) -> None:
        self.turn = PieceColor.BLACK if self.turn == PieceColor.WHITE else PieceColor.WHITE
    

    def update_king_cell(self, cell_name: str, king_color: str) -> None:
        piece = self._board[cell_name]
        if isinstance(piece, King):
            if king_color == PieceColor.WHITE:
                self.w_king_cell = cell_name
            else:
                self.b_king_cell = cell_name


    def is_king_in_check(self, king_color: str) -> bool:
        king_cell = self.w_king_cell if king_color == PieceColor.WHITE else self.b_king_cell
        king =  cast(King, self._board[king_cell])
        return king.is_on_check(king_cell)
    
    
    def ascension_pieces(self) -> list[Piece]:
        return [Queen(self.turn, self), 
                Rook(self.turn, self), 
                Bishop(self.turn, self),
                Knight(self.turn, self)]


    def __getitem__(self, cell_name: str) -> Piece:
        return self._board[cell_name]


    def __iter__(self) -> Iterator[str]:
        return iter(self._board)
    

    def __len__(self) -> int:
        return len(self._board)
    

    def __setitem__(self, cell_name: str, piece: Piece) -> None:
        self._board[cell_name] = piece
    

    def __delitem__(self, cell_name: str) -> None:
        del self._board[cell_name]