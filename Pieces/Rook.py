from Pieces.Pieces import Pieces
from Board.Cell_utils import Cell_utils
import pygame

import time

class Rook(Pieces):

    
    def __init__(self, cell, type, board) -> None:

        super().__init__(cell, type, board)
        self.image = pygame.image.load(f"Pieces/images/{type}_rook.png")

    def possible_moves(self, cell_name) -> list:

        start_time = time.perf_counter()
        
        row, column = Cell_utils.map_cell_to_index(cell_name)

        possible_moves = []

        #Upwards check
        for r in range(row - 1, -1, -1):
            move = self.is_next_possible(cell_name, r, column)
            if move:
                possible_moves.append(move)
            else:
                break

        #Downwards check
        for r in range(row + 1, 8):
            move = self.is_next_possible(cell_name, r, column)
            if move:
                possible_moves.append(move)
            else:
                break

        for c in range(column - 1, -1, -1):
            move = self.is_next_possible(cell_name, row, c)
            if move:
                possible_moves.append(move)
            else:
                break

        for c in range(column + 1, 8):
            move = self.is_next_possible(cell_name, row, c)
            if move:
                possible_moves.append(move)
            else:
                break

        end_time = time.perf_counter()

        #print(f"It took the function {end_time - start_time}")
        print(possible_moves)
        return possible_moves