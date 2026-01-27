from Board import BoardStatus
from Board.Pieces import Pawn
from Utils.Cell_utils import are_teammates, get_passant_cell
from Board.Move import Step


def manage_passant(board: BoardStatus, step: Step) -> None:
    _restore_passant(board)
    _make_pawn_passant(board, step)


def can_kill_passant(board: BoardStatus, step: Step) -> bool:
    pawn = board.get(step.start_cell)
    if not isinstance(pawn, Pawn): 
        return False
    passant_cell_name = get_passant_cell(step.end_cell, board.turn)
    passant = board.get(passant_cell_name)
    return isinstance(passant, Pawn) and passant.is_passant and not are_teammates(step.start_cell, passant_cell_name, board)

        
def _make_pawn_passant(board: BoardStatus, step: Step) -> None:
    pawn = board.get(step.end_cell)
    if not isinstance(pawn, Pawn): 
        return
    pawn.is_passant = pawn.is_two_steps_move(step)


def _restore_passant(board: BoardStatus) -> None:
    for piece in board.values():
        if isinstance(piece, Pawn) and piece.type == board.turn:
            piece.is_passant = False