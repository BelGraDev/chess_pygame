from Board.logicManager import LogicManager
from Controller.GameController import GameController
from Render.chessUI import ChessUI
from Render.ChessMenu import *
from GameModes.GameState import GameState
from Interfaces.IMode import IMode

class PvpMode(IMode):

    def __init__(self, screen: pygame.surface.Surface) -> None:
        self.logic_manageer = LogicManager()
        self.boardUI = ChessUI(screen)
        self.chess_menu = ChessMenu(screen)
        self.controller = GameController(self.logic_manageer, self.boardUI)
        self.game_state = GameState.PVP

    
    def init_mode(self) -> None:
        self.controller.init_board_pieces()

        
    def play(self, coord: tuple[int, int])-> GameState:
        if not self.logic_manageer.is_end_game():
            self._handle_in_game(coord)
        else:
            type = self.controller.check_if_button_pressed(coord)
            self._handle_post_game(type)

        return self.game_state
    
    
    def _handle_in_game(self, coord: tuple[int, int]) -> None:
        cell = self.boardUI.selected_cell(coord)
        if cell:
            self.controller.render_move(cell)
            self.boardUI.render_border()
            

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
        
    