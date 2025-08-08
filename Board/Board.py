from Pieces.Rook import Rook
from Pieces.Bishop import Bishop
from Pieces.Pawn import Pawn
from Pieces.King import King
from Pieces.Queen import Queen
from Pieces.Knight import Knight
from Board.Cell_utils import Cell_utils
from Board.MoveType import MoveType     
class Board:

    def __init__(self):

        self.board =  {
            "a1": Rook("a1", "w"),
            "b1": Knight("b1", "w"),
            "c1": Bishop("c1", "w"),
            "d1": Queen("d1", "w"),
            "e1": King("e1", "w"),
            "f1": Bishop("f1", "w"),
            "g1": Knight("g1", "w"),
            "h1": Rook("h1", "w"),
            "a2": Pawn("a2", "w"),
            "b2": Pawn("b2", "w"),
            "c2": Pawn("c2", "w"),
            "d2": Pawn("d2", "w"),
            "e2": Pawn("e2", "w"),
            "f2": Pawn("f2", "w"),
            "g2": Pawn("g2", "w"),
            "h2": Pawn("h2", "w"),
            "a8": Rook("a8", "b"),
            "b8": Knight("b8", "b"),
            "c8": Bishop("c8", "b"),
            "d8": Queen("d8", "b"),
            "e8": King("e8", "b"),
            "f8": Bishop("f8", "b"),
            "g8": Knight("g8", "b"),
            "h8": Rook("h8", "b"),
            "a7": Pawn("a7", "b"),
            "b7": Pawn("b7", "b"),
            "c7": Pawn("c7", "b"),
            "d7": Pawn("d7", "b"),
            "e7": Pawn("e7", "b"),
            "f7": Pawn("f7", "b"),
            "g7": Pawn("g7", "b"),
            "h7": Pawn("h7", "b")
        }

    def move(self, prev_cell, next_cell) -> int:

        prev_piece = self.board[prev_cell]

        if Cell_utils.is_cell_empty(next_cell, self):
            self.board[next_cell] = prev_piece
            del self.board[prev_cell]
            print(f"Next cell is empty, moving from {prev_cell} to {next_cell}")
            return MoveType.EMPTY_CELL
        
        elif Cell_utils.is_white_piece(next_cell, self) != Cell_utils.is_white_piece(prev_cell, self):
                self.board[next_cell] = prev_piece
                del self.board[prev_cell]
                print(f"I've killed a man, moving from {prev_cell} to {next_cell}")
                return MoveType.CAPTURE
        
        print(f"Teammate in my target, staying on {prev_cell}")
        return MoveType.TEAMMATE

