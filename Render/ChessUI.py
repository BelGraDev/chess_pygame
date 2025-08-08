from Render.Cell import Cell
from Board.Cell_utils import Cell_utils
from Render.View_utils import View_utils
import pygame

class ChessUI:

    
    CELL_SIZE = 75
    MARGIN_SIZE = 25
    BOARD_WIDTH = BOARD_HEIGHT = 600
    WHITE_COLOR = (255, 255, 255)
    BLACK_COLOR = (100, 100, 100, 255)
    HIGHLIGHT_COLOR = (253, 216, 8)


    def __init__(self):

        self.cells = [[], [], [], [], [], [], [], []]

    
    def init_board(self, screen) -> None:
        for row in range(8):
            for col in range(8):

                x = self.MARGIN_SIZE + col * self.CELL_SIZE
                y = self.MARGIN_SIZE + row * self.CELL_SIZE
                cell_name = Cell_utils.map_index_to_cell(row, col)
                color = self.WHITE_COLOR if (row + col) % 2 == 0 else self.BLACK_COLOR       
                cell = Cell((x, y), cell_name, color)
                pygame.draw.rect(screen, color, cell)
                self.cells[row].append(cell)

        border = pygame.Rect(self.MARGIN_SIZE, self.MARGIN_SIZE, self.BOARD_WIDTH, self.BOARD_HEIGHT)
        pygame.draw.rect(screen, self.WHITE_COLOR, border,  1)
        
    def init_pieces(self, screen, board):

        for cell, piece in board.items():
            rect = self.get_cell_rect(cell)
            screen.blit(piece.image, rect)

    def get_board_size(self) -> tuple:
        width = self.BOARD_WIDTH + self.MARGIN_SIZE * 2
        height = self.BOARD_HEIGHT + self.MARGIN_SIZE * 2
        return width, height
    
    def get_cell_rect(self, cell_name):
        row, col = Cell_utils.map_cell_to_index(cell_name)
        cell = self.cells[row][col]
        return cell
    
    def draw_piece(self, screen, piece, cell) -> None:
        View_utils.redraw_piece(screen, piece, cell)
        
    def draw_highlight(self, screen, piece, cell) -> None:
        View_utils.redraw_cell_piece(screen, self.HIGHLIGHT_COLOR, piece, cell)

    def draw_unhighlight(self, screen, cell) -> None:
        View_utils.redraw_cell(screen, cell)
    
    def draw_replacement_pieces(self, screen, piece, cell) -> None:
        View_utils.redraw_cell_piece(screen, cell.color, piece, cell)
        
