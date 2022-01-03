"""
Find the maximum of two numbers without using any if-else statements, branching, or direct comparisons.
"""

import sys

CHAR_BIT = 8
INT_BIT = sys.getsizeof(int())


def max_v0(x, y):
    return x if x > y else y


def min_v0(x, y):
    return x if x < y else y


def max_v1(x, y):
    return x ^ ((x ^ y) & -(x < y))


def min_v1(x, y):
    return y ^ ((x ^ y) & -(x < y))


def max_v2(x, y):
    return x - ((x - y) & ((x - y) >> (INT_BIT * CHAR_BIT - 1)))


def min_v2(x, y):
    return y + ((x - y) & ((x - y) >> (INT_BIT * CHAR_BIT - 1)))


def absbit32(x, y):
    sub = x - y
    mask = sub >> 31
    return (sub ^ mask) - mask


def max_v3(x, y):
    abs = absbit32(x, y)
    return (x + y + abs) // 2


def min_v3(x, y):
    abs = absbit32(x, y)
    return (x + y - abs) // 2


if __name__ == "__main__":
    # ternary operator
    print(min_v0(12, 34))
    print(max_v0(12, 34))

    # using XOR and comparison operator
    print(min_v1(12, 34))
    print(max_v1(12, 34))

    # Use subtraction and shift
    print(min_v2(12, 34))
    print(max_v2(12, 34))

    # Use absolute value
    print(min_v3(12, 34))
    print(max_v3(12, 34))
