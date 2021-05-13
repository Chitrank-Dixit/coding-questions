"""
This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""


def largest_product(arr):
    product = 1
    for i in range(len(arr)):
        if (arr[i] * arr[i - 1] * arr[i - 2]) > product:
            product = arr[i] * arr[i - 1] * arr[i - 2]
    return product


if __name__ == "__main__":
    arr = [-10, -10, 5, 2]
    print(largest_product(arr))

    arr = [-10, -10, -5, 2]
    print(largest_product(arr))
