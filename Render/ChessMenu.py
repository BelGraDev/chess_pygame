import pygame
from enum import IntEnum

class ChessButton(IntEnum):
    PLAY_BUTTON = 1

class Button(pygame.Rect):

    BUTTON_HEIGHT = 50
    BUTTON_WIDTH = 200
    def __init__(self, type, coord):
        self.type = type
        pygame.Rect.__init__(self, coord[0] - self.BUTTON_WIDTH / 2, coord[1] - self.BUTTON_HEIGHT / 2, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)

class ChessMenu:

    def __init__(self, screen):
        self.screen = screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.buttons = self._create_buttons()

    
    def _create_buttons(self) -> list[Button]:
        button_types = [ChessButton.PLAY_BUTTON]
        button_x = self.width / 2
        button_y = self.height / 2
        buttons = [Button(type, (button_x, button_y)) for type in button_types]
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