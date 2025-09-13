import pygame
import sys
from Render.ChessMenu import *
from GameModes.PvpMode import PvpMode
from GameModes.GameState import GameState

pygame.init()

SCREEN_WIDTH = SCREEN_HEIGHT = 650

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
ui = ChessMenu(screen)
ui.render_menu()
game_state = GameState.MENU
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            coord = pygame.mouse.get_pos()
            if game_state is GameState.MENU:
                type = ui.button_clicked(coord)
                match type:
                    case ChessButton.PLAY_BUTTON:
                        game_mode = PvpMode(screen)
                        game_mode.init_mode()
                        game_state = GameState.PVP
                    case _:
                        pass
            else:
                game_state = game_mode.play(coord)

    pygame.display.update()
    clock.tick(60)
    