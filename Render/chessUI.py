from Render.Cell import Cell
from Utils.Cell_utils import map_index_to_cell, map_cell_to_index, get_cell_rect
from Render.ChessMenu import Button
from Utils.View_utils import redraw_cell, redraw_cell_piece
from Interfaces.IChessUI import IChessUI
from Board.Pieces import Piece
from Render.Cell import Cell
from .ui import UI
from .endGameUI import EndGameUI
from .boardUI import BoardUI

import pygame

class ChessUI(IChessUI, UI):

    def __init__(self, screen: pygame.Surface) -> None:
        super().__init__(screen)
        self.cells: list[list[Cell]] = [[], [], [], [], [], [], [], []]
        self.end_game_ui = EndGameUI(screen)
        self.board_ui = BoardUI(screen, self.cells, self.ascension_cells)


    def init_board(self) -> None:
        self.board_ui.init_board()


    def init_pieces(self, board: dict[str, Piece]) -> None:
        self.board_ui.init_pieces(board)

    
    def render_border(self) -> None:
        self.board_ui.render_border()


    def get_end_game_buttons(self) -> list[Button]:
        return self.end_game_ui.get_end_game_buttons()


    def selected_cell(self, coord: tuple[int, int]) -> str | None:
        
        for row in range(8):
            for col in range(8):
                cell = self.cells[row][col]
                if(cell.collidepoint(coord)):
                    return cell.name
                
        return None
    

    def render_mate(self, turn: str) -> None:
        self.end_game_ui.render_mate(turn)


    def render_tie(self) -> None:
        self.end_game_ui.render_tie()
        

    def render_end_game_buttons(self) -> None:
        self.end_game_ui.render_end_game_buttons()


    def render_pawn_ascension(self, cell_name: str, turn: str, pieces: list[Piece]) -> None:
        self.board_ui.render_pawn_ascension(cell_name, turn, pieces)

    
    def draw_possible_move(self, cell_name: str) -> None:
        self.board_ui.draw_possible_move(cell_name)


    def draw_empty_cell(self, cell_name: str) -> None:
        self.board_ui.draw_empty_cell(cell_name)


    def draw_piece(self, piece: Piece, cell: Cell) -> None:
        self.board_ui.draw_piece(piece, cell)        


    def draw_highlight(self, piece: Piece, cell_name: str) -> None:
        self.board_ui.draw_highlight(piece, cell_name)
    

    def draw_replacement_pieces(self, piece: Piece, cell_name: str) -> None:
        self.board_ui.draw_replacement_pieces(piece, cell_name)

    
