from Pieces.Rook import Rook
from Pieces.Bishop import Bishop
from Pieces.Pawn import Pawn
from Pieces.King import King
from Pieces.Queen import Queen
from Pieces.Knight import Knight
from Board.Cell_utils import Cell_utils
from Board.MoveType import MoveType 
import numpy as np   
class Board:

    def __init__(self):

        self.board =  {
            "a1": Rook("a1", "w", self),
            "b1": Knight("b1", "w", self),
            "c1": Bishop("c1", "w", self),
            "d1": Queen("d1", "w", self),
            "e1": King("e1", "w", self),
            "f1": Bishop("f1", "w", self),
            "g1": Knight("g1", "w", self),
            "h1": Rook("h1", "w", self),
            "a2": Pawn("a2", "w", self),
            "b2": Pawn("b2", "w", self),
            "c2": Pawn("c2", "w", self),
            "d2": Pawn("d2", "w", self),
            "e2": Pawn("e2", "w", self),
            "f2": Pawn("f2", "w", self),
            "g2": Pawn("g2", "w", self),
            "h2": Pawn("h2", "w", self),
            "a8": Rook("a8", "b", self),
            "b8": Knight("b8", "b", self),
            "c8": Bishop("c8", "b", self),
            "d8": Queen("d8", "b", self),
            "e8": King("e8", "b", self),
            "f8": Bishop("f8", "b", self),
            "g8": Knight("g8", "b", self),
            "h8": Rook("h8", "b", self),
            "a7": Pawn("a7", "b", self),
            "b7": Pawn("b7", "b", self),
            "c7": Pawn("c7", "b", self),
            "d7": Pawn("d7", "b", self),
            "e7": Pawn("e7", "b", self),
            "f7": Pawn("f7", "b", self),
            "g7": Pawn("g7", "b", self),
            "h7": Pawn("h7", "b", self)
        }
        self.cells = np.zeros((8,8))

    def in_next_cell(self, prev_cell, next_cell) -> int:

        if Cell_utils.is_cell_empty(next_cell, self):
            return MoveType.EMPTY_CELL
        
        elif Cell_utils.is_white_piece(next_cell, self) != Cell_utils.is_white_piece(prev_cell, self):
            return MoveType.CAPTURE
        
        return MoveType.TEAMMATE

    def move(self, prev_cell, next_cell) -> int:
        prev_piece = self.board[prev_cell]
        possible_moves = prev_piece.possible_moves(prev_cell)
        print(next_cell)
        print(f"These are the possible moves: {possible_moves}")

        if next_cell in possible_moves:
            move = self.in_next_cell(prev_cell, next_cell)

            match move:

                case MoveType.EMPTY_CELL:
                    self.board[next_cell] = prev_piece
                    del self.board[prev_cell]
                
                case MoveType.CAPTURE:
                    self.board[next_cell] = prev_piece
                    del self.board[prev_cell]
                
            return move
        else:
            return MoveType.NOT_AVAILABLE
