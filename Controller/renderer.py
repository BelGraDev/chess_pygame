from Interfaces.IChessUI import IChessUI
from Board.logicManager import LogicManager
from Utils.Cell_utils import map_cell_to_index, map_index_to_cell, is_cell_empty
from Board.Move import MoveType
from .controllerStatus import ControllerStatus
from Board.Pieces import Piece

class Renderer:
    def __init__(self, chessUI: IChessUI, logic_manager: LogicManager, controller_status: ControllerStatus):
        self.chessUI = chessUI
        self.logic_manager = logic_manager
        self.controller_status = controller_status


    def move(self, prev_cell_name: str, next_cell_name: str) -> None:
        self._move_to_cell(next_cell_name)
        self._unhighlight_cell(prev_cell_name)
        self.redraw_list_cells(next_cell_name, self.controller_status.possible_moves_cells)

    def render_castle(self, cell_name: str) -> None:
        row, col = map_cell_to_index(cell_name)

        rook1_cell_name = map_index_to_cell(row, col + 1)
        if self.logic_manager.get_piece_if_any(rook1_cell_name) is None:
            self.chessUI.draw_empty_cell(rook1_cell_name)

        rook2_cell_name = map_index_to_cell(row, col - 2)
        if self.logic_manager.get_piece_if_any(rook2_cell_name) is None:
            self.chessUI.draw_empty_cell(rook2_cell_name)


    def render_passant_kill(self, cell_name: str) -> None:
        row, col = map_cell_to_index(cell_name)
        direction: int = 1 if self.logic_manager.get_turn() == "w" else -1
        passant_cell: str = map_index_to_cell(row + direction, col)
        self.chessUI.draw_empty_cell(passant_cell)

    
    def render_possible_moves(self, cell_name: str) -> None:
        self.controller_status.set_possible_moves(cell_name)
        for next_cell_name in self.controller_status.possible_moves_cells:
            self.chessUI.draw_possible_move(next_cell_name)
    

    def render_end_game(self, type: MoveType, mate_color: str) -> None:
        match type:
            case MoveType.CHECK_MATE:
                self.chessUI.render_mate(mate_color)
            case _:
                self.chessUI.render_tie()
        self.chessUI.render_end_game_buttons()

    
    def redraw_list_cells(self, moved_to: str | None, possible_moves: list[str]) -> None: 
        for move in possible_moves:
            if move != moved_to:                
                if is_cell_empty(move, self.logic_manager.get_board()):
                    self.chessUI.draw_empty_cell(move)
                else:
                    piece = self.logic_manager.get_piece(move)
                    self.chessUI.draw_replacement_pieces(piece, move)


    def ascend_pawn(self, prev_cell_name: str, cell_name: str) -> None:
        ascension_pieces = self.controller_status.ascend_pawn()
        self.chessUI.render_pawn_ascension(cell_name, self.logic_manager.get_turn(), ascension_pieces)
        self._unhighlight_cell(prev_cell_name)
        self.redraw_list_cells(cell_name, self.controller_status.possible_moves_cells)


    def promote_piece(self, cell_name: str) -> None:
        piece = self._get_promoted_piece(cell_name)
        ascending_to = self.chessUI.ascension_cells[0]
        self.logic_manager.complete_promotion(ascending_to, piece)
        self._move_to_cell(ascending_to)
        self.redraw_list_cells(ascending_to, self.chessUI.ascension_cells)
        self.controller_status.promote_piece()

        
    def highlight_cell(self, cell_name: str) -> None:
        self.controller_status.highlight_cell(cell_name)
        piece = self.logic_manager.get_piece(cell_name)
        self.chessUI.draw_highlight(piece, cell_name)


    def switch_focus(self, prev_cell_name: str, cell_name: str) -> None:
        self.highlight_cell(cell_name)
        self._redraw_piece_cell(prev_cell_name)
        self.redraw_list_cells(None, self.controller_status.possible_moves_cells)
        self.render_possible_moves(cell_name)


    def _move_to_cell(self, cell_name: str) -> None:
        self.logic_manager.move_to_cell(cell_name)
        self._redraw_piece_cell(cell_name)


    def _unhighlight_cell(self, cell_name: str) -> None:
        self.controller_status.unhighlight_cell()
        self.chessUI.draw_empty_cell(cell_name)

    
    def _get_promoted_piece(self, cell_name: str) -> Piece:
        index = self.chessUI.ascension_cells.index(cell_name)
        piece = self.controller_status.ascension_pieces[index]
        return piece
    

    def _redraw_piece_cell(self, cell_name: str) -> None:
        piece = self.logic_manager.get_piece(cell_name)
        self.chessUI.draw_replacement_pieces(piece, cell_name)

