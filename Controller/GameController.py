from Board.Move import MoveType
from Interfaces import IController, IChessUI
from Board.logicManager import LogicManager
from Render.ChessMenu import ChessButton
from .renderer import Renderer
from .controllerStatus import ControllerStatus

class GameController(IController):
    def __init__(self, logic_manager: LogicManager, boardUI: IChessUI):
        self.logic_manager = logic_manager
        self.chessUI = boardUI
        self.controller_status = ControllerStatus(logic_manager)
        self.renderer = Renderer(self.chessUI, self.logic_manager, self.controller_status)

    def init_board_pieces(self) -> None:
        self.chessUI.init_board()
        self.chessUI.init_pieces(self.logic_manager.get_board())

    def render_move(self, cell_name: str) -> None:
        if not self.controller_status.pawn_ascending:

            prev_cell_name = self.controller_status.cell_highlighted

            if prev_cell_name:
                move_result: MoveType = self.logic_manager.move(prev_cell_name, cell_name)
                match move_result:

                    case MoveType.EMPTY_CELL | MoveType.CAPTURE:
                        self.renderer.move(prev_cell_name, cell_name)

                    case MoveType.CHECK_MATE | MoveType.TIE:
                        mate_color: str = self.logic_manager.get_turn()
                        self.renderer.move(prev_cell_name, cell_name)
                        self.renderer.render_end_game(move_result, mate_color)

                    case MoveType.TEAMMATE:
                        self.renderer.switch_focus(prev_cell_name, cell_name)
                    
                    case MoveType.CASTLE:
                        self.renderer.move(prev_cell_name, cell_name)
                        self.renderer.render_castle(cell_name)

                    case MoveType.PAWN_ASCENSION:
                        self.renderer.ascend_pawn(prev_cell_name, cell_name)        

                    case MoveType.PASSANT_PAWN:
                        self.renderer.render_passant_kill(cell_name)
                        self.renderer.move(prev_cell_name, cell_name)

                    case _:
                        return
            else:
                try:
                    if not self.logic_manager.can_color_play(cell_name): return

                    self.renderer.highlight_cell(cell_name)
                    self.renderer.render_possible_moves(cell_name)
                    self.controller_status.set_possible_moves(cell_name)

                except KeyError:
                    pass
        else:
            
            self.renderer.promote_piece(cell_name)


    def check_if_button_pressed(self, coord: tuple[int, int]) -> ChessButton | None:
        for button in self.chessUI.get_end_game_buttons():
            if button.collidepoint(coord):
                return button.type 




