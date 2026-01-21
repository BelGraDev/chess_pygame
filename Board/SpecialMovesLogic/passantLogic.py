from ..BoardStatus import BoardStatus
from Board.Pieces import Pawn
from Utils.Cell_utils import are_teammates, get_passant_cell

class PassantLogic:
    def __init__(self, board: BoardStatus) -> None:
        self.board_status = board


    def manage_passant(self, prev_cell_name: str, next_cell_name: str) -> None:
        self._restore_passant()
        self._make_pawn_passant(prev_cell_name, next_cell_name)


    def can_kill_passant(self, prev_cell_name: str, next_cell_name: str) -> bool:
        pawn = self.board_status.get(prev_cell_name)
        if not isinstance(pawn, Pawn): 
            return False
        passant_cell_name = get_passant_cell(next_cell_name, self.board_status.turn)
        passant = self.board_status.get(passant_cell_name)
        return isinstance(passant, Pawn) and passant.is_passant and not are_teammates(prev_cell_name, passant_cell_name, self.board_status)
    
            
    def _make_pawn_passant(self, prev_cell_name: str, next_cell_name: str) -> None:
        pawn = self.board_status.get(next_cell_name)
        if not isinstance(pawn, Pawn): 
            return
        pawn.is_passant = pawn.is_two_steps_move(prev_cell_name, next_cell_name)


    def _restore_passant(self) -> None:
        for piece in self.board_status.values():
            if isinstance(piece, Pawn) and piece.type == self.board_status.turn:
                piece.is_passant = False