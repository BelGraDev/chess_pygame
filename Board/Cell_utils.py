class Cell_utils:

    #Since the board is drawn from top to bottom, the row number has to be adjusted accordingly
    def map_cell_to_index(cell: str) -> tuple:
        column: chr = ord(cell[0]) - 97
        row: int = int(cell[1])
        adj_row = abs(row - 8)
        return adj_row, column

    def map_index_to_cell(row: int, column: str) -> str:
        adj_row = abs(row - 8)
        column = chr(column + 97)
        cell = column + str(adj_row)
        return cell

    def is_cell_empty(cell: str, board) -> bool:

        try:
            board.board[cell]
            return False
        except KeyError:
            return True

    def is_white_piece(cell:str, board) -> bool:

        piece = board.board[cell]
        return True if piece.type == "w" else False