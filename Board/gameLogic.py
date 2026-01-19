from .BoardStatus import BoardStatus
from .MoveValidator import MoveValidator
from .Pieces import Pawn, Piece
from .Move import MoveType
from Utils.Cell_utils import map_cell_to_index

class GameLogic:
    
    def __init__(self, board: BoardStatus):
        self.board_status = board
        self.move_validator = MoveValidator(board)


    def can_color_play(self, cell_name: str) -> bool:
        prev_cell_piece = self.board_status[cell_name]
        return prev_cell_piece.type == self.board_status.turn
    
        
    def move_to_cell(self, next_cell_name: str) -> None:
        piece = self.board_status[next_cell_name]
        if not piece.has_moved:
            piece.has_moved = True 

        self.board_status.switch_turn()
    
        
    def pawn_ascension(self, cell_name: str):
        row = map_cell_to_index(cell_name)[0]
        piece = self.board_status[cell_name]
        is_on_top = row == 7 or row == 0
        if isinstance(piece, Pawn) and is_on_top:
            return True
        return False
    

    def complete_promotion(self, cell_name: str, piece: Piece) -> None:
        self.board_status[cell_name] = piece


    def is_end_game(self) -> None | MoveType:
        opponent_color: str = "b" if self.board_status.turn == "w" else "w"
        for cell_name, piece in list(self.board_status.board.items()):
            if piece.type == opponent_color:
                possible_moves = piece.possible_moves(cell_name)
                for move in possible_moves:
                    is_valid = self.move_validator.is_valid_move(cell_name, move)
                    if is_valid:
                        return None
        end_game = MoveType.CHECK_MATE if self.board_status.is_king_in_check(opponent_color) else MoveType.TIE
        self.board_status.is_end_game = True
        return end_game
    
