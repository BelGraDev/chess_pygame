import pygame
from Board.Pieces import Piece
from Render.boardCells import Cell

def redraw_cell_piece(screen: pygame.Surface, color: tuple[int, int , int, int], piece: Piece, cell: Cell) -> None:
    pygame.draw.rect(screen, color, cell)
    screen.blit(piece.image, cell)

def redraw_cell(screen: pygame.Surface, cell: Cell) -> None:
    pygame.draw.rect(screen, cell.color, cell)

def draw_image(screen: pygame.Surface, image: pygame.Surface, cell: Cell):
    screen.blit(image, cell)


    