
import pygame
import chess_ui.utils.ui as ui
from .board_cells import BoardCells
from .utils.fen_strings import get_index_image
from .utils.constants import STARTING_POSITION, NUM_CELLS


class ChessUI():
    def __init__(self, screen: pygame.Surface, board_arrangment: str = STARTING_POSITION):
        self.screen = screen
        self.board_cells = BoardCells()
        self.board_arrangment = board_arrangment


    def init_board(self) -> None:
        background = pygame.image.load(f'{ui.IMAGES_PATH}/background2.png')
        self.screen.blit(background, (0,0))
        for index in range(NUM_CELLS):
            cell = self.board_cells[index]
            pygame.draw.rect(self.screen, cell.color, cell)
        self.render_border()


    def init_pieces(self) -> None:
        for index, piece_image in get_index_image(self.board_arrangment):
            rect = self.board_cells[index]
            self.screen.blit(piece_image, rect)


    def render_border(self) -> None:
        border = pygame.Rect(ui.MARGIN_SIZE, ui.MARGIN_SIZE, ui.BOARD_WIDTH, ui.BOARD_HEIGHT)
        pygame.draw.rect(self.screen, ui.BORDER_COLOR, border,  2)
