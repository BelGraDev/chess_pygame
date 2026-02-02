from Utils.Board_Utils import move_piece_in_board, restore_last_state, get_passant_cell
from .SpecialMovesLogic import can_kill_passant
from Board.Move import Step
from Board import BoardStatus



def is_valid_move(board: BoardStatus, step: Step) -> bool:
    _can_kill_passant = can_kill_passant(board, step)

    if _can_kill_passant:
        passant_cell = get_passant_cell(step.end_cell, board.turn)
        original_next_piece = board.get(passant_cell)
        next_piece_cell_name = passant_cell
    else: 
        original_next_piece = board.get(step.end_cell)
        next_piece_cell_name = step.end_cell

    prev_piece = move_piece_in_board(board, step, _can_kill_passant)

    if prev_piece is not None:
        prev_piece_color = prev_piece.type
        board.update_king_cell(step.end_cell, prev_piece_color)

        king_is_in_check = board.is_king_in_check(prev_piece_color)

        restore_last_state(board, prev_piece, original_next_piece, next_piece_cell_name, step)
        
        board.update_king_cell(step.start_cell, prev_piece_color)
        return not king_is_in_check
    else:
        return False

