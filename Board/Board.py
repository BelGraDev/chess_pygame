from Pieces.Rook import Rook
from Pieces.Bishop import Bishop
from Pieces.Pawn import Pawn
from Pieces.King import King
from Pieces.Queen import Queen
from Pieces.Knight import Knight
from .Move import *
from Utils.Board_Utils import Board_Utils
from .BoardStatus import BoardStatus
from .MoveValidator import MoveValidator
class Board:

    def __init__(self):
        self.board_status = BoardStatus()
        self.move_validator = MoveValidator(self.board_status)

    def move(self, prev_cell_name: str, next_cell_name) -> int:

        move = Move(self.board_status, prev_cell_name, next_cell_name)

        if move.type is not MoveType.TEAMMATE:
            if not self.move_validator._is_valid_move(prev_cell_name, next_cell_name):
                return MoveType.NOT_AVAILABLE
            else: 

                if self.move_validator._want_to_castle(prev_cell_name, next_cell_name):
                    king = self.board_status.board[prev_cell_name]
                    if not self.move_validator._is_king_in_check(king.type):
                        self._castle(prev_cell_name, next_cell_name)
                        move.type = MoveType.CASTLE
                    else:
                        return MoveType.NOT_AVAILABLE
                else:
                    can_kill_passant = self.move_validator._can_kill_passant(prev_cell_name, next_cell_name)
                    Board_Utils.move_piece_in_board(self.board_status.board, prev_cell_name, next_cell_name, self.board_status.turn, can_kill_passant)
                    self._manage_passant(prev_cell_name, next_cell_name)
                    if can_kill_passant:
                        return MoveType.PASSANT_PAWN
                    if self.move_validator._pawn_ascension(next_cell_name):
                        return MoveType.PAWN_ASCENSION

                self.move_validator.update_king_cell(next_cell_name, self.board_status.turn)

                end_game = self.move_validator.is_end_game()
                if end_game:
                    return end_game
                
        return move.type

    def move_to_cell(self, next_cell_name: str) -> None:
        piece = self.board_status.board[next_cell_name]
        if not piece.has_moved:
            piece.has_moved = True 

        self._switch_turn()
        
    def can_color_play(self, cell_name: str) -> bool:
        prev_cell_piece = self.board_status.board[cell_name]
        return prev_cell_piece.type == self.board_status.turn
    
    def _switch_turn(self) -> None:
        self.board_status.turn = "b" if self.board_status.turn == "w" else "w"

    #Methods related to passant pawn
    def _manage_passant(self, prev_cell_name: str, next_cell_name: str) -> bool:
        self._restore_passant()
        self._make_pawn_passant(prev_cell_name, next_cell_name)
            
    def _make_pawn_passant(self, prev_cell_name: str, next_cell_name: str) -> bool:
        pawn = self.board_status.board.get(next_cell_name)
        if not isinstance(pawn, Pawn): return
        pawn.is_passant = pawn.is_two_steps_move(prev_cell_name, next_cell_name)

    def _restore_passant(self) -> None:
        for piece in self.board_status.board.values():
            if isinstance(piece, Pawn) and piece.type == self.board_status.turn:
                piece.is_passant = False
    #End of passant pawn related methods
    #Pawn ascension related methods
    def ascension_pieces(self):
        turn = self.board_status.turn
        return [Queen(turn, self.board_status), Knight(turn, self.board_status), Rook(turn, self.board_status), Bishop(turn, self.board_status)]
    
    def complete_promotion(self, cell_name, piece):
        self.board_status.board[cell_name] = piece
    
    #Castle related methods
    def _castle(self, prev_cell: str, next_cell: str) -> None:
        king = self.board_status.board[prev_cell]
        self.board_status.board[next_cell] = king
        del self.board_status.board[prev_cell]

        row, col = Cell_utils.map_cell_to_index(next_cell)

        rook1_cell_name = Cell_utils.map_index_to_cell(row, col + 1)
        next_rook_cell_name = Cell_utils.map_index_to_cell(row, col - 1)
        if self._castle_rook(rook1_cell_name, next_rook_cell_name): return

        rook2_cell_name = Cell_utils.map_index_to_cell(row, col - 2)
        next_rook_cell_name = Cell_utils.map_index_to_cell(row, col + 1)
        self._castle_rook(rook2_cell_name, next_rook_cell_name)

    def _castle_rook(self, rook_cell_name: str, next_rook_cell_name: str) -> bool:
        rook = self.board_status.board.get(rook_cell_name)
        if rook is not None and not rook.has_moved:
            self.board_status.board[next_rook_cell_name] = rook
            del self.board_status.board[rook_cell_name]
            return True
        return False
    #End castle related methods