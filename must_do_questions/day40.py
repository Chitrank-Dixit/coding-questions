"""
For a given staircase, the i-th step is assigned a non-negative cost indicated by a cost array.

Once you pay the cost for a step, you can either climb one or two steps. Find the minimum cost to reach the top of the
staircase. Your first step can either be the first or second step.
"""


def min_cost(cost, n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return cost[n]

    return cost[n] + min(min_cost(cost, n - 1), min_cost(cost, n - 2))


def min_cost_climbing_stairs(cost):
    n = len(cost)
    return min(min_cost(cost, n - 1), min_cost(cost, n - 2))


def min_cost_memoize(cost, n, memo={}):
    if n in memo:
        return memo[n]
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return cost[n]
    memo[n] = cost[n] + min(
        min_cost(cost, n - 1, memo), min_cost(cost, n - 2, memo)
    )
    return memo[n]


def min_cost_climbing_stairs_memoize(cost):
    n = len(cost)
    return min(min_cost(cost, n - 1), min_cost(cost, n - 2))


def min_cost_climbing_stairs_dp(cost):
    dp = {}

    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(0, len(cost)):
        if i < 2:
            dp[i] = cost[i]
        else:
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

    return min(dp[len(cost) - 1], dp[len(cost) - 2])


def min_cost_climbing_stairs_optimized(cost):
    back = cost[0]
    prev = cost[1]

    for i in range(2, len(cost)):
        current = cost[i] + min(prev, back)
        back = prev
        prev = current

    return min(back, prev)


if __name__ == "__main__":
    cost = [20, 15, 30, 5]
    print(min_cost_climbing_stairs(cost))

    print(min_cost_climbing_stairs_memoize(cost))

    print(min_cost_climbing_stairs_dp(cost))

    print(min_cost_climbing_stairs_optimized(cost))
