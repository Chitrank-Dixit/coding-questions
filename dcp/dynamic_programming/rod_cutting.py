import sys

from one_dimensional.util.stop_watch import start_watch, stop_watch_print


def max_profit(li, p):
    if li == 0:
        return 0
    max_p = -sys.maxsize
    for i in range(0, li):
        max_p = max(max_p, p[i] + max_profit(li - i - 1, p))
    return max_p


def max_profit_memo(li, p, cache):
    if li == 0:
        return 0
    if cache[li] != -1:
        return cache[li]
    max_p = -sys.maxsize
    for i in range(0, li):
        max_p = max(max_p, p[i] + max_profit(li - i - 1, p))
    cache[li] = max_p
    return max_p


def max_profit_dp(L, p):
    dp = [0 for _ in range(0, L + 1)]
    for li in range(1, L + 1):
        dp[li] = -sys.maxsize
        for i in range(0, li):
            dp[li] = max(dp[li], p[i] + dp[li - i - 1])
    return dp[L]


def max_profit_dp_reconstruct(L, p):
    dp = [0 for _ in range(0, L + 1)]
    cuts = [i for i in range(0, L + 1)]
    for li in range(1, L + 1):
        dp[li] = -sys.maxsize
        for i in range(0, li):
            if p[i] + dp[li - i - 1] > dp[li]:
                dp[li] = p[i] + dp[li - i - 1]
                cuts[li] = i + 1

    li = L
    cut = cuts[L]
    while cut != 0:
        print(str(cut) + ",", end="")
        li = li - cut
        cut = cuts[li]
    return dp[L]


profits_table = [1, 5, 8, 9, 10, 13, 17, 20, 24, 30]

li = 8
start_watch()
res = max_profit(li, profits_table)
print(res)
stop_watch_print("Recursion {} milli seconds")

cache = [-1 for _ in range(0, li + 1)]
start_watch()
res = max_profit_memo(li, profits_table, cache)
print(res)
stop_watch_print("Memoization {} milli seconds")

start_watch()
res = max_profit_dp(li, profits_table)
print(res)
stop_watch_print("Bottom up {} milli seconds")

res = max_profit_dp_reconstruct(li, profits_table)
print(res)
