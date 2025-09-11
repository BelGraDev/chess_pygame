from Board.Board import Board
from Controller.GameController import GameController
from Render.BoardUI import BoardUI

class PvpMode:

    def __init__(self, screen):
        self.board = Board()
        self.boardUI = BoardUI(screen)
        self.controller = GameController(self.board, self.boardUI)
    
    
    def init_mode(self):

        self.controller.init_board_pieces()
        

    def play(self, coord):
         if not self.board.board_status.is_check_mate:
            cell = self.boardUI.selected_cell(coord)
            if cell:
                self.controller.render_move(cell)
                self.boardUI.render_border()