import pygame
import sys
from Board.Board import Board
from Render.ChessUI import ChessUI

pygame.init()

board = Board()
renderer = ChessUI(board)

size = renderer.get_board_size()
screen = pygame.display.set_mode(size)
screen.fill((137,81,41))
renderer.init_board_pieces(screen)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
           sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            coord = pygame.mouse.get_pos()
            print(renderer.selected_cell(coord))

    pygame.display.update()
    clock.tick(60)
    