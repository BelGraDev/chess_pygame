from .Cell_utils import get_passant_cell
from Board.Pieces import Piece
from Board import BoardStatus
from Board.Move import Step

def move_piece_in_board(board: BoardStatus, step: Step,  can_kill_passant: bool) -> Piece | None:
    prev_piece = board[step.start_cell]
    possible_moves = prev_piece.possible_moves(step.start_cell)
    if step.end_cell in possible_moves:

        board[step.end_cell] = prev_piece
        del board[step.start_cell]
        if can_kill_passant:
            _kill_passant(board, step.end_cell, board.turn)

        return prev_piece
    return None

def restore_last_state(board: BoardStatus, prev_piece: Piece, original_next_piece: Piece | None, next_piece_cell_name: str, step: Step) -> None:
    board[step.start_cell] = prev_piece
    if original_next_piece is not None:
        board[next_piece_cell_name] = original_next_piece
        if next_piece_cell_name != step.end_cell:
            del board[step.end_cell]
    else:
        del board[next_piece_cell_name]
    
def _kill_passant(board: BoardStatus, cell_name: str, turn: str) -> None:
    passant_cell = get_passant_cell(cell_name, turn)
    del board[passant_cell]
