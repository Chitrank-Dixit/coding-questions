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


class Solution:
    """
    example on the left: [1, 3, 0, 2]
    example on the right: [2, 0, 3, 1]
    """

    def solveNQueens(self, n: int):
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions

    def is_valid_state(self, state, n):
        # check if it is a valid solution
        return len(state) == n

    def get_candidates(self, state, n):
        if not state:
            return range(n)

        # find the next position in the state to populate
        position = len(state)
        candidates = set(range(n))
        # prune down candidates that place the queen into attacks
        for row, col in enumerate(state):
            # discard the column index if it's occupied by a queen
            candidates.discard(col)
            dist = position - row
            # discard diagonals
            candidates.discard(col + dist)
            candidates.discard(col - dist)
        return candidates

    def search(self, state, solutions, n):
        if self.is_valid_state(state, n):
            state_string = self.state_to_string(state, n)
            solutions.append(state_string)
            return

        for candidate in self.get_candidates(state, n):
            # recurse
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()

    def state_to_string(self, state, n):
        # ex. [1, 3, 0, 2]
        # output: [".Q..","...Q","Q...","..Q."]
        ret = []
        for i in state:
            string = "." * i + "Q" + "." * (n - i - 1)
            ret.append(string)
        return ret


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

    print(Solution().solveNQueens(n=4))
