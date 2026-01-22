from Utils.Cell_utils import get_passant_cell
from Utils.Board_Utils import move_piece_in_board, restore_last_state
from .SpecialMovesLogic import CastleLogic, PassantLogic
from .Move import Step
from .BoardStatus import BoardStatus

class MoveValidator:
    

    def __init__(self, board: BoardStatus):
        self.board_status = board
        self.castleLogic = CastleLogic(board)
        self.passantLogic = PassantLogic(board)


    def is_valid_move(self, step: Step) -> bool:
        can_kill_passant = self.passantLogic.can_kill_passant(step)

        if can_kill_passant:
            passant_cell = get_passant_cell(step.end_cell, self.board_status.turn)
            original_next_piece = self.board_status.get(passant_cell)
            next_piece_cell_name = passant_cell
        else: 
            original_next_piece = self.board_status.get(step.end_cell)
            next_piece_cell_name = step.end_cell

        prev_piece = move_piece_in_board(self.board_status, step, can_kill_passant)

        if prev_piece is not None:
            prev_piece_color = prev_piece.type
            self.board_status.update_king_cell(step.end_cell, prev_piece_color)

            king_is_in_check = self.board_status.is_king_in_check(prev_piece_color)

            restore_last_state(self.board_status, prev_piece, original_next_piece, next_piece_cell_name, step)
            
            self.board_status.update_king_cell(step.start_cell, prev_piece_color)
            return not king_is_in_check
        else:
            return False
    
