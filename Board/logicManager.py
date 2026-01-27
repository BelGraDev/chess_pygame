from .Pieces import Piece
from .Move import Step, MoveType, Move
from Utils.Board_Utils import move_piece_in_board
from Board import BoardStatus
from .gameLogic.SpecialMovesLogic import castle, want_to_castle, manage_passant, can_kill_passant
from .gameLogic.MoveValidator import is_valid_move
from .gameLogic.gameLogic import is_end_game, pawn_ascension, move_to_cell, can_color_play, complete_promotion
from .gameLogic.aiLogic import get_best_ai_move
from Interfaces.ILogicManager import ILogicManager
from typing import Optional

class LogicManager(ILogicManager):

    def __init__(self) -> None:
        self.board_status = BoardStatus()


    def move(self, prev_cell_name: str, next_cell_name: str) -> MoveType:
        step = Step(prev_cell_name, next_cell_name)
        move = Move(self.board_status, step)

        if move.type is not MoveType.TEAMMATE:
            if not is_valid_move(self.board_status, step):
                return MoveType.NOT_AVAILABLE
            else: 

                if want_to_castle(self.board_status, step):
                    king = self.get_piece(prev_cell_name)
                    if not self.board_status.is_king_in_check(king.type):
                        castle(self.board_status, step)
                        move.type = MoveType.CASTLE
                    else:
                        return MoveType.NOT_AVAILABLE
                else:
                    _can_kill_passant = can_kill_passant(self.board_status, step)
                    move_piece_in_board(self.board_status, step, _can_kill_passant)
                    manage_passant(self.board_status, step)
                    if _can_kill_passant:
                        return MoveType.PASSANT_PAWN
                    if self.pawn_ascension(next_cell_name):
                        return MoveType.PAWN_ASCENSION

                self.board_status.update_king_cell(next_cell_name, self.board_status.turn)

                end_game = is_end_game(self.board_status)
                if end_game:
                    return end_game
        return move.type


    def get_best_ai_move(self, ai_turn: str) -> Optional[tuple[str, str]]:
        return get_best_ai_move(self.board_status, ai_turn)


    def get_piece(self, cell_name: str) -> Piece:
        return self.board_status[cell_name]
    

    def get_piece_if_any(self, cell_name: str) -> Optional[Piece]:
        return self.board_status.get(cell_name)


    def get_turn(self) -> str:
        return self.board_status.turn
    

    def get_board(self) -> BoardStatus:
        return self.board_status
    

    def can_color_play(self, cell_name: str) -> bool:
        return can_color_play(self.board_status, cell_name)
    
        
    def move_to_cell(self, next_cell_name: str) -> None:
        move_to_cell(self.board_status, next_cell_name)

        
    def pawn_ascension(self, cell_name: str):
        return pawn_ascension(self.board_status, cell_name)
    

    def ascension_pieces(self) -> list[Piece]:
        return self.board_status.ascension_pieces()
    

    def complete_promotion(self, cell_name: str, piece: Piece) -> None:
        complete_promotion(self.board_status, cell_name, piece)

    def is_end_game(self) -> bool:
        return self.board_status.is_end_game

    

