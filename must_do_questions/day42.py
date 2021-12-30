"""
Sudoku puzzle
"""


def get_box_id(row, col):
    col_val = col // 3
    row_val = (row // 3) * 3
    return row_val + col_val


def solve_sudoku(board):
    n = len(board)
    boxes = [{} for i in range(n)]
    rows = [{} for i in range(n)]
    cols = [{} for i in range(n)]

    for r in range(n):
        for c in range(n):
            if board[r][c] == ".":
                val = board[r][c]
                box_id = get_box_id(r, c)
                boxes[box_id][val] = True
                rows[r][val] = True
                cols[c][val] = True

    return solve_backtracking(board, boxes, rows, cols, 0, 0)


def is_valid(box, row, col, num):
    if box[num] or row[num] or col[num]:
        return False
    else:
        return True


def solve_backtracking(board, boxes, rows, cols, r, c):
    if r == len(board) or c == len(board[0]):
        return True
    else:
        if board[r][c] == ".":
            for num in range(1, 10):
                num_val = str(num)
                board[r][c] = num_val
                box_id = get_box_id(r, c)
                box = boxes[box_id]
                row = rows[r]
                col = cols[c]

                if is_valid(box, row, col, num_val):
                    box[num_val] = True
                    col[num_val] = True
                    row[num_val] = True
                    if c == len(board[0]) - 1:
                        if solve_backtracking(
                            board, boxes, rows, cols, r + 1, 0
                        ):
                            return True
                    else:
                        if solve_backtracking(
                            board, boxes, rows, cols, r, c + 1
                        ):
                            return True

                box.pop(num_val)
                row.pop(num_val)
                col.pop(num_val)
            board[r][c] = "."
        else:
            if c == len(board[0]):
                if solve_backtracking(board, boxes, rows, cols, r + 1, 0):
                    return True
            else:
                if solve_backtracking(board, boxes, rows, cols, r, c + 1):
                    return True


if __name__ == "__main__":
    board = [
        ["5", "3", "", "", "7", "", "", "", ""],
        ["6", "", "", "1", "9", "5", "", "", ""],
        ["", "9", "8", "", "", "", "", "6", ""],
        ["8", "", "", "", "6", "", "", "", "3"],
        ["4", "", "", "8", "", "3", "", "", "1"],
        ["7", "", "", "", "2", "", "", "", "6"],
        ["", "6", "", "", "", "", "2", "8", ""],
        ["", "", "", "4", "1", "9", "", "", "5"],
        ["", "", "", "", "8", "", "", "7", "9"],
    ]

    print(solve_sudoku(board))
