from Utils.Cell_utils import get_passant_cell
from Utils.Board_Utils import move_piece_in_board, restore_last_state
from .SpecialMovesLogic import CastleLogic, PassantLogic
from .BoardStatus import BoardStatus

class MoveValidator:
    

    def __init__(self, board: BoardStatus):
        self.board_status = board
        self.castleLogic = CastleLogic(board)
        self.passantLogic = PassantLogic(board)


    def is_valid_move(self, prev_cell_name: str, next_cell_name: str) -> bool:
        board = self.board_status.board
        can_kill_passant = self.passantLogic.can_kill_passant(prev_cell_name, next_cell_name)

        if can_kill_passant:
            passant_cell = get_passant_cell(next_cell_name, self.board_status.turn)
            original_next_piece = self.board_status.get(passant_cell)
            next_piece_cell_name = passant_cell
        else: 
            original_next_piece = self.board_status.get(next_cell_name)
            next_piece_cell_name = next_cell_name

        prev_piece = move_piece_in_board(board, prev_cell_name, next_cell_name, self.board_status.turn, can_kill_passant)

        if prev_piece is not None:
            prev_piece_color = prev_piece.type
            self.board_status.update_king_cell(next_cell_name, prev_piece_color)

            king_is_in_check = self.board_status.is_king_in_check(prev_piece_color)

            restore_last_state(board, prev_piece, original_next_piece, prev_cell_name, next_piece_cell_name, next_cell_name)
            
            self.board_status.update_king_cell(prev_cell_name, prev_piece_color)
            return not king_is_in_check
        else:
            return False
    
