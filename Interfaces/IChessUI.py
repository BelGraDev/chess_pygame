from abc import ABC, abstractmethod
from Render.ChessMenu import Button
from Render.boardCells import Cell
from Board import BoardStatus

from Board.Pieces import Piece
from pygame import Surface

class IChessUI(ABC):

    def __init__(self, screen: Surface):
        self.ascension_cells: list[str] = []
        self.screen = screen

    @abstractmethod
    def init_board(self) -> None:
        pass
    
    @abstractmethod
    def init_pieces(self, board: BoardStatus) -> None:
        pass

    @abstractmethod
    def render_border(self) -> None:
        pass
    
    @abstractmethod
    def selected_cell(self, coord: tuple[int, int]) -> str | None:
        pass

    @abstractmethod
    def render_mate(self, turn: str) -> None:
        pass
    
    @abstractmethod
    def render_tie(self) -> None:
        pass
    
    @abstractmethod
    def render_end_game_buttons(self) -> None:
        pass

    @abstractmethod
    def get_end_game_buttons(self) -> list[Button]:
        pass
    @abstractmethod
    def render_pawn_ascension(self, cell_name:str, turn: str, pieces: list[Piece]) -> None:
        pass

    @abstractmethod
    def draw_possible_move(self, cell_name: str) -> None:
        pass

    @abstractmethod
    def draw_empty_cell(self, cell_name: str) -> None:
        pass

    @abstractmethod
    def draw_piece(self, piece: Piece, cell: Cell) -> None:
        pass

    @abstractmethod
    def draw_highlight(self, piece: Piece, cell_name: str) -> None:
        pass

    @abstractmethod
    def draw_replacement_pieces(self, piece: Piece, cell_name: str) -> None:
        pass
