import pygame
from enum import IntEnum

class ChessButton(IntEnum):
    PLAY_BUTTON = 1
    PLAY_AGAIN = 2
    GO_TO_MENU = 3
    AI_BUTTON = 4

class Button(pygame.Rect):

    def __init__(self, type: ChessButton, coord: tuple[float, float], height: int, width: int):
        self.type = type
        pygame.Rect.__init__(self, coord[0] - self.width / 2, coord[1] - self.height / 2, width, height)

class ChessMenu:

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen: pygame.Surface = screen
        self.background_image = pygame.image.load("Render/images/menu_background1.png")
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.buttons = self._create_buttons()

    
    def _create_buttons(self) -> list[Button]:
        button_types: list[ChessButton] = [ChessButton.PLAY_BUTTON, ChessButton.AI_BUTTON]
        button_width: int = 300; button_height: int = 75
        buttons: list[Button] = []

        for i, type in enumerate(button_types):   

            button_x = self.width / 2 - button_width / 2
            button_y = self.height / 2 + button_height * (i - 1)
            buttons.append(Button(type, (button_x, button_y), button_height, button_width))

        return buttons
    
    def render_menu(self) -> None:

        self.screen.blit(self.background_image, (-275,0))
        image_path = "Render/images/Buttons/"
        for button in self.buttons:
            match button.type:
                
                case ChessButton.PLAY_BUTTON:
                    image = pygame.image.load(image_path + "player_vs_player.png")

                case ChessButton.AI_BUTTON:
                    image = pygame.image.load(image_path + "player_vs_player.png")
                case _:
                    pass

            self.screen.blit(image, button) # type: ignore

    def button_clicked(self, coord: tuple[int, int]) -> ChessButton | None:
            for button in self.buttons:
                if(button.collidepoint(coord)):
                    return button.type
            return None