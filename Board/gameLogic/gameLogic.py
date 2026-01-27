from Board import BoardStatus, PieceColor
from .MoveValidator import is_valid_move
from Board.Pieces import Pawn, Piece
from Board.Move import MoveType, Step
from Utils.Cell_utils import map_cell_to_index


def can_color_play(board: BoardStatus, cell_name: str) -> bool:
    prev_cell_piece = board[cell_name]
    return prev_cell_piece.type == board.turn

    
def move_to_cell(board: BoardStatus, next_cell_name: str) -> None:
    piece = board[next_cell_name]
    if not piece.has_moved:
        piece.has_moved = True 

    board.switch_turn()

    
def pawn_ascension(board: BoardStatus, cell_name: str):
    row = map_cell_to_index(cell_name)[0]
    piece = board[cell_name]
    is_on_top = row == 7 or row == 0
    if isinstance(piece, Pawn) and is_on_top:
        return True
    return False


def complete_promotion(board: BoardStatus, cell_name: str, piece: Piece) -> None:
    board[cell_name] = piece


def is_end_game(board: BoardStatus) -> None | MoveType:
    opponent_color: str = PieceColor.BLACK if board.turn == PieceColor.WHITE else PieceColor.WHITE
    for cell_name, piece in list(board.items()):
        if piece.type == opponent_color:
            possible_moves = piece.possible_moves(cell_name)
            for move in possible_moves:
                is_valid = is_valid_move(board, Step(cell_name, move))
                if is_valid:
                    return None
    end_game = MoveType.CHECK_MATE if board.is_king_in_check(opponent_color) else MoveType.TIE
    board.is_end_game = True
    return end_game

