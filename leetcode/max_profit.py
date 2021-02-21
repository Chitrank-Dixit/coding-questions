class Solution:
    def maxProfit(self, prices):
        buy_index = None
        sell_index = None
        prev = 0
        i = 1
        profit = 0
        while i < len(prices):
            if buy_index is None:
                if prices[i] < prices[prev]:
                    buy_index = i
                else:
                    buy_index = prev
                i -= 1
                prev -= 1
            elif sell_index is None:
                if prices[i] > prices[buy_index]:
                    sell_index = i

            if buy_index is not None and sell_index is None:
                if prices[i] < prices[buy_index]:
                    buy_index = i

            if sell_index is not None:
                if prices[i] > prices[sell_index]:
                    sell_index = i
                elif prices[i] < prices[sell_index]:
                    profit += prices[sell_index] - prices[buy_index]
                    buy_index = None
                    sell_index = None
                    i -= 1
                    prev -= 1
            i += 1
            prev += 1

        if buy_index is not None and sell_index is not None:
            profit += prices[sell_index] - prices[buy_index]

        return profit


if __name__ == "__main__":
    s = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(s.maxProfit(prices=prices))

    prices = [1, 2, 3, 4, 5]
    print(s.maxProfit(prices=prices))

    prices = [7, 6, 4, 3, 1]
    print(s.maxProfit(prices=prices))

    prices = [1, 2]
    print(s.maxProfit(prices=prices))

    prices = [3, 2, 6, 5, 0, 3]
    print(s.maxProfit(prices=prices))

    prices = [2, 4, 1]
    print(s.maxProfit(prices=prices))
