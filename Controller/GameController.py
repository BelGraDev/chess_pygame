from Board.Move import MoveType
from Utils.Cell_utils import Cell_utils

class GameController:
    def __init__(self, board, chessUI):
        self.board = board
        self.chessUI = chessUI
        self.cell_highlighted = None
        self.pawn_ascending = False
        self.ascension_pieces = None
        
    def init_board_pieces(self) -> None:
        board = self.board.board
        self.chessUI.init_board()
        self.chessUI.init_pieces(board)
        self.possible_moves = []

    def render_move(self, cell_name: str) -> None:

        if not self.pawn_ascending:

            prev_cell_name = self.cell_highlighted

            if prev_cell_name:
                move_result = self.board.move(prev_cell_name, cell_name)
                match move_result:

                    case MoveType.EMPTY_CELL | MoveType.CAPTURE:
                        self._move(prev_cell_name, cell_name)

                    case MoveType.CHECK_MATE:
                        mate_color = self.board.turn
                        self._move(prev_cell_name, cell_name)
                        self.chessUI.render_mate(mate_color)

                    case MoveType.TEAMMATE:
                        self._switch_focus(prev_cell_name, cell_name)
                    
                    case MoveType.CASTLE:
                        self._move(prev_cell_name, cell_name)
                        self._render_castle(cell_name)

                    case MoveType.PAWN_ASCENSION:
                        self._ascend_pawn(prev_cell_name, cell_name)        

                    case MoveType.PASSANT_PAWN:
                        self._render_passant_kill(cell_name)
                        self._move(prev_cell_name, cell_name)

                    case _:
                        return
            else:
                try:
                    if not self.board.can_color_play(cell_name): return

                    self._highlight_cell(cell_name)
                    self._render_possible_moves(cell_name)
                except KeyError:
                    pass
        else:
            self._promote_piece(cell_name)

    def _move(self, prev_cell_name: str, next_cell_name: str) -> None:
        self._move_to_cell(next_cell_name)
        self._unhighlight_cell(prev_cell_name)
        self._redraw_list_cells(next_cell_name, self.possible_moves)
    
    def _highlight_cell(self, cell_name: str) -> None:
        piece = self.board.board[cell_name]
        self.cell_highlighted = cell_name
        self.chessUI.draw_highlight(piece, cell_name)

    def _unhighlight_cell(self, cell_name: str) -> None:
        self.cell_highlighted = None
        self.chessUI.draw_empty_cell(cell_name)

    def _render_possible_moves(self, cell_name: str) -> list:
        piece = self.board.board[cell_name]
        self.possible_moves = piece.possible_moves(cell_name)
        for next_cell_name in self.possible_moves:
            self.chessUI.draw_possible_move(next_cell_name)
        return self.possible_moves
    
    def _redraw_list_cells(self, moved_to: str, possible_moves: list) -> None: 
        for move in possible_moves:
            if move != moved_to:                
                if Cell_utils.is_cell_empty(move, self.board):
                    self.chessUI.draw_empty_cell(move)
                else:
                    piece = self.board.board.get(move)
                    self.chessUI.draw_replacement_pieces(piece, move)

    def _render_castle(self, cell_name: str) -> None:
        row, col = Cell_utils.map_cell_to_index(cell_name)

        rook1_cell_name = Cell_utils.map_index_to_cell(row, col + 1)
        if self.board.board.get(rook1_cell_name) is None:
            self.chessUI.draw_empty_cell(rook1_cell_name)

        rook2_cell_name = Cell_utils.map_index_to_cell(row, col - 2)
        if self.board.board.get(rook2_cell_name) is None:
            self.chessUI.draw_empty_cell(rook2_cell_name)

    def _render_passant_kill(self, cell_name):
        row, col = Cell_utils.map_cell_to_index(cell_name)
        direction = 1 if self.board.turn == "w" else -1
        passant_cell = Cell_utils.map_index_to_cell(row + direction, col)
        self.chessUI.draw_empty_cell(passant_cell)

    def _redraw_piece_cell(self, cell_name: str) -> None:
        piece = self.board.board[cell_name]
        self.chessUI.draw_replacement_pieces(piece, cell_name)

    def _move_to_cell(self, cell_name: str) -> None:
        self.board.move_to_cell(cell_name)
        self._redraw_piece_cell(cell_name)

    def _ascend_pawn(self, prev_cell_name, cell_name):
        self.pawn_ascending = True
        self.ascension_pieces = self.board.ascension_pieces()
        self.chessUI.render_pawn_ascension(cell_name, self.board.turn, self.ascension_pieces)
        self._unhighlight_cell(prev_cell_name)
        self._redraw_list_cells(cell_name, self.possible_moves)

    def _get_promoted_piece(self, cell_name):
        index_piece = self.chessUI.ascension_cells.index(cell_name)
        piece = self.ascension_pieces[index_piece]
        return piece
            
    def _promote_piece(self, cell_name: str) -> None:
        piece = self._get_promoted_piece(cell_name)
        ascending_to = self.chessUI.ascension_cells[0]
        self.board.complete_promotion(ascending_to, piece)
        self._move_to_cell(ascending_to)
        self._redraw_list_cells(ascending_to, self.chessUI.ascension_cells)
        self.pawn_ascending = False

    def _switch_focus(self, prev_cell_name: str, cell_name: str) -> None:
        self._highlight_cell(cell_name)
        self._redraw_piece_cell(prev_cell_name)
        self._redraw_list_cells(None, self.possible_moves)
        self._render_possible_moves(cell_name)



