from Board.BoardStatus import BoardStatus, PieceColor
from Board.gameLogic.MoveValidator import is_valid_move
from Utils.Board_Utils import restore_last_state
from Board.Move import Step
from typing import Callable, Optional

class AILogic:
    def __init__(self, board: BoardStatus, p_turn: PieceColor, a_turn: PieceColor) -> None:
        self.board = board
        self.player_turn = p_turn
        self.ai_turn = a_turn

    def get_best_ai_move(self) -> Optional[Step]:
        best_score = float('-inf')
        best_move: Optional[Step] = None

        for cell, piece in self.board.items():
            if piece.type == self.ai_turn:
                for move_cell in piece.possible_moves(cell):
                    move_step = Step(cell, move_cell)
                    original_next_piece = self.board.get(move_cell)
                    score = self._minimax(0, False)
                    restore_last_state(self.board, piece, original_next_piece, move_cell, move_step)

                    if score > best_score:
                        best_score = score
                        best_move = move_step
        return best_move

    def _minimax(self, depth: int, is_maximizing: bool) -> float:
        if self.board.end_game is not None:
            return self.board.end_game
        if is_maximizing:
            best_score = self._compute_score(depth, is_maximizing, max)
        else:
            best_score = self._compute_score(depth, is_maximizing, min)
        return best_score
    
    def _compute_score(self, depth: int, is_maximizing: bool, min_max_func: Callable[[float, float], float]) -> float:
        best_score = float('-inf') if is_maximizing else float('inf')
        current_turn = self.ai_turn if is_maximizing else self.player_turn

        for cell, piece in self.board.items():
            if piece.type == current_turn:
                for move_cell in piece.possible_moves(cell):
                    original_next_piece = self.board.get(move_cell)
                    self.board[move_cell] = piece
                    score = self._minimax(depth + 1, not is_maximizing)
                    restore_last_state(self.board, piece, original_next_piece, move_cell, Step(cell, move_cell))
                    best_score = min_max_func(score, best_score)

        return best_score


def get_best_ai_move(board: BoardStatus, ai_turn: str)  -> tuple[str, str] | None:
    for cell, piece in board.items():
        if piece.type == ai_turn:
            possible_moves = piece.possible_moves(cell)
            if possible_moves:
                next_cell = possible_moves[0]
                if is_valid_move(board, Step(cell, next_cell)):
                    return cell, next_cell
    return None