from Render.Cell import Cell
from Utils.Cell_utils import Cell_utils
from Utils.View_utils import View_utils
import pygame

class ChessUI:

    
    CELL_SIZE = 75
    MARGIN_SIZE = 25
    BOARD_WIDTH = BOARD_HEIGHT = 600
    WHITE_COLOR = (255, 255, 255)
    BLACK_COLOR = (100, 100, 100, 255)
    HIGHLIGHT_COLOR = (250, 230, 150)

    def __init__(self):
        self.cells = [[], [], [], [], [], [], [], []]
        self.screen = None

    def init_board(self) -> None:
        for row in range(8):
            for col in range(8):

                x = self.MARGIN_SIZE + col * self.CELL_SIZE
                y = self.MARGIN_SIZE + row * self.CELL_SIZE
                cell_name = Cell_utils.map_index_to_cell(row, col)
                color = self.WHITE_COLOR if (row + col) % 2 == 0 else self.BLACK_COLOR       
                cell = Cell((x, y), cell_name, color)
                pygame.draw.rect(self.screen, color, cell)
                self.cells[row].append(cell)

        border = pygame.Rect(self.MARGIN_SIZE, self.MARGIN_SIZE, self.BOARD_WIDTH, self.BOARD_HEIGHT)
        pygame.draw.rect(self.screen, self.WHITE_COLOR, border,  1)
        
    def init_pieces(self, board):

        for cell, piece in board.items():
            rect = self.get_cell_rect(cell)
            self.screen.blit(piece.image, rect)

    def selected_cell(self, coord) -> str | None:
        
        for row in range(8):
            for col in range(8):
                cell = self.cells[row][col]
                if(cell.collidepoint(coord)):
                    return cell.name
                
        return None
    def render_mate(self, turn) -> None:
        image = pygame.image.load(f"Render/images/{turn}_mate.png").convert_alpha()
        self.screen.blit(image, (self.MARGIN_SIZE, self.BOARD_HEIGHT / 2 - image.get_height() / 2 + self.MARGIN_SIZE))

    def get_board_size(self) -> tuple:
        width = self.BOARD_WIDTH + self.MARGIN_SIZE * 2
        height = self.BOARD_HEIGHT + self.MARGIN_SIZE * 2
        return width, height
    
    def get_cell_rect(self, cell_name):
        row, col = Cell_utils.map_cell_to_index(cell_name)
        cell = self.cells[row][col]
        return cell
    
    def draw_possible_move(self, cell) -> None:
        image = pygame.image.load("Render/images/move.png").convert_alpha()
        image_rect = image.get_rect(center= cell.center)
        self.screen.blit(image, image_rect)

    def draw_empty_cell(self, cell):
        View_utils.redraw_cell(self.screen, cell)

    def draw_piece(self, piece, cell) -> None:
        View_utils.redraw_cell_piece(self.screen, cell.color, piece, cell)
        
    def draw_highlight(self, piece, cell) -> None:
        View_utils.redraw_cell_piece(self.screen, self.HIGHLIGHT_COLOR, piece, cell)
    
    def draw_replacement_pieces(self, piece, cell) -> None:
        View_utils.redraw_cell_piece(self.screen, cell.color, piece, cell)
        
