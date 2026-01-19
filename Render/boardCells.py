from pygame import Rect
from .ui import UI
from Utils.Cell_utils import map_index_to_cell, map_cell_to_index

class Cell(Rect):
    CELL_SIZE = 75
    def __init__(self, coord: tuple[float, float], name: str, color: tuple[int, int, int, int]) -> None:

        self.name = name
        self.color = color
        Rect.__init__(self, coord[0], coord[1],  self.CELL_SIZE, self.CELL_SIZE)

class BoardCells(UI):
    def __init__(self):
        self.board_cells: list[list[Cell]] = self._init_board_cells()

    def _init_board_cells(self) -> list[list[Cell]]:
        board_cells: list[list[Cell]] = [[],[],[],[],[],[],[],[]]
        for row in range(8):
            for col in range(8):
                x = self.MARGIN_SIZE + col * self.CELL_SIZE
                y = self.MARGIN_SIZE + row * self.CELL_SIZE
                cell_name = map_index_to_cell(row, col)
                color = self.WHITE_COLOR if (row + col) % 2 == 0 else self.GREY_COLOR       
                cell = Cell((x, y), cell_name, color)
                board_cells[row].append(cell)
        return board_cells

    def __getitem__(self, key: str | tuple[int, int]) -> Cell:
        if isinstance(key, str):
            row, col = map_cell_to_index(key)
            cell = self.board_cells[row][col]
            return cell
        else:
            return self.board_cells[key[0]][key[1]]

