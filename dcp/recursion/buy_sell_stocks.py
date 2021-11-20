"""
Buy sell stocks
prices = [7,1, 5, 3, 6, 4]
"""


def buy_sell(prices, i, j, memo):
    if j > i:
        if i in memo and j in memo[j]:
            return memo[i][j]
        if j == (len(prices) - 1) and i <= (len(prices) - 1):
            return max(prices[j] - prices[i], buy_sell(prices, i + 1, j, memo))
        return max(
            prices[j] - prices[i],
            max(
                buy_sell(prices, i, j + 1, memo),
                buy_sell(prices, i + 1, j, memo),
            ),
        )
    return 0


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(buy_sell(prices, i=0, j=1, memo={}))

    prices = [7, 6, 4, 3, 1]
    print(buy_sell(prices, i=0, j=1, memo={}))
