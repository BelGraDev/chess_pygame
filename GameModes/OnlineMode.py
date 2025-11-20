from Interfaces.IMode import IMode
from Board.Board import Board
from Render.BoardUI import BoardUI
from Render.ChessMenu import ChessMenu
from Controller.GameController import GameController
from .GameState import GameState
import asyncio
from websockets.client import connect

class OnlineMode(IMode):

    def __init__(self, screen):
        self.board = Board()
        self.boardUI = BoardUI(screen)
        self.chess_menu = ChessMenu(screen)
        self.controller = GameController(self.board, self.boardUI)
        self.game_state = GameState.ONLINE
        self.websocket = None

    def init_mode(self):
        self.controller.init_board_pieces()
        self._connect()

    def play(self, coord: tuple)-> GameState:
        if not self.board.board_status.is_end_game:
            self._handle_in_game(coord)
        else:
            type = self.controller.check_if_button_pressed(coord)
            self._handle_post_game(type)

        return self.game_state
    
    def _handle_in_game(self, coord: tuple) -> None:
        cell = self.boardUI.selected_cell(coord)
        if cell:
            self.websocket.send(cell)
            date: str = self.websocket.recv()
            print(date)
            self.boardUI.render_border()

    async def _connect(self) -> None:
        self.websocket = await connect("ws//:localhost:81")