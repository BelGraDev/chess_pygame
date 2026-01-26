from Interfaces import IMode
from GameModes import GameState
from pygame import Surface

class AIMode(IMode):
    
    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)
        self.game_mode = GameState.AI


    def _handle_in_game(self, coord: tuple[int, int]) -> None:
        cell = self.boardUI.selected_cell(coord)
        if cell:
            self.controller.render_move(cell)
            self.boardUI.render_border()
