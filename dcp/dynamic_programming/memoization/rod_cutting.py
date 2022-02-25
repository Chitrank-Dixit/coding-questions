# We initialize the matrix with -1 at first.
# in memoization make matrix of size of the changing elements and assign new values


def rod_cutting(prices, length, N, n):
    # base conditions
    if n == 0 or N == 0:
        return 0
    if t[n][N] != 0:
        return t[n][N]

    # choice diagram code
    if length[n - 1] <= N:
        t[n][N] = max(
            prices[n - 1] + rod_cutting(prices, length, N - length[n - 1], n),
            rod_cutting(prices, length, N, n - 1),
        )
        return t[n][N]
    elif length[n - 1] > N:
        t[n][N] = rod_cutting(prices, length, N, n - 1)
        return t[n][N]


if __name__ == "__main__":
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    length = [1, 2, 3, 4, 5, 6, 7, 8]
    N = 8
    n = len(prices)
    t = [[0 for i in range(N + 1)] for j in range(n + 1)]
    print(rod_cutting(prices, length, N, n))
