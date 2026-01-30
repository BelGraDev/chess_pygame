from Board.BoardStatus import BoardStatus
from Utils.Cell_utils import map_cell_to_index, map_index_to_cell
import numpy as np

def to_numpy(board: BoardStatus):
    efficient_board = np.zeros((8,8))
    return efficient_board