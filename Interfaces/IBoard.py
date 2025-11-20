from abc import ABC, abstractmethod

class IBoard(ABC):

    @abstractmethod
    def move(self, prev_cell_name: str, next_cell_name) -> int:
        pass
    
    @abstractmethod
    def move_to_cell(self, next_cell_name: str) -> None:
        pass

    @abstractmethod
    def can_color_play(self) -> None:
        pass

    @abstractmethod
    def ascension_pieces(self) -> None:
        pass

    @abstractmethod
    def complete_promotion(self, cell_name: str, piece):
        pass