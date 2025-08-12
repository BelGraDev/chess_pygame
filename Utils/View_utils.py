import pygame

class View_utils:  
    
    def redraw_cell_piece(screen, color, piece, cell) -> None:
        pygame.draw.rect(screen, color, cell)
        screen.blit(piece.image, cell)

    def redraw_cell(screen, cell) -> None:
        pygame.draw.rect(screen, cell.color, cell)

    def draw_image(screen, image, cell):
        screen.blit(image, cell)


    