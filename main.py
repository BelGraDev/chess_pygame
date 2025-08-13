import pygame
import sys
from Board.Board import Board
from Render.ChessUI import ChessUI
from Controller.GameController import GameController

pygame.init()

board = Board()
renderer = ChessUI()
controller = GameController(board, renderer)

size = renderer.get_board_size()
screen = pygame.display.set_mode(size)
screen.fill((137,81,41))
renderer.screen = screen
controller.init_board_pieces()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
           sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            coord = pygame.mouse.get_pos()
            cell = renderer.selected_cell(coord)
            if cell:
                controller.render_move(cell)

    pygame.display.update()
    clock.tick(60)
    