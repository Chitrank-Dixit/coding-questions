"""
Get kth element in grammer
"""


def solve(n, k):
    if n == 1 and k == 1:
        return 0
    mid = (2 ** (n - 1)) // 2
    if k <= mid:
        return solve(n - 1, k)
    else:
        return 0 if solve(n - 1, k - mid) else 1


if __name__ == "__main__":
    n = 8
    k = 3
    print(solve(n, k))

    n = 8
    k = 2
    print(solve(n, k))

    n = 8
    k = 1
    print(solve(n, k))
