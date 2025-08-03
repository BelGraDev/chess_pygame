import pygame

class Cell(pygame.Rect):

    def __init__(self, coord: iter, name: str):
        self.CELL_SIZE = 75
        self.name = name
        pygame.Rect.__init__(self, coord[0], coord[1],  self.CELL_SIZE, self.CELL_SIZE)

    def get_name(self) -> str:
        return self.name
    
    #Since the board is drawn from top to bottom, the row number has to be adjusted accordingly
    def map_cell_to_index(cell: str) -> tuple:
        column: chr = ord(cell[0]) - 97
        row: int = int(cell[1])
        adj_row = abs(row - 8)
        return adj_row, column
    
    def map_index_to_cell(row: int, column: str) -> str:
        adj_row = abs(row - 8)
        column = chr(column + 97)
        cell = column + str(adj_row)
        return cell