import pygame
from .ChessMenu import ChessButton, Button
from .ui import UI

class EndGameUI(UI):

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.end_game_buttons: list[Button] = []


    def render_mate(self, turn: str) -> None:
        image = pygame.image.load(f"Render/images/{turn}_mate.png").convert_alpha()
        self.screen.blit(image, (self.MARGIN_SIZE, self.BOARD_HEIGHT / 2 - image.get_height() / 2 + self.MARGIN_SIZE))


    def render_tie(self) -> None:
        image = pygame.image.load("Render/images/tie.png").convert_alpha()
        self.screen.blit(image, (self.MARGIN_SIZE, self.BOARD_HEIGHT / 2 - image.get_height() / 2 + self.MARGIN_SIZE))

        
    def render_end_game_buttons(self) -> None:
        middle_x = (self.BOARD_WIDTH + self.MARGIN_SIZE * 2) / 2
        middle_y = self.BOARD_HEIGHT / 2

        button_height = 50; button_width = 200

        go_to_menu_button = Button(ChessButton.GO_TO_MENU, (middle_x - button_width - self.MARGIN_SIZE, middle_y + button_width - self.MARGIN_SIZE * 2), button_height, button_width)
        play_again_button = Button(ChessButton.PLAY_AGAIN, (middle_x + self.MARGIN_SIZE, middle_y + button_width - self.MARGIN_SIZE * 2), button_height, button_width)
        image_path = "Render/images/Buttons/"

        go_to_menu_image = pygame.image.load(f"{image_path}back_to_menu.png")
        play_again_image = pygame.image.load(f"{image_path}play_again.png")

        self.screen.blit(go_to_menu_image, go_to_menu_button)
        self.screen.blit(play_again_image, play_again_button)

        self.end_game_buttons = [go_to_menu_button, play_again_button]


    def get_end_game_buttons(self) -> list[Button]:
        return self.end_game_buttons