import pygame
import sys
from Board.Board import Board

pygame.init()

board = Board()
size = board.get_size()
screen = pygame.display.set_mode(size)
screen.fill((137,81,41))
board.draw_board(screen)
board.draw_pieces(screen)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
           sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            coord = pygame.mouse.get_pos()
            print(board.selected_cell(coord))

    pygame.display.update()
    clock.tick(60)
    