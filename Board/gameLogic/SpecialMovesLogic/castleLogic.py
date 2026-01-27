from Board import BoardStatus
from Board.Pieces import King
from Board.Move import Step
from Utils.Cell_utils import map_cell_to_index, map_index_to_cell

def want_to_castle(board: BoardStatus, step: Step) -> bool:
    prev_piece = board[step.start_cell]
    if isinstance(prev_piece, King):
        possible_moves = prev_piece.possible_moves(step.start_cell)

        if step.end_cell in possible_moves:
            _ , prev_col = map_cell_to_index(step.start_cell)
            _ , next_col = map_cell_to_index(step.end_cell)
            return abs(prev_col - next_col) == 2
    return False


def castle(board: BoardStatus, step: Step) -> None:
    king = board[step.start_cell]
    board[step.end_cell] = king
    del board[step.start_cell]

    row, col = map_cell_to_index(step.end_cell)

    rook1_cell_name = map_index_to_cell(row, col + 1)
    next_rook_cell_name = map_index_to_cell(row, col - 1)
    if _castle_rook(board, Step(rook1_cell_name, next_rook_cell_name)): return

    rook2_cell_name = map_index_to_cell(row, col - 2)
    next_rook_cell_name = map_index_to_cell(row, col + 1)
    _castle_rook(board, Step(rook2_cell_name, next_rook_cell_name))


def _castle_rook(board: BoardStatus, step: Step) -> bool:
    rook = board.get(step.start_cell)
    if rook is not None and not rook.has_moved:
        board[step.end_cell] = rook
        del board[step.start_cell]
        return True
    return False