from ..BoardStatus import BoardStatus
from Board.Pieces import King
from Utils.Cell_utils import map_cell_to_index, map_index_to_cell


class CastleLogic:
    def __init__(self, board : BoardStatus) -> None:
        self.board_status = board

    def want_to_castle(self, prev_cell_name: str, next_cell_name: str) -> bool:
        prev_piece = self.board_status[prev_cell_name]
        if isinstance(prev_piece, King):
            possible_moves = prev_piece.possible_moves(prev_cell_name)

            if next_cell_name in possible_moves:
                prev_col = map_cell_to_index(prev_cell_name)[1]
                next_col = map_cell_to_index(next_cell_name)[1]
                return abs(prev_col - next_col) == 2
        return False
    
    def castle(self, prev_cell: str, next_cell: str) -> None:
        king = self.board_status[prev_cell]
        self.board_status[next_cell] = king
        del self.board_status[prev_cell]

        row, col = map_cell_to_index(next_cell)

        rook1_cell_name = map_index_to_cell(row, col + 1)
        next_rook_cell_name = map_index_to_cell(row, col - 1)
        if self._castle_rook(rook1_cell_name, next_rook_cell_name): return

        rook2_cell_name = map_index_to_cell(row, col - 2)
        next_rook_cell_name = map_index_to_cell(row, col + 1)
        self._castle_rook(rook2_cell_name, next_rook_cell_name)

    def _castle_rook(self, rook_cell_name: str, next_rook_cell_name: str) -> bool:
        rook = self.board_status.get(rook_cell_name)
        if rook is not None and not rook.has_moved:
            self.board_status[next_rook_cell_name] = rook
            del self.board_status[rook_cell_name]
            return True
        return False