import pygame
import sys
from Render.ChessMenu import *
from GameModes.PvpMode import PvpMode

pygame.init()

SCREEN_WIDTH = SCREEN_HEIGHT = 650

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
ui = ChessMenu(screen)
ui.render_menu()
mode = None
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            coord = pygame.mouse.get_pos()
            if mode is None:
                type = ui.button_clicked(coord)
                match type:
                    case ChessButton.PLAY_BUTTON:
                        mode = PvpMode(screen)
                        mode.init_mode()
                    case _:
                        pass
            else:
                mode.play(coord)

    pygame.display.update()
    clock.tick(60)
    