from Pieces import Bishop, King, Knight, Pawn, Queen, Rook
from .Cell import Cell
import pygame

class Board:

    CELL_SIZE = 75
    MARGIN_SIZE = 25
    BOARD_WIDTH = BOARD_HEIGHT = 600

    def __init__(self):

        self.cells = [[], [], [], [], [], [], [], []]
    #     self.board =  {
    #         "a1": Rook("a1"),
    #         "b1": Knight("b1"),
    #         "c1": Bishop("c1"),
    #         "d1": Queen("d1"),
    #         "e1": King("e1"),
    #         "f1": Bishop("f1"),
    #         "g1": Knight("g1"),
    #         "h1": Rook("h1"),
    #         "a2": Pawn("a2"),
    #         "b2": Pawn("b2"),
    #         "c2": Pawn("c2"),
    #         "d2": Pawn("d2"),
    #         "e2": Pawn("e2"),
    #         "f2": Pawn("f2"),
    #         "g2": Pawn("g2"),
    #         "h2": Pawn("h2"),
    #         "a8": Rook("a8"),
    #         "b8": Knight("b8"),
    #         "c8": Bishop("c8"),
    #         "d8": Queen("d8"),
    #         "e8": King("e8"),
    #         "f8": Bishop("f8"),
    #         "g8": Knight("g8"),
    #         "h8": Rook("h8"),
    #         "a7": Pawn("a7"),
    #         "b7": Pawn("b7"),
    #         "c7": Pawn("c7"),
    #         "d7": Pawn("d7"),
    #         "e7": Pawn("e7"),
    #         "f7": Pawn("f7"),
    #         "g7": Pawn("g7"),
    #         "h7": Pawn("h7")
    #     }
        
    def draw_board(self, screen):
                
        white_color = (255, 255, 255)
        black_color = (0, 0, 0)
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
        print(self.cells)

    def render_white_pieces(self, screen):

        for piece in self.board.values():
            piece.render_piece(screen)

    def get_size(self) -> tuple:
        width = self.BOARD_WIDTH + self.MARGIN_SIZE * 2
        height = self.BOARD_HEIGHT + self.MARGIN_SIZE * 2
        return width, height
    
    #def map_cell_to_index(cell: str) -> tuple:
