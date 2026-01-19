from Board.logicManager import LogicManager
from Board.Pieces import Piece

class ControllerStatus:

    def __init__(self, logic_manager: LogicManager):
        self.cell_highlighted: str | None = None
        self.pawn_ascending = False
        self.ascension_pieces: list[Piece] = []
        self.possible_moves_cells: list[str] = []

        self.logic_manager = logic_manager


    def highlight_cell(self, cell_name: str) -> None:
        self.cell_highlighted = cell_name


    def unhighlight_cell(self) -> None:
        self.cell_highlighted = None


    def ascend_pawn(self) -> list[Piece]:
        self.pawn_ascending = True
        self.ascension_pieces = self.logic_manager.ascension_pieces()
        return self.ascension_pieces
    

    def promote_piece(self) -> None:
        self.pawn_ascending = False

    
    def set_possible_moves(self, cell_name: str) -> None:
        piece = self.logic_manager.get_piece(cell_name)
        self.possible_moves_cells = piece.possible_moves(cell_name)