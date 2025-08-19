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
    
    def _highlight_cell(self, cell_name) -> None:
        piece = self.board.board[cell_name]
        cell = self.cell_highlighted = self.chessUI.get_cell_rect(cell_name)
        self.chessUI.draw_highlight(piece, cell)

    def _unhighlight_cell(self, cell) -> None:
        self.cell_highlighted = None
        self.chessUI.draw_empty_cell(cell)

    def _render_possible_moves(self, cell_name) -> list:
        piece = self.board.board[cell_name]
        self.possible_moves = piece.possible_moves(cell_name)
        for next_cell_name in self.possible_moves:
            next_cell = self.chessUI.get_cell_rect(next_cell_name)
            self.chessUI.draw_possible_move(next_cell)
        return self.possible_moves
    
    def _undraw_possible_moves(self, moved_to, possible_moves) -> None: 
        for move in possible_moves:
            if move != moved_to:
                cell = self.chessUI.get_cell_rect(move)
                
                if Cell_utils.is_cell_empty(move, self.board):
                    self.chessUI.draw_empty_cell(cell)
                else:
                    piece = self.board.board.get(move)
                    self.chessUI.draw_replacement_pieces(piece, cell)

    def render_move(self, cell_name) -> None:
        prev_cell = self.cell_highlighted
        if prev_cell:
            move_result = self.board.move(prev_cell.name, cell_name)
            print(move_result)
            match move_result:

                case MoveType.EMPTY_CELL | MoveType.CAPTURE:
                    self._move_to_cell(cell_name)
                    self._unhighlight_cell(prev_cell)
                    self._undraw_possible_moves(cell_name, self.possible_moves)

                case MoveType.CHECK_MATE:
                    mate_color = self.board.turn
                    self._move_to_cell(cell_name)
                    self._unhighlight_cell(prev_cell)
                    self._undraw_possible_moves(cell_name, self.possible_moves)
                    self.chessUI.render_mate(mate_color)

                case MoveType.TEAMMATE:
                    self._switch_focus(prev_cell, cell_name)
                    return
                
                case _:
                    return
        else:
            try:
                if not self.board.can_color_play(cell_name): return

                self._highlight_cell(cell_name)
                self._render_possible_moves(cell_name)
            except KeyError:
                pass

    def _redraw_piece_cell(self, cell_name):
        cell = self.chessUI.get_cell_rect(cell_name) 
        piece = self.board.board[cell_name]
        self.chessUI.draw_replacement_pieces(piece, cell)

    def _move_to_cell(self, cell_name) -> None:
        self.board.move_to_cell(cell_name)
        self._redraw_piece_cell(cell_name)
        
    def _switch_focus(self, prev_cell, cell_name) -> None:

        self._highlight_cell(cell_name)
        self._redraw_piece_cell(prev_cell.name)
        self._undraw_possible_moves(None, self.possible_moves)
        self._render_possible_moves(cell_name)



