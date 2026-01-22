from .Pieces import Piece
from .Move import Step, MoveType, Move
from Utils.Board_Utils import move_piece_in_board
from .SpecialMovesLogic import CastleLogic, PassantLogic
from .BoardStatus import BoardStatus
from .MoveValidator import MoveValidator
from .gameLogic import GameLogic
from Interfaces.ILogicManager import ILogicManager

class LogicManager(ILogicManager):

    def __init__(self):
        self.board_status = BoardStatus()
        self.move_validator = MoveValidator(self.board_status)
        self.castleLogic = CastleLogic(self.board_status)
        self.passantLogic = PassantLogic(self.board_status)
        self.game_logic = GameLogic(self.board_status)


    def move(self, prev_cell_name: str, next_cell_name: str) -> MoveType:
        step = Step(prev_cell_name, next_cell_name)
        move = Move(self.board_status, step)

        if move.type is not MoveType.TEAMMATE:
            if not self.move_validator.is_valid_move(step):
                return MoveType.NOT_AVAILABLE
            else: 

                if self.castleLogic.want_to_castle(step):
                    king = self.get_piece(prev_cell_name)
                    if not self.board_status.is_king_in_check(king.type):
                        self.castleLogic.castle(step)
                        move.type = MoveType.CASTLE
                    else:
                        return MoveType.NOT_AVAILABLE
                else:
                    can_kill_passant = self.passantLogic.can_kill_passant(step)
                    move_piece_in_board(self.board_status, step, can_kill_passant)
                    self.passantLogic.manage_passant(step)
                    if can_kill_passant:
                        return MoveType.PASSANT_PAWN
                    if self.pawn_ascension(next_cell_name):
                        return MoveType.PAWN_ASCENSION

                self.board_status.update_king_cell(next_cell_name, self.board_status.turn)

                end_game = self.game_logic.is_end_game()
                if end_game:
                    return end_game
                
        return move.type


    def get_piece(self, cell_name: str) -> Piece:
        return self.board_status[cell_name]
    

    def get_piece_if_any(self, cell_name: str) -> Piece  | None:
        return self.board_status.get(cell_name)


    def get_turn(self) -> str:
        return self.board_status.turn
    

    def get_board(self) -> BoardStatus:
        return self.board_status
    

    def can_color_play(self, cell_name: str) -> bool:
        return self.game_logic.can_color_play(cell_name)
    
        
    def move_to_cell(self, next_cell_name: str) -> None:
        self.game_logic.move_to_cell(next_cell_name)

        
    def pawn_ascension(self, cell_name: str):
        return self.game_logic.pawn_ascension(cell_name)
    

    def ascension_pieces(self) -> list[Piece]:
        return self.board_status.ascension_pieces()
    

    def complete_promotion(self, cell_name: str, piece: Piece) -> None:
        self.game_logic.complete_promotion(cell_name, piece)

    def is_end_game(self) -> bool:
        return self.board_status.is_end_game

    

