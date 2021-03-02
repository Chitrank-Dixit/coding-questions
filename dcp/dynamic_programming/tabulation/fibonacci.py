def fibonacci(n):
    dp = [0 for i in range(n)]
    dp[0] = 1

    for i in range(1, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]


def fibonacci_v1(n):
    dp = [0 for i in range(n + 1)]
    dp[1] = 1

    for i in range(0, n + 1):
        if not (i + 1) > n:
            dp[i + 1] += dp[i]
        if not (i + 2) > n:
            dp[i + 2] += dp[i]
    return dp[n]


if __name__ == "__main__":
    print(fibonacci(7))
    print(fibonacci(50))

    print(fibonacci_v1(7))

    print(fibonacci_v1(50))
