from abc import ABC, abstractmethod
from Render.ChessMenu import Button

class IBoardUI(ABC):

    @abstractmethod
    def init_board(self) -> None:
        pass

    @abstractmethod
    def render_border(self) -> None:
        pass
    
    @abstractmethod
    def init_pieces(self, board) -> None:
        pass
    
    @abstractmethod
    def selected_cell(self, coord) -> str | None:
        pass
    
    @abstractmethod
    def render_mate(self, turn: str) -> None:
        pass
    
    @abstractmethod
    def render_tie(self) -> None:
        pass
    
    @abstractmethod
    def render_check_buttons(self) -> list[Button]:
        pass

    @abstractmethod
    def render_pawn_ascension(self, cell_name:str, turn, pieces) -> None:
        pass

    @abstractmethod
    def get_board_size(self) -> tuple:
        pass

    @abstractmethod
    def draw_possible_move(self, cell_name: str) -> None:
        pass

    @abstractmethod
    def draw_empty_cell(self, cell_name: str) -> None:
        pass

    @abstractmethod
    def draw_piece(self, piece, cell) -> None:
        pass

    @abstractmethod
    def draw_highlight(self, piece, cell_name: str) -> None:
        pass

    @abstractmethod
    def draw_replacement_pieces(self, piece, cell_name: str) -> None:
        pass

    @abstractmethod
    def draw_ascension_cell(self, piece, cell_name: str) -> None:
        pass