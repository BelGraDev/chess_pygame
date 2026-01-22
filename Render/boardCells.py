from pygame import Rect
from .ui import UI
from Utils.Cell_utils import map_index_to_cell, map_cell_to_index

class Cell(Rect, UI):

    def __init__(self, coord: tuple[float, float], name: str, color: tuple[int, ...]) -> None:

        self.name = name
        self.color = color
        x, y = coord
        super().__init__(x, y,  self.CELL_SIZE, self.CELL_SIZE)

    def __str__(self) -> str:
        return self.__repr__()
    
    def __repr__(self) -> str:
        return f'Cell(name: {self.name!r}, color: {self.color})'


class BoardCells(UI):

    def __init__(self):
        self.board_cells = self._init_board_cells()


    def _init_board_cells(self) -> list[list[Cell]]:
        board_cells: list[list[Cell]] = [[self._create_cell(row, col) for col in range(8)]
                                                                    for row in range(8)]
        return board_cells
    
    def _create_cell(self, row: int, col: int) -> Cell:
        x = self.MARGIN_SIZE + col * self.CELL_SIZE
        y = self.MARGIN_SIZE + row * self.CELL_SIZE
        cell_name = map_index_to_cell(row, col)
        color = self.WHITE_COLOR if (row + col) % 2 == 0 else self.GREY_COLOR       
        return Cell((x, y), cell_name, color)

    def __getitem__(self, key: str | tuple[int, int]) -> Cell:
        if isinstance(key, str):
            row, col = map_cell_to_index(key)
            cell = self.board_cells[row][col]
            return cell
        else:
            row, col = key
            return self.board_cells[row][col]

