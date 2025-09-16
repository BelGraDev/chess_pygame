from Pieces.Pawn import Pawn
from Pieces.King import King
from Utils.Cell_utils import Cell_utils
from Utils.Board_Utils import Board_Utils
from .Move import MoveType
class MoveValidator:
    
    def __init__(self, board):
        self.board_status = board

    def _is_valid_move(self, prev_cell_name: str, next_cell_name: str) -> bool:
        board = self.board_status.board
        can_kill_passant = self._can_kill_passant(prev_cell_name, next_cell_name)

        if can_kill_passant:
            passant_cell = Cell_utils.get_passant_cell(next_cell_name, self.board_status.turn)
            original_next_piece = board.get(passant_cell)
            next_piece_cell_name = passant_cell
        else: 
            original_next_piece = board.get(next_cell_name)
            next_piece_cell_name = next_cell_name

        prev_piece = Board_Utils.move_piece_in_board(board, prev_cell_name, next_cell_name, self.board_status.turn, can_kill_passant)

        if prev_piece is not None:
            prev_piece_color = prev_piece.type
            self.update_king_cell(next_cell_name, prev_piece_color)

            king_is_in_check = self._is_king_in_check(prev_piece_color)

            Board_Utils.restore_last_state(board, prev_piece, original_next_piece, prev_cell_name, next_piece_cell_name, next_cell_name)
            
            self.update_king_cell(prev_cell_name, prev_piece_color)
            return not king_is_in_check
        else:
            return False
    
    def update_king_cell(self, cell_name: str, king_color: str) -> None:
        piece = self.board_status.board[cell_name]
        if isinstance(piece, King):
            if king_color == "w":
                self.board_status.w_king_cell = cell_name
            else:
                self.board_status.b_king_cell = cell_name

    def is_end_game(self) -> None | MoveType:
        opponent_color: str = "b" if self.board_status.turn == "w" else "w"
        for cell_name, piece in list(self.board_status.board.items()):
            if piece.type == opponent_color:
                possible_moves: list[str] = piece.possible_moves(cell_name)
                for move in possible_moves:
                    is_valid: bool = self._is_valid_move(cell_name, move)
                    if is_valid:
                        return None
        end_game = MoveType.CHECK_MATE if self._is_king_in_check(opponent_color) else MoveType.TIE
        self.board_status.is_end_game = True
        return end_game

    def _is_king_in_check(self, king_color: str) -> bool:
            king_cell = self.board_status.w_king_cell if king_color == "w" else self.board_status.b_king_cell
            king = self.board_status.board[king_cell]
            return king.is_on_check(king_cell)
    
    def _want_to_castle(self, prev_cell_name: str, next_cell_name: str) -> bool:
        prev_piece = self.board_status.board[prev_cell_name]
        if isinstance(prev_piece, King):
            possible_moves = prev_piece.possible_moves(prev_cell_name)

            if next_cell_name in possible_moves:
                prev_col = Cell_utils.map_cell_to_index(prev_cell_name)[1]
                next_col = Cell_utils.map_cell_to_index(next_cell_name)[1]
                return abs(prev_col - next_col) == 2
        return False
        
    def _pawn_ascension(self, cell_name):
        row = Cell_utils.map_cell_to_index(cell_name)[0]
        piece = self.board_status.board[cell_name]
        is_on_top = row == 7 or row == 0
        if isinstance(piece, Pawn) and is_on_top:
            return True
        return False

    def _can_kill_passant(self, prev_cell_name: str, next_cell_name: str) -> bool:
        pawn = self.board_status.board.get(prev_cell_name)
        if not isinstance(pawn, Pawn): return False
        passant_cell_name = Cell_utils.get_passant_cell(next_cell_name, self.board_status.turn)
        passant = self.board_status.board.get(passant_cell_name)
        return isinstance(passant, Pawn) and passant.is_passant and not Cell_utils.are_teammates(prev_cell_name, passant_cell_name, self.board_status.board)