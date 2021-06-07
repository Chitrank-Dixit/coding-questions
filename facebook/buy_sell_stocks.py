"""
Given a array of numbers representing the stock prices of a company in chronological order, write a function that
calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can
sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at
10 dollars.
"""


def buy_sell(prices):
    max_profit = 0

    i = 0
    j = 1
    low = prices[i]
    while j < len(prices):
        if low < prices[j]:
            profit = prices[j] - low
            if profit > max_profit:
                max_profit = profit

        if prices[i] < low:
            low = prices[i]

        i += 1
        j += 1
    return max_profit


if __name__ == "__main__":
    prices = [9, 11, 8, 5, 7, 10]
    print(buy_sell(prices))

    prices = [7, 1, 5, 3, 6, 4]
    print(buy_sell(prices))
