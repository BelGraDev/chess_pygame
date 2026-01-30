from Board.BoardStatus import BoardStatus, PieceColor
from Utils.Board_Utils import restore_last_state
from Board.Move import Step
from typing import Callable, Optional

class AILogic:

    MAX_DEPTH = 2
    def __init__(self, board: BoardStatus, p_turn: PieceColor, a_turn: PieceColor) -> None:
        self.board = board
        self.player_turn = p_turn
        self.ai_turn = a_turn

    def get_best_ai_move(self) -> Optional[Step]:
        best_score = float('-inf')
        alpha = float('-inf')
        beta = float('inf')
        best_move: Optional[Step] = None

        for cell, piece in self.board.items():
            if piece.type == self.ai_turn:
                possible_moves = piece.possible_moves(cell)
                if possible_moves:
                    for move_cell in possible_moves:
                        move_step = Step(cell, move_cell)
                        original_next_piece = self.board.get(move_cell)
                        self.board[move_cell] = piece
                        score = minimax(self.board, 0, self.MAX_DEPTH, False, alpha, beta, self.ai_turn, self.player_turn)
                        restore_last_state(self.board, piece, original_next_piece, move_cell, move_step)

                        if score > best_score:
                            best_score = score
                            best_move = move_step
        return best_move

def minimax(board: BoardStatus, depth: int,  max_depth: int, is_maximizing: bool, alpha: float, beta: float, ai_turn: PieceColor, player_turn: PieceColor) -> float:
    if board.end_game is not None:
        return board.end_game

    if depth == max_depth:
        return board.evaluate_board_status(ai_turn)
    
    best_score = compute_score(board, depth, max_depth, is_maximizing, max if is_maximizing else min, alpha, beta, ai_turn, player_turn)

    return best_score

def compute_score(board: BoardStatus, depth: int, max_depth: int, is_maximizing: bool, min_max_func: Callable[[float, float],float], alpha: float, beta: float, ai_turn: PieceColor, player_turn: PieceColor) -> float:
    best_score = float('-inf') if is_maximizing else float('inf')
    current_turn = ai_turn if is_maximizing else player_turn

    for cell, piece in list(board.items()):
        if piece.type == current_turn:
            possible_moves = piece.possible_moves(cell)
            if possible_moves:
                for move_cell in possible_moves:
                    original_next_piece = board.get(move_cell)
                    board[move_cell] = piece
                    score = minimax(board, depth + 1, max_depth, not is_maximizing, alpha, beta, ai_turn, player_turn)
                    restore_last_state(board, piece, original_next_piece, move_cell, Step(cell, move_cell))
                    best_score = min_max_func(score, best_score)
                    if is_maximizing:
                        alpha = max(alpha, best_score)
                    else:
                        beta = min(beta, best_score)
                    if beta <= alpha: return best_score

    return best_score
