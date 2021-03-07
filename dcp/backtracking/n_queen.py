def is_it_safe_to_place(board, row, column):
    r = row - 1
    c = column
    while r >= 0:
        if board[r][c]:
            return False
        r -= 1

    r = row
    c = column - 1

    while c >= 0:
        if board[r][c]:
            return False
        c -= 1

    r = row - 1
    c = column - 1

    while r >= 0 and c >= 0:
        if board[r][c]:
            return False
        r -= 1
        c -= 1

    r = row - 1
    c = column + 1

    while r >= 0 and c < len(board[0]):
        if board[r][c]:
            return False
        r -= 1
        c += 1

    return True


def n_queen(board, row, column, total_queen, queen_placed, ans):

    if queen_placed == total_queen:
        print(ans)
        return

    if column == len(board[0]):
        row += 1
        column = 0

    if row == len(board):
        return

    if is_it_safe_to_place(board, row, column):
        # do
        board[row][column] = True
        # recur
        n_queen(
            board,
            row,
            column + 1,
            total_queen,
            queen_placed + 1,
            ans + f"[{row}-{column}]",
        )
        # undo
        board[row][column] = False

    n_queen(board, row, column + 1, total_queen, queen_placed, ans)


if __name__ == "__main__":
    bs = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    print(
        n_queen(
            board=bs, row=0, column=0, total_queen=4, queen_placed=0, ans=""
        )
    )
