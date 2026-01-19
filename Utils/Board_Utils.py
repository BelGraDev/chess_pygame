from .Cell_utils import get_passant_cell
from Board.Pieces import Piece

def move_piece_in_board(board: dict[str, Piece], prev_cell_name: str, next_cell_name: str, turn: str, can_kill_passant: bool) -> Piece | None:
    prev_piece = board[prev_cell_name]
    possible_moves = prev_piece.possible_moves(prev_cell_name)
    if next_cell_name in possible_moves:

        board[next_cell_name] = prev_piece
        del board[prev_cell_name]
        if can_kill_passant:
            _kill_passant(board, next_cell_name, turn)

        return prev_piece
    return None

def restore_last_state(board: dict[str, Piece], prev_piece: Piece, original_next_piece: Piece | None, prev_cell_name: str, next_piece_cell_name: str, next_cell_name: str) -> None:
    board[prev_cell_name] = prev_piece
    if original_next_piece is not None:
        board[next_piece_cell_name] = original_next_piece
        if next_piece_cell_name != next_cell_name:
            del board[next_cell_name]
    else:
        del board[next_piece_cell_name]
    
def _kill_passant(board: dict[str, Piece], cell_name: str, turn: str) -> None:
    passant_cell = get_passant_cell(cell_name, turn)
    del board[passant_cell]
