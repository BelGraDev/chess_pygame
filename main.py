import pygame
import sys
from chess_ui.chess_ui import ChessUI
pygame.init()

SCREEN_WIDTH = SCREEN_HEIGHT = 650

screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
chess_ui = ChessUI(screen)
chess_ui.init_board()
chess_ui.init_pieces()

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            coord = pygame.mouse.get_pos()
            

    pygame.display.update()
    clock.tick(60)
    