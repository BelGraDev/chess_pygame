from Board import LogicManager, PieceColor
from Board.Pieces import Piece
from dataclasses import dataclass, field
from random import randint
from typing import Optional

@dataclass
class ControllerStatus:

    logic_manager: LogicManager
    cell_highlighted: Optional[str] = None
    pawn_ascending = False
    player_turn: PieceColor = field(init=False)
    ai_turn: PieceColor = field(init=False)
    ascension_pieces: list[Piece] = field(default_factory=list[Piece])
    possible_moves_cells: list[str] = field(default_factory=list[str])


    def __post_init__(self) -> None:
        self.player_turn, self.ai_turn = self._calculate_player_and_ai_turn()


    def _calculate_player_and_ai_turn(self) -> tuple[PieceColor, PieceColor]:
        player_turn = PieceColor.WHITE if randint(0, 1) == 0 else PieceColor.BLACK
        ai_turn = PieceColor.WHITE if player_turn == PieceColor.BLACK else PieceColor.BLACK
        return player_turn, ai_turn


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