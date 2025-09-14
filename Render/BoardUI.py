from Render.Cell import Cell
from Utils.Cell_utils import Cell_utils
from Render.ChessMenu import Button
from Render.ChessMenu import ChessButton
from Utils.View_utils import View_utils

import pygame

class BoardUI:
    
    CELL_SIZE = 75
    MARGIN_SIZE = 25
    BOARD_WIDTH = BOARD_HEIGHT = 600
    BORDER_COLOR = (0, 0, 0)
    WHITE_COLOR = (255, 255, 255)
    GREY_COLOR = (100, 100, 100, 255)
    HIGHLIGHT_COLOR = (250, 230, 150)
    ASCENSION_CELL_COLOR = (166, 123, 91)

    def __init__(self, screen):
        self.cells = [[], [], [], [], [], [], [], []]
        self.screen = screen

    def init_board(self) -> None:
        background = pygame.image.load("Render/images/background2.png")
        self.screen.blit(background, (0,0))
        for row in range(8):
            for col in range(8):

                x = self.MARGIN_SIZE + col * self.CELL_SIZE
                y = self.MARGIN_SIZE + row * self.CELL_SIZE
                cell_name = Cell_utils.map_index_to_cell(row, col)
                color = self.WHITE_COLOR if (row + col) % 2 == 0 else self.GREY_COLOR       
                cell = Cell((x, y), cell_name, color)
                pygame.draw.rect(self.screen, color, cell)
                self.cells[row].append(cell)
                self.render_border()

    def render_border(self):
        border = pygame.Rect(self.MARGIN_SIZE, self.MARGIN_SIZE, self.BOARD_WIDTH, self.BOARD_HEIGHT)
        pygame.draw.rect(self.screen, self.BORDER_COLOR, border,  2)
        
    def init_pieces(self, board):

        for cell, piece in board.items():
            rect = self._get_cell_rect(cell)
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

    def render_check_buttons(self) -> list[Button]:
        middle_x = (self.BOARD_WIDTH + self.MARGIN_SIZE * 2) / 2
        middle_y = self.BOARD_HEIGHT / 2

        button_height = 50; button_width = 200

        go_to_menu_button = Button(ChessButton.GO_TO_MENU, (middle_x - button_width - self.MARGIN_SIZE, middle_y + button_width - self.MARGIN_SIZE * 2), button_height, button_width)
        play_again_button = Button(ChessButton.PLAY_AGAIN, (middle_x + self.MARGIN_SIZE, middle_y + button_width - self.MARGIN_SIZE * 2), button_height, button_width)
        image_path = "Render/images/Buttons/"

        go_to_menu_image = pygame.image.load(image_path + "back_to_menu.png")
        play_again_image = pygame.image.load(image_path + "play_again.png")

        self.screen.blit(go_to_menu_image, go_to_menu_button)
        self.screen.blit(play_again_image, play_again_button)

        return (go_to_menu_button, play_again_button)

    def render_pawn_ascension(self, cell_name, turn, pieces):
        row, col = Cell_utils.map_cell_to_index(cell_name)
        direction = 1 if turn == "w" else -1
        self.ascension_cells = []
        for r, piece in zip(range(row, row + (5 * direction), direction), pieces):
            cell_name = Cell_utils.map_index_to_cell(r, col)
            self.ascension_cells.append(cell_name)
            self.draw_ascension_cell(piece, cell_name)

    def get_board_size(self) -> tuple:
        width = self.BOARD_WIDTH + self.MARGIN_SIZE * 2
        height = self.BOARD_HEIGHT + self.MARGIN_SIZE * 2
        return width, height
    
    def _get_cell_rect(self, cell_name):
        row, col = Cell_utils.map_cell_to_index(cell_name)
        cell = self.cells[row][col]
        return cell
    
    def draw_possible_move(self, cell_name) -> None:
        image = pygame.image.load("Render/images/move.png").convert_alpha()
        cell = self._get_cell_rect(cell_name)
        image_rect = image.get_rect(center= cell.center)
        self.screen.blit(image, image_rect)

    def draw_empty_cell(self, cell_name):
        cell = self._get_cell_rect(cell_name)
        View_utils.redraw_cell(self.screen, cell)

    def draw_piece(self, piece, cell) -> None:
        View_utils.redraw_cell_piece(self.screen, cell.color, piece, cell)
        
    def draw_highlight(self, piece, cell_name) -> None:
        cell = self._get_cell_rect(cell_name)
        View_utils.redraw_cell_piece(self.screen, self.HIGHLIGHT_COLOR, piece, cell)
    
    def draw_replacement_pieces(self, piece, cell_name) -> None:
        cell = self._get_cell_rect(cell_name)
        View_utils.redraw_cell_piece(self.screen, cell.color, piece, cell)
    
    def draw_ascension_cell(self, piece, cell_name) -> None:
        cell = self._get_cell_rect(cell_name)
        View_utils.redraw_cell_piece(self.screen, self.ASCENSION_CELL_COLOR, piece, cell)
