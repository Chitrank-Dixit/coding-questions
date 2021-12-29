"""
On a given nxn chessboard, a knight piece will start at the r-th row and c-th column. The knight will attempt to
make k moves.

A knight can move in 8 possible ways. Each move will choose one of these 8 at random. The knight continues moving until
it finishes k moves or it moves off the chessboard. Return the probability that the knight is on the chessboard after it
finishes moving.
"""

directions = [
    [-2, -1],
    [-2, 1],
    [-1, 2],
    [1, 2],
    [2, 1],
    [2, -1],
    [1, -2],
    [-1, -2],
]


def knight_probability(N, k, r, c):
    if r < 0 or r >= N or c < 0 or c >= N:
        return 0
    if k == 0:
        return 1
    res = 0
    for i in range(len(directions)):
        dir = directions[i]
        res += knight_probability(N, k - 1, r + dir[0], c + dir[1]) / 8

    return res


def recurse(N, k, r, c, dp):
    if r < 0 or r >= N or c < 0 or c >= N:
        return 0
    if k == 0:
        return 1

    if k in dp and r in dp[k] and c in dp[k][r] and dp[k][r][c] is not None:
        return dp[k][r][c]

    res = 0
    for i in range(len(directions)):
        dir = directions[i]
        res += recurse(N, k - 1, r + dir[0], c + dir[1], dp) / 8

    dp[k][r][c] = res
    return dp[k][r][c]


def knight_probability_dp(N, k, r, c):
    dp = {}
    for i in range(k + 1):
        inner_dict = {}
        for j in range(N):
            third = {}
            for k in range(N):
                third[k] = None
            inner_dict[j] = third
        dp[i] = inner_dict

    return recurse(N, k, r, c, dp)


def knight_probability_dp_1(N, k, r, c):
    dp = {}
    for i in range(k + 1):
        inner_dict = {}
        for j in range(N):
            third = {}
            for k in range(N):
                third[k] = None
            inner_dict[j] = third
        dp[i] = inner_dict
    dp[0][r][c] = 1
    for step in range(k + 1):
        for row in range(N):
            for col in range(N):
                for i in range(len(directions)):
                    dir = directions[i]
                    prev_row = row + dir[0]
                    prev_col = col + dir[1]
                    if (
                        prev_row >= 0
                        and prev_row < N
                        and prev_col >= 0
                        and prev_col < N
                    ):
                        dp[step][row][col] += (
                            dp[step - 1][prev_row][prev_col] / 8
                        )

    res = 0
    for i in range(N):
        for j in range(N):
            res += dp[k][i][j]
    return res


def knight_probability_dp_1_op(N, k, r, c):
    prev_dp = {}
    for j in range(N):
        third = {}
        for k in range(N):
            third[k] = 0
        prev_dp[j] = third

    curr_dp = {}
    for j in range(N):
        third = {}
        for k in range(N):
            third[k] = 0
        curr_dp[j] = third

    prev_dp[r][c] = 1
    for step in range(k + 1):
        for row in range(N):
            for col in range(N):
                for i in range(len(directions)):
                    dir = directions[i]
                    prev_row = row + dir[0]
                    prev_col = col + dir[1]
                    if (
                        prev_row >= 0
                        and prev_row < N
                        and prev_col >= 0
                        and prev_col < N
                    ):
                        curr_dp[row][col] += prev_dp[prev_row][prev_col] / 8

    prev_dp = curr_dp

    curr_dp = {}
    for j in range(N):
        third = {}
        for k in range(N):
            third[k] = 0
        curr_dp[j] = third

    res = 0
    for i in range(N):
        for j in range(N):
            res += prev_dp[i][j]
    return res


if __name__ == "__main__":
    N = 6
    k = 2
    r = 2
    c = 2
    print(knight_probability(N, k, r, c))

    print(knight_probability_dp(N, k, r, c))

    print(knight_probability_dp_1(N, k, r, c))

    print(knight_probability_dp_1_op(N, k, r, c))
