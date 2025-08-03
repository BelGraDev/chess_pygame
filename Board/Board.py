from Pieces.Rook import Rook
from Pieces.Bishop import Bishop
from Pieces.Pawn import Pawn
from Pieces.King import King
from Pieces.Queen import Queen
from Pieces.Knight import Knight
from .Cell import Cell
import pygame

class Board:

    #Before i forget, once a cell is obtained, i get the corresponding click from the mouse click, look at the piece that is on the cell in the dict cells, and access to its move function. Before all this happens, a first click will need to happen, in order to select the piece.

    CELL_SIZE = 75
    MARGIN_SIZE = 25
    BOARD_WIDTH = BOARD_HEIGHT = 600

    def __init__(self):

        self.cells = [[], [], [], [], [], [], [], []]
        self.board =  {
            "a1": Rook("a1", "w"),
            "b1": Knight("b1", "w"),
            "c1": Bishop("c1", "w"),
            "d1": Queen("d1", "w"),
            "e1": King("e1", "w"),
            "f1": Bishop("f1", "w"),
            "g1": Knight("g1", "w"),
            "h1": Rook("h1", "w"),
            "a2": Pawn("a2", "w"),
            "b2": Pawn("b2", "w"),
            "c2": Pawn("c2", "w"),
            "d2": Pawn("d2", "w"),
            "e2": Pawn("e2", "w"),
            "f2": Pawn("f2", "w"),
            "g2": Pawn("g2", "w"),
            "h2": Pawn("h2", "w"),
            "a8": Rook("a8", "b"),
            "b8": Knight("b8", "b"),
            "c8": Bishop("c8", "b"),
            "d8": Queen("d8", "b"),
            "e8": King("e8", "b"),
            "f8": Bishop("f8", "b"),
            "g8": Knight("g8", "b"),
            "h8": Rook("h8", "b"),
            "a7": Pawn("a7", "b"),
            "b7": Pawn("b7", "b"),
            "c7": Pawn("c7", "b"),
            "d7": Pawn("d7", "b"),
            "e7": Pawn("e7", "b"),
            "f7": Pawn("f7", "b"),
            "g7": Pawn("g7", "b"),
            "h7": Pawn("h7", "b")
        }
        
    def draw_board(self, screen) -> None:
                
        white_color = (255, 255, 255)
        black_color = (100, 100, 100, 255)  # RGB dark gray, fully opaque
        cell_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        for row in range(8):
            for col in range(8):

                x = self.MARGIN_SIZE + col * self.CELL_SIZE
                y = self.MARGIN_SIZE + row * self.CELL_SIZE
                cell_name = cell_letter[col] + str(8 - row)
                color = white_color if (row + col) % 2 == 0 else black_color       
                cell = Cell((x, y), cell_name)
                pygame.draw.rect(screen, color, cell)
                self.cells[row].append(cell)

        border = pygame.Rect(self.MARGIN_SIZE, self.MARGIN_SIZE, self.BOARD_WIDTH, self.BOARD_HEIGHT)
        pygame.draw.rect(screen, white_color, border,  1)

    def draw_pieces(self, screen):

        for cell, piece in self.board.items():
            row, col = Cell.map_cell_to_index(cell)
            rect = self.cells[row][col]
            screen.blit(piece.image, rect)

    def get_size(self) -> tuple:
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
                

        