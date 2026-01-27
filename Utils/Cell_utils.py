#Since the board is drawn from top to bottom, the row number has to be adjusted accordingly
def map_cell_to_index(cell_name: str) -> tuple[int, int]:
    column: int = ord(cell_name[0]) - 97
    row: int = int(cell_name[1])
    adj_row: int = abs(row - 8)
    return adj_row, column


def map_index_to_cell(row: int, column: int) -> str:
    adj_row = abs(row - 8)
    column_letter = chr(column + 97)
    cell_name = f"{column_letter}{str(adj_row)}"
    return cell_name