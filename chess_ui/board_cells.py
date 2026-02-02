from pygame import Rect
import chess_ui.utils.ui as ui
from chess_ui.utils.constants import NUM_CELLS

class Cell(Rect):

    def __init__(self, coord: tuple[float, float], index: int, color: tuple[int, ...]) -> None:

        self.index = index
        self.color = color
        x, y = coord
        super().__init__(x, y,  ui.CELL_SIZE, ui.CELL_SIZE)

    def __str__(self) -> str:
        return self.__repr__()
    
    def __repr__(self) -> str:
        return f'Cell(index: {self.index!r}, color: {self.color})'


class BoardCells:

    def __init__(self):
        self.board_cells = self._init_board_cells()


    def _init_board_cells(self) -> list[Cell]:
        board_cells: list[Cell] = [self._create_cell(index) for index in range(NUM_CELLS)]                                   
        return board_cells
    

    def _create_cell(self, index: int) -> Cell:
        row, col = self._get_row_col(index)
        x = ui.MARGIN_SIZE + col * ui.CELL_SIZE
        y = ui.MARGIN_SIZE + row * ui.CELL_SIZE
        color = self._get_color(row, col)     
        return Cell((x, y), index, color)


    def _get_row_col(self, index: int) -> tuple[int, int]:
        row = int(index / 8)
        col = index % 8
        return row, col
    
    def _get_color(self, row: int, col: int) -> tuple[int,...]:
        return ui.WHITE_COLOR if (row + col) % 2 == 0 else ui.GREY_COLOR       


    def __getitem__(self, key:  int) -> Cell:

        cell = self.board_cells[key]
        return cell

