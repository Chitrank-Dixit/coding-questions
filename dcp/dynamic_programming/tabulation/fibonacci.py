def fibonacci(n):
    dp = [0 for i in range(n)]
    dp[0] = 1

    for i in range(1, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]


if __name__ == "__main__":
    print(fibonacci(7))
