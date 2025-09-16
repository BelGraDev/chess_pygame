from Board.Board import Board
from Controller.GameController import GameController
from Render.BoardUI import BoardUI
from Render.ChessMenu import *
from .GameState import GameState

class PvpMode:

    def __init__(self, screen: pygame.surface.Surface) -> None:
        self.board = Board()
        self.boardUI = BoardUI(screen)
        self.chess_menu = ChessMenu(screen)
        self.controller = GameController(self.board, self.boardUI)
        self.game_state = GameState.PVP
    
    def init_mode(self) -> None:
        self.controller.init_board_pieces()
        
    def play(self, coord: tuple)-> GameState:
        if not self.board.board_status.is_end_game:
            self._handle_in_game(coord)
        else:
            type = self.controller.check_if_button_pressed(coord)
            self._handle_post_game_buttons(type)

        return self.game_state
    def _handle_in_game(self, coord: tuple) -> None:
        cell = self.boardUI.selected_cell(coord)
        if cell:
            self.controller.render_move(cell)
            self.boardUI.render_border()

    def _handle_post_game_buttons(self, type: ChessButton) -> None:
        match type:
            case ChessButton.PLAY_AGAIN:
                self.board = Board()
                self.controller = GameController(self.board, self.boardUI)
                self.init_mode()
            case ChessButton.GO_TO_MENU:
                self.chess_menu.render_menu()
                self.game_state = GameState.MENU
        
    