cost = [[1, 3, 5, 8], [4, 2, 1, 7], [4, 3, 2, 3]]

n = len(cost[0])
m = len(cost)


def min_cost_path_v1(cost, n, m, memo={}):
    memo.update({0: {0: cost[0][0]}})

    for j in range(1, n):
        memo[0][j] = memo[0][j - 1] + cost[0][j]

    for i in range(1, m):
        memo[i][0] = memo[i - 1][0] + cost[i][0]

    for i in range(1, m):
        for j in range(1, n):
            memo[i][j] = min(memo[i - 1][j], memo[i][j - 1]) + cost[i][j]
    return memo[m - 1][n - 1]


if __name__ == "__main__":
    i = 0
    j = 0

    memo = {
        0: {0: None, 1: None, 2: None, 3: None},
        1: {0: None, 1: None, 2: None, 3: None},
        2: {0: None, 1: None, 2: None, 3: None},
    }
    print(min_cost_path_v1(cost, n, m, memo))
