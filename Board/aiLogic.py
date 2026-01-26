from Board.BoardStatus import BoardStatus
from Board.MoveValidator import is_valid_move
from Board.Move import Step
from typing import Optional


def get_best_ai_move(board: BoardStatus, ai_turn: str)  -> Optional[tuple[str, str]]:
    for cell, piece in board.items():
        if piece.type == ai_turn:
            possible_moves = piece.possible_moves(cell)
            if possible_moves:
                next_cell = possible_moves[0]
                if is_valid_move(board, Step(cell, next_cell)):
                    del board[cell]
                    board[next_cell] = piece
                    return cell, next_cell
    return None