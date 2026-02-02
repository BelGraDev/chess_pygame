import chess_engine.utils.constants as constants
from utils.fen_strings import parse_fen
import numpy as np

class Board:

    def __init__(self, fen_string: str = constants.STARTING_POSITION):
        _board, self.turn = parse_fen(fen_string)
        self.board = np.array(_board, dtype=np.int64)
        self.num_pieces = constants.NUM_PIECES

board= Board()
print(board.board)