from enum import Enum

class MoveType(Enum):

    NOT_AVAILABLE = -1
    EMPTY_CELL = 0
    CAPTURE = 1
    TEAMMATE = 2