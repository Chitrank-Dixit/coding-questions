# A Dynamic Programming based Python
# Program for 0-1 Knapsack problem
# Returns the maximum value that can
# be put in a knapsack of capacity M


def rod_cutting(M, length, prices, n):
    K = [[0 for x in range(M + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(M + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif length[i - 1] <= w:
                K[i][w] = max(
                    prices[i - 1] + K[i][w - length[i - 1]], K[i - 1][w]
                )
            else:
                K[i][w] = K[i - 1][w]

    return K[n][M]


if __name__ == "__main__":
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    length = [1, 2, 3, 4, 5, 6, 7, 8]
    N = 8
    n = len(prices)
    print(rod_cutting(N, length, prices, n))
