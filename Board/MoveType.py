from enum import Enum

class MoveType(Enum):

    EMPTY_CELL = 0
    CAPTURE = 1
    TEAMMATE = 2