class Cell_utils:

    #Since the board is drawn from top to bottom, the row number has to be adjusted accordingly
    def map_cell_to_index(cell_name: str) -> tuple:
        column: chr = ord(cell_name[0]) - 97
        row: int = int(cell_name[1])
        adj_row = abs(row - 8)
        return adj_row, column

    def map_index_to_cell(row: int, column: int) -> str:
        adj_row = abs(row - 8)
        column = chr(column + 97)
        cell_name = column + str(adj_row)
        return cell_name

    def is_cell_empty(cell_name: str, board) -> bool:
        return cell_name not in board.board

    def are_teammates(prev_cell_name: str, next_cell_name: str, board: dict) -> bool:

        prev_piece = board[prev_cell_name]
        next_piece = board[next_cell_name]
        return False if prev_piece.type != next_piece.type else True
    
    def get_passant_cell(cell_name: str, turn: str):
        row, col = Cell_utils.map_cell_to_index(cell_name)
        direction = 1 if turn == "w" else -1
        passant_cell = Cell_utils.map_index_to_cell(row + direction, col)
        return passant_cell