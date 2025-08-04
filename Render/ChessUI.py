from Render.Cell import Cell
from Board.Cell_utils import Cell_utils
import pygame

class ChessUI:

    
    CELL_SIZE = 75
    MARGIN_SIZE = 25
    BOARD_WIDTH = BOARD_HEIGHT = 600
    WHITE_COLOR = (255, 255, 255)
    BLACK_COLOR = (100, 100, 100, 255)


    def __init__(self, board):

        self.cells = [[], [], [], [], [], [], [], []]
        self.board = board
        self.cell_highlighted = None
    
    def init_board(self, screen) -> None:
        for row in range(8):
            for col in range(8):

                x = self.MARGIN_SIZE + col * self.CELL_SIZE
                y = self.MARGIN_SIZE + row * self.CELL_SIZE
                cell_name = Cell_utils.map_index_to_cell(row, col)
                color = self.WHITE_COLOR if (row + col) % 2 == 0 else self.BLACK_COLOR       
                cell = Cell((x, y), cell_name)
                pygame.draw.rect(screen, color, cell)
                self.cells[row].append(cell)

        border = pygame.Rect(self.MARGIN_SIZE, self.MARGIN_SIZE, self.BOARD_WIDTH, self.BOARD_HEIGHT)
        pygame.draw.rect(screen, self.WHITE_COLOR, border,  1)
        
    def init_pieces(self, screen):

        for cell, piece in self.board.board.items():
            rect = self.get_cell_rect(cell)
            screen.blit(piece.image, rect)

    def init_board_pieces(self, screen):

        self.init_board(screen)
        self.init_pieces(screen)

    def get_board_size(self) -> tuple:
        width = self.BOARD_WIDTH + self.MARGIN_SIZE * 2
        height = self.BOARD_HEIGHT + self.MARGIN_SIZE * 2
        return width, height
    
    def selected_cell(self, coord) -> str | None:
        
        for row in range(8):
            for col in range(8):
                cell = self.cells[row][col]
                if(cell.collidepoint(coord)):
                    return cell.name
                
        return None
    
    #I still have to implement the unhighlight in case another piece is selected.
    def highlight_cell(self, screen, cell) -> None:

        if not self.cell_highlighted:
            try:
                piece = self.board.board[cell]
                rect = self.get_cell_rect(cell)
                self.cell_highlighted = cell

                pygame.draw.rect(screen, (253, 216, 8), rect)
                screen.blit(piece.image, rect)

            except KeyError:
                print("Clicked empty cell")
    
    def draw_single_cell(cell):
        pass

    
    def render_move(self, screen, cell):
        if self.cell_highlighted:
            prev_cell = self.cell_highlighted
            if self.board.move(prev_cell, cell):
                rect = self.get_cell_rect(cell) 
                piece = self.board.board[cell]
                screen.blit(piece.image, rect)
                #self.cell_highlighted = None             If i do not comment this line, the error is king of solved

    def get_cell_rect(self, cell):
        row, col = Cell_utils.map_cell_to_index(cell)
        rect = self.cells[row][col]
        return rect
