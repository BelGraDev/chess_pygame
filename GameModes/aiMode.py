from Interfaces import IMode
from GameModes import GameState
from pygame import Surface
from random import randint

class AIMode(IMode):
    
    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)
        self.game_state = GameState.AI
        self._player_turn = self._calculate_player_turn()


    def _calculate_player_turn(self) -> str:
        return 'w' if randint(0, 1) == 0 else 'b'
    
    def _handle_in_game(self, coord: tuple[int, int]) -> None:
        cell = self.boardUI.selected_cell(coord)
        if cell:
            self.controller.ai_game(cell, self._player_turn)
            self.boardUI.render_border()

    