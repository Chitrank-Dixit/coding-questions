# A Dynamic Programming based Python
# Program for 0-1 Knapsack problem
# Returns the maximum value that can
# be put in a knapsack of capacity W


def coin_change(s, coins, n):
    K = [[0 for x in range(s + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner

    for i in range(n + 1):
        for w in range(s + 1):
            if i == 0 and w != 0:
                K[i][w] = 0
            if w == 0:
                K[i][w] = 1
            elif coins[i - 1] <= w:
                K[i][w] = K[i - 1][w] + K[i][w - coins[i - 1]]
            else:
                K[i][w] = K[i - 1][w]

    return K[n][s]


if __name__ == "__main__":
    coins = [1, 1, 2, 3]
    s = 5
    n = len(coins) - 1
    print(coin_change(s, coins, n))

    coins = [1, 2, 3]
    s = 5
    n = len(coins) - 1
    print(coin_change(s, coins, n))