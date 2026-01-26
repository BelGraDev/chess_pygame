from abc import ABC, abstractmethod
from GameModes.GameState import GameState
from Render.chessUI import ChessUI
from Render.ChessMenu import ChessMenu, ChessButton
from Board.logicManager import LogicManager
from Controller.GameController import GameController
from pygame import Surface

class IMode(ABC):

    def __init__(self, screen: Surface) -> None:
        self.logic_manageer = LogicManager()
        self.boardUI = ChessUI(screen)
        self.chess_menu = ChessMenu(screen)
        self.controller = GameController(self.logic_manageer, self.boardUI)


    def init_mode(self) -> None:
        self.controller.init_board_pieces()


    def play(self, coord: tuple[int, int]) -> GameState:
        if not self.logic_manageer.is_end_game():
            self._handle_in_game(coord)
        else:
            type = self.controller.check_if_button_pressed(coord)
            self._handle_post_game(type)
        return self.game_state
    

    def _handle_post_game(self, type: ChessButton | None) -> None:
        match type:
            case ChessButton.PLAY_AGAIN:
                self.logic_manageer = LogicManager()
                self.controller = GameController(self.logic_manageer, self.boardUI)
                self.init_mode()
            case ChessButton.GO_TO_MENU:
                self.chess_menu.render_menu()
                self.game_state = GameState.MENU
            case _:
                pass

        
    @abstractmethod
    def _handle_in_game(self, coord: tuple[int, int]) -> None:
        pass

