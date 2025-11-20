import pygame
from enum import IntEnum

class ChessButton(IntEnum):
    PLAY_BUTTON = 1
    PLAY_AGAIN = 2
    GO_TO_MENU = 3
    ONLINE_BUTTON = 4

class Button(pygame.Rect):

    def __init__(self, type, coord, height, width):
        self.type: ChessButton = type
        pygame.Rect.__init__(self, coord[0] - self.width / 2, coord[1] - self.height / 2, width, height)

class ChessMenu:

    def __init__(self, screen) -> None:
        self.screen: pygame.Surface = screen
        self.width: int = self.screen.get_width()
        self.height: int = self.screen.get_height()
        self.buttons: list[Button] = self._create_buttons()

    
    def _create_buttons(self) -> list[Button]:
        button_types: list[ChessButton] = [ChessButton.PLAY_BUTTON, ChessButton.ONLINE_BUTTON]
        button_width: int = 300; button_height: int = 75
        buttons = []

        for i, type in enumerate(button_types):   

            button_x: int = self.width / 2 - button_width / 2
            button_y: int = self.height / 2 + button_height * (i-1)
            buttons.append(Button(type, (button_x, button_y), button_height, button_width))

        return buttons
    
    def render_menu(self) -> None:
        self.screen.fill((0, 0, 0))
        image_path: str = "Render/images/Buttons/"
        for button in self.buttons:
            match button.type:
                
                case ChessButton.PLAY_BUTTON:
                    image = pygame.image.load(image_path + "player_vs_player.png")

                case ChessButton.ONLINE_BUTTON:
                    image = pygame.image.load(image_path + "player_vs_player.png")

            self.screen.blit(image, button)

    def button_clicked(self, coord) -> ChessButton | None:
            for button in self.buttons:
                if(button.collidepoint(coord)):
                    return button.type
            return None