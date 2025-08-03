from Board.Cell import Cell
import pygame

class ChessUI:

    
    CELL_SIZE = 75
    MARGIN_SIZE = 25
    BOARD_WIDTH = BOARD_HEIGHT = 600

    def __init__(self, board):

        self.cells = [[], [], [], [], [], [], [], []]
        self.board = board
    
    def init_board(self, screen) -> None:
        white_color = (255, 255, 255)
        black_color = (100, 100, 100, 255)

        for row in range(8):
            for col in range(8):

                x = self.MARGIN_SIZE + col * self.CELL_SIZE
                y = self.MARGIN_SIZE + row * self.CELL_SIZE
                cell_name = Cell.map_index_to_cell(row, col)
                color = white_color if (row + col) % 2 == 0 else black_color       
                cell = Cell((x, y), cell_name)
                pygame.draw.rect(screen, color, cell)
                self.cells[row].append(cell)

        border = pygame.Rect(self.MARGIN_SIZE, self.MARGIN_SIZE, self.BOARD_WIDTH, self.BOARD_HEIGHT)
        pygame.draw.rect(screen, white_color, border,  1)
        
    def init_pieces(self, screen):

        for cell, piece in self.board.board.items():
            row, col = Cell.map_cell_to_index(cell)
            rect = self.cells[row][col]
            screen.blit(piece.image, rect)

    def init_board_pieces(self, screen):

        self.init_board(screen)
        self.init_pieces(screen)

    def get_board_size(self) -> tuple:
        width = self.BOARD_WIDTH + self.MARGIN_SIZE * 2
        height = self.BOARD_HEIGHT + self.MARGIN_SIZE * 2
        return width, height
    
    def selected_cell(self, coord) -> str:
        
        for row in range(8):
            for col in range(8):
                cell = self.cells[row][col]
                if(cell.collidepoint(coord)):
                    return cell.name
                
        return None