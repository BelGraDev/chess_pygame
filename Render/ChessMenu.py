import pygame
from enum import IntEnum

class ChessButton(IntEnum):
    PLAY_BUTTON = 1
    PLAY_AGAIN = 2
    GO_TO_MENU = 3

class Button(pygame.Rect):

    def __init__(self, type, coord, height, width):
        self.type = type
        pygame.Rect.__init__(self, coord[0] - self.width / 2, coord[1] - self.height / 2, width, height)

class ChessMenu:

    def __init__(self, screen):
        self.screen = screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.buttons = self._create_buttons()

    
    def _create_buttons(self) -> list[Button]:
        button_types = [ChessButton.PLAY_BUTTON]
        button_width = 200; button_height = 50
        button_x = self.width / 2 - button_width / 2
        button_y = self.height / 2
        buttons = [Button(type, (button_x, button_y), button_height, button_width) for type in button_types]
        return buttons
    
    def render_menu(self):
        self.screen.fill((0, 0, 0))
        for button in self.buttons:
            pygame.draw.rect(self.screen, (255, 255, 255), button)

    def button_clicked(self, coord) -> ChessButton | None:
            for button in self.buttons:
                if(button.collidepoint(coord)):
                    return button.type
            return None