from abc import ABC, abstractmethod
from .GameState import GameState

class IMode(ABC):

    @abstractmethod
    def init_mode(self) -> None:
        pass

    @abstractmethod
    def play(self, coord:tuple) -> GameState:
        pass

