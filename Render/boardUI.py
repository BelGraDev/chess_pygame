from .ui import UI
from Utils.Cell_utils import map_index_to_cell, map_cell_to_index
from Utils.View_utils import redraw_cell_piece, redraw_cell
import pygame
from Board.Pieces import Piece
from Board import BoardStatus, PieceColor
from .boardCells import Cell, BoardCells


class BoardUI(UI):
    def __init__(self, screen: pygame.Surface, cells: BoardCells, ascension_cells: list[str]):
        self.screen = screen
        self.board_cells = cells
        self.ascension_cells = ascension_cells


    def init_board(self) -> None:
        background = pygame.image.load("Render/images/background2.png")
        self.screen.blit(background, (0,0))
        for row in range(8):
            for col in range(8):
                cell = self.board_cells[row, col]
                pygame.draw.rect(self.screen, cell.color, cell)
        self.render_border()


    def init_pieces(self, board: BoardStatus) -> None:
        for cell_name, piece in board.items():
            rect = self.board_cells[cell_name]
            self.screen.blit(piece.image, rect)


    def render_border(self) -> None:
        border = pygame.Rect(self.MARGIN_SIZE, self.MARGIN_SIZE, self.BOARD_WIDTH, self.BOARD_HEIGHT)
        pygame.draw.rect(self.screen, self.BORDER_COLOR, border,  2)

    def render_pawn_ascension(self, cell_name: str, turn: str, pieces: list[Piece]) -> None:
        self.ascension_cells.clear()
        row, col = map_cell_to_index(cell_name)
        direction = 1 if turn == PieceColor.WHITE else -1
        
        for r, piece in zip(range(row, row + (len(pieces) * direction), direction), pieces):
            cell_name = map_index_to_cell(r, col)
            self.ascension_cells.append(cell_name)
            self._draw_ascension_cell(piece, cell_name)

    def draw_possible_move(self, cell_name: str) -> None:
        image = pygame.image.load("Render/images/move.png").convert_alpha()
        cell = self.board_cells[cell_name]
        image_rect = image.get_rect(center= cell.center)
        self.screen.blit(image, image_rect)

    def _draw_ascension_cell(self, piece: Piece, cell_name: str) -> None:
        cell = self.board_cells[cell_name]
        redraw_cell_piece(self.screen, self.ASCENSION_CELL_COLOR, piece, cell)

    def draw_highlight(self, piece: Piece, cell_name: str) -> None:
        cell = self.board_cells[cell_name]
        redraw_cell_piece(self.screen, self.HIGHLIGHT_COLOR, piece, cell)
    
    def draw_replacement_pieces(self, piece: Piece, cell_name: str) -> None:
        cell = self.board_cells[cell_name]
        redraw_cell_piece(self.screen, cell.color, piece, cell)

    
    def draw_empty_cell(self, cell_name: str) -> None:
        cell = self.board_cells[cell_name]
        redraw_cell(self.screen, cell)


    def draw_piece(self, piece: Piece, cell: Cell) -> None:
        redraw_cell_piece(self.screen, cell.color, piece, cell)