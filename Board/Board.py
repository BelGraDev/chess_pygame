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
        self.w_king_cell = "e1"
        self.b_king_cell = "e8"
        self.turn = "w"
        self.cells = Board_cells(8,8)
        self.is_check_mate = False

    def move(self, prev_cell_name: str, next_cell_name) -> int:

        move = Move(self, prev_cell_name, next_cell_name)

        if move.type is not MoveType.TEAMMATE:
            if not self._is_valid_move(prev_cell_name, next_cell_name):
                return MoveType.NOT_AVAILABLE
            else: 

                if self._want_to_castle(prev_cell_name, next_cell_name):
                    self._castle(prev_cell_name, next_cell_name)
                    move.type = MoveType.CASTLE
                else:
                    Board_Utils.move_piece_in_board(self.board, prev_cell_name, next_cell_name)

                self._update_king_cell(next_cell_name, self.turn)

                if self._opponent_under_check_mate():
                    return MoveType.CHECK_MATE
                
        return move.type

    def move_to_cell(self, cell_name: str) -> None:
        piece = self.board[cell_name]

        if not piece.has_moved:
            piece.has_moved = True

        self._switch_turn()

    def can_color_play(self, cell_name: str) -> bool:

        prev_cell_piece = self.board[cell_name]
        return prev_cell_piece.type == self.turn
    
    #Move validation and check related methods
    def _is_valid_move(self, prev_cell_name: str, next_cell_name: str) -> bool:

        original_next_piece = self.board.get(next_cell_name)
        prev_piece = Board_Utils.move_piece_in_board(self.board, prev_cell_name, next_cell_name)

        if prev_piece is not None:
            prev_piece_color = prev_piece.type
            self._update_king_cell(next_cell_name, prev_piece_color)

            king_is_in_check = self._is_king_in_check(prev_piece_color)
            Board_Utils.restore_last_state(self.board, prev_piece, original_next_piece, prev_cell_name, next_cell_name)
            
            self._update_king_cell(prev_cell_name, prev_piece_color)
            return not king_is_in_check
        else:
            return False
    
    def _want_to_castle(self, prev_cell_name: str, next_cell_name: str) -> bool:
        prev_piece = self.board[prev_cell_name]
        if isinstance(prev_piece, King):
            possible_moves = prev_piece.possible_moves(prev_cell_name)
            if next_cell_name in possible_moves:
                prev_row, prev_col = Cell_utils.map_cell_to_index(prev_cell_name)
                next_row, next_col = Cell_utils.map_cell_to_index(next_cell_name)
                return abs(prev_col - next_col) == 2
        return False

    def _is_king_in_check(self, king_color: str) -> bool:
        king_cell = self.w_king_cell if king_color == "w" else self.b_king_cell
        king = self.board[king_cell]
        return king.is_on_check(king_cell)

    def _opponent_under_check_mate(self) -> bool:
        opponent_color = "b" if self.turn == "w" else "w"
        for cell_name, piece in list(self.board.items()):
            if piece.type == opponent_color:
                possible_moves = piece.possible_moves(cell_name)
                for move in possible_moves:
                    is_valid = self._is_valid_move(cell_name, move)
                    if is_valid:
                        return False
        self.is_check_mate = True
        return True
    
    def _update_king_cell(self, cell_name: str, king_color) -> None:
        piece = self.board[cell_name]
        if isinstance(piece, King):
            if king_color == "w":
                self.w_king_cell = cell_name
            else:
                self.b_king_cell = cell_name

    #End move validation and check related methods
    #Castle related methods
    def _castle(self, prev_cell: str, next_cell: str) -> None:
        king = self.board[prev_cell]
        self.board[next_cell] = king
        del self.board[prev_cell]

        row, col = Cell_utils.map_cell_to_index(next_cell)

        rook1_cell_name = Cell_utils.map_index_to_cell(row, col + 1)
        next_rook_cell_name = Cell_utils.map_index_to_cell(row, col - 1)
        if self._castle_rook(rook1_cell_name, next_rook_cell_name): return

        rook2_cell_name = Cell_utils.map_index_to_cell(row, col - 2)
        next_rook_cell_name = Cell_utils.map_index_to_cell(row, col + 1)
        self._castle_rook(rook2_cell_name, next_rook_cell_name)

    def _castle_rook(self, rook_cell_name: str, next_rook_cell_name: str) -> bool:
        rook = self.board.get(rook_cell_name)
        if rook is not None and not rook.has_moved:
            self.board[next_rook_cell_name] = rook
            del self.board[rook_cell_name]
            return True
        return False
    
    #End castle related methods
    def _switch_turn(self) -> None:
        self.turn = "b" if self.turn == "w" else "w"