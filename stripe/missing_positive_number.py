"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words,
find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


def get_lowest_positive_integer(array):
    low = 99999999
    high = 0
    num_set = set()

    for element in array:
        if element < low:
            low = element

        if element > high:
            high = element

        num_set.add(element)

    for i in range(low, high + 1):
        if i != 0 and i not in num_set:
            return i
    return None


def get_lowest_positive_integer_v1(array):
    pass


if __name__ == "__main__":
    print(get_lowest_positive_integer(array=[3, 4, -1, 1]))
