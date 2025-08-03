import pygame
import sys

pygame.init()

rect = pygame.Rect(10, 10 ,30, 30)
print(rect.centerx, rect.centery)

# def draw_board(width, height, screen):

#     block_size = 75
#     is_white_cell = False
#     white_color = (255, 255, 255)
#     black_color = (0,0,0)
#     color = white_color

#     for x in range(25, width, block_size):
#         for y in range(25, height, block_size):

#             if y != 25:
#                 if is_white_cell:
#                     color = white_color
#                     is_white_cell = False
#                 else:
#                     color = black_color
#                     is_white_cell = True

#             rect = pygame.Rect(x, y, block_size, block_size)
#             pygame.draw.rect(screen, color, rect)
#     border = pygame.Rect(25, 25, 600, 600)
#     pygame.draw.rect(screen, white_color, border,  1)

# BOARD_WIDTH: int = 600
# BOARD_HEIGHT: int = 600
# screen = pygame.display.set_mode((650, 650))
# screen.fill((137,81,41))

# while True:
#     draw_grid(BOARD_WIDTH, BOARD_HEIGHT, screen)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

#     pygame.display.update()

