from __future__ import annotations
from typing import TYPE_CHECKING
from .Cell_utils import map_cell_to_index, map_index_to_cell
from Board import PieceColor

if TYPE_CHECKING:
    from Board import BoardStatus
    from Board.Pieces import Piece
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


def is_cell_empty(cell_name: str, board: BoardStatus) -> bool:
    return cell_name not in board


def are_teammates(prev_cell_name: str, next_cell_name: str, board: BoardStatus) -> bool:
    prev_piece = board[prev_cell_name]
    next_piece = board[next_cell_name]
    return prev_piece.type == next_piece.type


def get_passant_cell(cell_name: str, turn: str) -> str:
    row, col = map_cell_to_index(cell_name)
    direction = 1 if turn == PieceColor.WHITE else -1
    passant_cell_name = map_index_to_cell(row + direction, col)
    return passant_cell_name


def is_cell_centered(cell_name: str) -> bool:
    _, col = map_cell_to_index(cell_name)
    return 2 <= col <= 5


def is_cell_advanced(cell_name: str, board: BoardStatus) -> bool:
    row, _ = map_cell_to_index(cell_name)
    return (board.turn == PieceColor.WHITE and row < 3) or (board.turn == PieceColor.BLACK and row > 4)

    
def _kill_passant(board: BoardStatus, cell_name: str, turn: str) -> None:
    passant_cell = get_passant_cell(cell_name, turn)
    del board[passant_cell]
