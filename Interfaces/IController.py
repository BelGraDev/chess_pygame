from abc import ABC, abstractmethod
from Render.ChessMenu import ChessButton

class IController(ABC):

    @abstractmethod
    def init_board_pieces(self) -> None:
        pass
    @abstractmethod
    def render_move(self, cell_name: str) -> None:
        pass

    @abstractmethod
    def check_if_button_pressed(self, coord: tuple[int, int]) -> ChessButton | None:
        pass