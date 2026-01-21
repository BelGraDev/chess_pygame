from abc import ABC, abstractmethod
from Board.Pieces import Piece
from Board.Move import MoveType
from Board.BoardStatus import BoardStatus

class ILogicManager(ABC):

    @abstractmethod
    def move(self, prev_cell_name: str, next_cell_name: str) -> MoveType:
        pass
    
    @abstractmethod
    def move_to_cell(self, next_cell_name: str) -> None:
        pass

    @abstractmethod
    def can_color_play(self, cell_name: str) -> bool:
        pass

    @abstractmethod
    def ascension_pieces(self) -> list[Piece]:
        pass

    @abstractmethod
    def complete_promotion(self, cell_name: str, piece: Piece) -> None:
        pass

    @abstractmethod
    def get_piece(self, cell_name: str) -> Piece:
        pass

    @abstractmethod
    def get_piece_if_any(self, cell_name: str) -> Piece  | None:
        pass

    @abstractmethod
    def get_turn(self) -> str:
        pass

    @abstractmethod
    def get_board(self) -> BoardStatus:
        pass