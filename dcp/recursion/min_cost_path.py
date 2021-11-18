cost = [[1, 3, 5, 8], [4, 2, 1, 7], [4, 3, 2, 3]]

n = len(cost) - 1
m = len(cost[0]) - 1


def min_cost_path(i, j):
    if i == n and j == m:
        return cost[n][m]
    elif i == n:
        return min_cost_path(i, j + 1) + cost[n][j]
    elif j == m:
        return min_cost_path(i + 1, j) + cost[i][m]

    return cost[i][j] + min(min_cost_path(i + 1, j), min_cost_path(i, j + 1))


def min_cost_path_v1(cost, n, m):
    if n == 0 and m == 0:
        return cost[0][0]

    if n == 0:
        return min_cost_path_v1(cost, n, m - 1) + cost[0][m]

    if m == 0:
        return min_cost_path_v1(cost, n - 1, m) + cost[n][0]

    x = min_cost_path_v1(cost, n - 1, m)
    y = min_cost_path_v1(cost, n, m - 1)

    return min(x, y) + cost[n][m]


if __name__ == "__main__":
    i = 0
    j = 0
    print(min_cost_path(i, j))

    print(min_cost_path_v1(cost, n, m))
