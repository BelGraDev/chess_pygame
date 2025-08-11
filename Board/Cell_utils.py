class Cell_utils:

    #Since the board is drawn from top to bottom, the row number has to be adjusted accordingly
    def map_cell_to_index(cell_name: str) -> tuple:
        print(cell_name)
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

        try:
            board.board[cell_name]
            return False
        except KeyError:
            return True

    def is_white_piece(cell_name:str, board) -> bool:

        piece = board.board[cell_name]
        return True if piece.type == "w" else False