from Board.MoveType import MoveType

class GameController:
    def __init__(self, board, chessUI):
        self.board = board
        self.chessUI = chessUI
        self.cell_highlighted = None
        
    def init_board_pieces(self, screen) -> None:
        board = self.board.board
        self.chessUI.init_board(screen)
        self.chessUI.init_pieces(screen, board)

    def selected_cell(self, coord) -> str | None:
            
            for row in range(8):
                for col in range(8):
                    cell = self.chessUI.cells[row][col]
                    if(cell.collidepoint(coord)):
                        return cell.name
                    
            return None
    
    def highlight_cell(self, screen, cell_name) -> None:

            try:
                piece = self.board.board[cell_name]
                cell = self.cell_highlighted = self.chessUI.get_cell_rect(cell_name)
                self.chessUI.draw_highlight(screen, piece, cell)

            except KeyError:
                print("Clicked empty cell")
        
    def unhighlight_cell(self,screen, cell):
        self.cell_highlighted = None
        self.chessUI.draw_unhighlight(screen, cell)


    def render_move(self, screen, cell_name) -> None:
        prev_cell = self.cell_highlighted
        if prev_cell:
            
            move_result = self.board.move(prev_cell.name, cell_name)
            match move_result:

                case MoveType.EMPTY_CELL:
                    self.move_to_cell(screen, cell_name)
                case MoveType.CAPTURE:
                    self.kill(screen, cell_name)
                case MoveType.TEAMMATE:
                    self.switch_focus(screen, prev_cell, cell_name)
                    return
                
            self.unhighlight_cell(screen, prev_cell)

        else:
            self.highlight_cell(screen, cell_name)

    def move_to_cell(self, screen, cell_name) -> None:
        cell = self.chessUI.get_cell_rect(cell_name) 
        piece = self.board.board[cell_name]
        self.chessUI.draw_piece(screen, piece, cell)

    def kill(self, screen, cell_name) -> None:
        cell = self.chessUI.get_cell_rect(cell_name) 
        piece = self.board.board[cell_name]
        self.chessUI.draw_replacement_pieces(screen, piece, cell)


    def switch_focus(self, screen, prev_cell, cell_name) -> None:

        self.highlight_cell(screen, cell_name)
    
        prev_piece = self.board.board[prev_cell.name]
        self.chessUI.draw_replacement_pieces(screen, prev_piece, prev_cell)

