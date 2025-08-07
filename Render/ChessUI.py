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
                cell = Cell((x, y), cell_name, color)
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
    
    def highlight_cell(self, screen, cell_name) -> None:

        try:
            piece = self.board.board[cell_name]
            cell = self.cell_highlighted = self.get_cell_rect(cell_name)

            pygame.draw.rect(screen, (253, 216, 8), cell)
            screen.blit(piece.image, cell)

        except KeyError:
            print("Clicked empty cell")
    
    def unhighlight_cell(self,screen, cell):
        self.cell_highlighted = None
        pygame.draw.rect(screen, cell.color, cell)

    
    def render_move(self, screen, cell_name) -> None:
        prev_cell = self.cell_highlighted
        if prev_cell:
            
            move_result = self.board.move(prev_cell.name, cell_name)
            match move_result:

                case 0:
                    self.move_to_cell(screen, cell_name)
                case 1:
                    self.render_kill(screen, cell_name)
                case _:
                    self.switch_focus(screen, prev_cell, cell_name)
                    return
                
            self.unhighlight_cell(screen, prev_cell)

        else:
            self.highlight_cell(screen, cell_name)

    def move_to_cell(self, screen, cell_name) -> None:
        cell = self.get_cell_rect(cell_name) 
        piece = self.board.board[cell_name]
        screen.blit(piece.image, cell)
    
    def render_kill(self, screen, cell_name) -> None:
        cell = self.get_cell_rect(cell_name) 
        piece = self.board.board[cell_name]
        pygame.draw.rect(screen, cell.color, cell)
        screen.blit(piece.image, cell)

    def switch_focus(self, screen, prev_cell, cell_name) -> None:

        self.highlight_cell(screen, cell_name)

        prev_piece = self.board.board[prev_cell.name]
        pygame.draw.rect(screen, prev_cell.color, prev_cell)
        screen.blit(prev_piece.image, prev_cell)


    def get_cell_rect(self, cell_name):
        row, col = Cell_utils.map_cell_to_index(cell_name)
        cell = self.cells[row][col]
        return cell
