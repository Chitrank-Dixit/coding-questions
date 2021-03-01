def count_paths(n, m):
    dp = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        dp[i][0] = 1

    for j in range(m):
        dp[0][j] = 1

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[n - 1][m - 1]


if __name__ == "__main__":
    print(count_paths(3, 3))

    print(count_paths(9, 9))

    print(count_paths(18, 18))
