from chess_engine.utils.enums import PieceType, Color

OFFSET_MARGIN = [PieceType.OFF_BOARD]
CODE_PIECES = set('rnbqkp')
PIECE_DICT = {
    'r': (PieceType.B_ROOK, PieceType.W_ROOK),
    'b': (PieceType.B_BISHOP, PieceType.W_BISHOP),
    'k': (PieceType.B_KING, PieceType.W_KING),
    'n': (PieceType.B_KNIGHT, PieceType.W_KNIGHT),
    'p': (PieceType.B_PAWN, PieceType.W_PAWN),
    'q': (PieceType.B_QUEEN, PieceType.W_QUEEN)
}


def parse_fen(fen_string: str) -> tuple[list[int], Color]:
    fen_components = fen_string.split(' ')
    pieces = fen_components[0]
    turn = Color(fen_components[1])
    board_offset: list[int] = [PieceType.OFF_BOARD] * 20
    board = board_offset + OFFSET_MARGIN

    for letter in pieces:
        if (lower_letter:=letter.lower()) in CODE_PIECES:
            board.append(_to_piece(lower_letter, letter.isupper()))
        elif letter.isnumeric():
            board += [PieceType.EMPTY_SPACE] * int(letter)
        elif letter == '/':
            board += OFFSET_MARGIN * 2
    board += OFFSET_MARGIN
    board += board_offset
    return board, turn


def _to_piece(letter: str, is_upper: bool) -> int:
    return PIECE_DICT[letter][int(is_upper)]