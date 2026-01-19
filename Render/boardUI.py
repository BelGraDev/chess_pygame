from .ui import UI
from Utils.Cell_utils import map_index_to_cell, get_cell_rect, map_cell_to_index
from Utils.View_utils import redraw_cell_piece, redraw_cell
import pygame
from Board.Pieces import Piece
from Render.Cell import Cell


class BoardUI(UI):
    def __init__(self, screen: pygame.Surface, cells: list[list[Cell]], ascension_cells: list[str]):
        self.screen = screen
        self.cells = cells
        self.ascension_cells = ascension_cells


    def init_board(self) -> None:
        background = pygame.image.load("Render/images/background2.png")
        self.screen.blit(background, (0,0))
        for row in range(8):
            for col in range(8):
                x = self.MARGIN_SIZE + col * self.CELL_SIZE
                y = self.MARGIN_SIZE + row * self.CELL_SIZE
                cell_name = map_index_to_cell(row, col)
                color = self.WHITE_COLOR if (row + col) % 2 == 0 else self.GREY_COLOR       
                cell = Cell((x, y), cell_name, color)
                pygame.draw.rect(self.screen, color, cell)
                self.cells[row].append(cell)
                self.render_border()


    def init_pieces(self, board: dict[str, Piece]) -> None:
        for cell, piece in board.items():
            rect = get_cell_rect(cell, self.cells)
            self.screen.blit(piece.image, rect)


    def render_border(self) -> None:
        border = pygame.Rect(self.MARGIN_SIZE, self.MARGIN_SIZE, self.BOARD_WIDTH, self.BOARD_HEIGHT)
        pygame.draw.rect(self.screen, self.BORDER_COLOR, border,  2)

    def render_pawn_ascension(self, cell_name: str, turn: str, pieces: list[Piece]) -> None:
        row, col = map_cell_to_index(cell_name)
        direction = 1 if turn == "w" else -1
        
        for r, piece in zip(range(row, row + (5 * direction), direction), pieces):
            cell_name = map_index_to_cell(r, col)
            self.ascension_cells.append(cell_name)
            self._draw_ascension_cell(piece, cell_name)

    def draw_possible_move(self, cell_name: str) -> None:
        image = pygame.image.load("Render/images/move.png").convert_alpha()
        cell = get_cell_rect(cell_name, self.cells)
        image_rect = image.get_rect(center= cell.center)
        self.screen.blit(image, image_rect)

    def _draw_ascension_cell(self, piece: Piece, cell_name: str) -> None:
        cell = get_cell_rect(cell_name, self.cells)
        redraw_cell_piece(self.screen, self.ASCENSION_CELL_COLOR, piece, cell)

    def draw_highlight(self, piece: Piece, cell_name: str) -> None:
        cell = get_cell_rect(cell_name, self.cells)
        redraw_cell_piece(self.screen, self.HIGHLIGHT_COLOR, piece, cell)
    
    def draw_replacement_pieces(self, piece: Piece, cell_name: str) -> None:
        cell = get_cell_rect(cell_name, self.cells)
        redraw_cell_piece(self.screen, cell.color, piece, cell)

    
    def draw_empty_cell(self, cell_name: str) -> None:
        cell = get_cell_rect(cell_name, self.cells)
        redraw_cell(self.screen, cell)


    def draw_piece(self, piece: Piece, cell: Cell) -> None:
        redraw_cell_piece(self.screen, cell.color, piece, cell)