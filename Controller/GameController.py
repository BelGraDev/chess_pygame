from Board.Move import MoveType
from Utils.Cell_utils import Cell_utils

class GameController:
    def __init__(self, board, chessUI):
        self.board = board
        self.chessUI = chessUI
        self.cell_highlighted = None
        
    def init_board_pieces(self) -> None:
        board = self.board.board
        self.chessUI.init_board()
        self.chessUI.init_pieces(board)
        self.possible_moves = []

    
    def render_move(self, cell_name: str) -> None:
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
                    return
                
                case MoveType.CASTLE:
                    self._move(prev_cell_name, cell_name)
                    self._render_castle(cell_name)

                case _:
                    return
        else:
            try:
                if not self.board.can_color_play(cell_name): return

                self._highlight_cell(cell_name)
                self._render_possible_moves(cell_name)
            except KeyError:
                pass
    
    def _move(self, prev_cell_name: str, next_cell_name: str) -> None:
        self._move_to_cell(next_cell_name)
        self._unhighlight_cell(prev_cell_name)
        self._undraw_possible_moves(next_cell_name, self.possible_moves)
    
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
    
    def _undraw_possible_moves(self, moved_to: str, possible_moves: list) -> None: 
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

    def _redraw_piece_cell(self, cell_name: str) -> None:
        piece = self.board.board[cell_name]
        self.chessUI.draw_replacement_pieces(piece, cell_name)

    def _move_to_cell(self, cell_name: str) -> None:
        self.board.move_to_cell(cell_name)
        self._redraw_piece_cell(cell_name)
        
    def _switch_focus(self, prev_cell_name: str, cell_name: str) -> None:
        self._highlight_cell(cell_name)
        self._redraw_piece_cell(prev_cell_name)
        self._undraw_possible_moves(None, self.possible_moves)
        self._render_possible_moves(cell_name)



