from enum import IntEnum, Enum

class PieceType(IntEnum):
    W_PAWN = 1
    W_KNIGHT = 2
    W_BISHOP = 3
    W_ROOK = 4
    W_QUEEN = 5
    W_KING = 6
    B_PAWN = -1
    B_KNIGHT = -2
    B_BISHOP = -3
    B_ROOK = -4
    B_QUEEN = -5
    B_KING = -6
    EMPTY_SPACE = 0
    OFF_BOARD = 99

class Color(Enum):
    WHITE = 'w'
    BLACK = 'b'