from __future__ import annotations #This imports are required to avoid circular dependency and 
from typing import TYPE_CHECKING   #provide type hints safely
if TYPE_CHECKING:
    from Board.BoardStatus import BoardStatus



#Since the board is drawn from top to bottom, the row number has to be adjusted accordingly
def map_cell_to_index(cell_name: str) -> tuple[int, int]:
    column: int = ord(cell_name[0]) - 97
    row: int = int(cell_name[1])
    adj_row: int = abs(row - 8)
    return adj_row, column


def map_index_to_cell(row: int, column: int) -> str:
    adj_row = abs(row - 8)
    column_letter = chr(column + 97)
    cell_name = f"{column_letter}{str(adj_row)}"
    return cell_name


def is_cell_empty(cell_name: str, board: BoardStatus) -> bool:
    return cell_name not in board


def are_teammates(prev_cell_name: str, next_cell_name: str, board: BoardStatus) -> bool:
    prev_piece = board[prev_cell_name]
    next_piece = board[next_cell_name]
    return prev_piece.type == next_piece.type


def get_passant_cell(cell_name: str, turn: str) -> str:
    row, col = map_cell_to_index(cell_name)
    direction = 1 if turn == "w" else -1
    passant_cell_name = map_index_to_cell(row + direction, col)
    return passant_cell_name


def is_cell_centered(cell_name: str) -> bool:
    _, col = map_cell_to_index(cell_name)
    return 2 <= col <= 5


def is_cell_advanced(cell_name: str, board: BoardStatus) -> bool:
    row, _ = map_cell_to_index(cell_name)
    return (board.turn == 'w' and row < 3) or (board.turn == 'b' and row > 4)