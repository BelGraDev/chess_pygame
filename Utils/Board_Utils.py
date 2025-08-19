class Board_Utils:

    def move_piece_in_board(board: dict, prev_cell_name: str, next_cell_name: str):
        prev_piece = board[prev_cell_name]
        possible_moves = prev_piece.possible_moves(prev_cell_name)
        if next_cell_name in possible_moves:
            
            board[next_cell_name] = prev_piece
            del board[prev_cell_name]
            return prev_piece
        
        return None
    
    def restore_last_state(board: dict, prev_piece, original_next_piece, prev_cell_name: str, next_cell_name: str) -> None:
        board[prev_cell_name] = prev_piece
        if original_next_piece:
            board[next_cell_name] = original_next_piece
        else:
            del board[next_cell_name]

