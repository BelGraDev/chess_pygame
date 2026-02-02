import chess_ui.utils.ui as ui
from typing import Generator
from pygame import Surface, image

CODE_PIECES = set('rnbqkp')
PIECE_IMAGE_PATH = f'{ui.IMAGES_PATH}/pieces/'
PIECE_IMAGE_DICT = {
    'r': ('b_rook.png'  , 'w_rook.png'),
    'b': ('b_bishop.png', 'w_bishop.png'),
    'k': ('b_king.png'  , 'w_king.png'),
    'n': ('b_knight.png', 'w_knight.png'),
    'p': ('b_pawn.png'  , 'w_pawn.png'),
    'q': ('b_queen.png' , 'w_queen.png')
}


def get_index_image(fen_string: str) -> Generator[tuple[int, Surface], None, None]:
    board = fen_string.split(' ')[0].replace('/', '')

    index = 0
    for letter in board:
        if (lower_letter:=letter.lower()) in CODE_PIECES:
            yield index, _get_image(lower_letter, letter.isupper())
            index +=1
        elif letter.isnumeric():
            index += int(letter)


def _get_image(letter: str, is_upper: bool) -> Surface:
    return image.load(f'{PIECE_IMAGE_PATH}{PIECE_IMAGE_DICT[letter][int(is_upper)]}')

