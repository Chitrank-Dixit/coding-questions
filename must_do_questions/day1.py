"""
Given an Array of Integers, return the indices of the two numbers that add up to the given target
"""


def num_pairs(arr, target):
    if len(arr) < 2:
        return None

    for i in range(len(arr)):
        num_to_find = target - arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j] == num_to_find:
                return (i, j)
    return None


def num_pairs_v1(arr, target):
    if len(arr) < 2:
        return None
    num_dict = dict()
    for count, element in enumerate(arr):
        if element in num_dict:
            return (num_dict[element], count)
        num_dict[target - element] = count
    return None


if __name__ == "__main__":
    arr = []
    target = 3
    print(num_pairs(arr, target))

    arr = [5]
    target = 8
    print(num_pairs(arr, target))

    arr = [5]
    target = 5
    print(num_pairs(arr, target))

    arr = [1, 6]
    target = 7
    print(num_pairs(arr, target))

    arr = [1, 2, 3, 4, 5]
    target = 25
    print(num_pairs(arr, target))

    arr = [1, 3, 7, 9, 2]
    target = 11
    print(num_pairs(arr, target))

    # nums_pairs v1

    arr = []
    target = 3
    print(num_pairs_v1(arr, target))

    arr = [5]
    target = 8
    print(num_pairs_v1(arr, target))

    arr = [5]
    target = 5
    print(num_pairs_v1(arr, target))

    arr = [1, 6]
    target = 7
    print(num_pairs_v1(arr, target))

    arr = [1, 2, 3, 4, 5]
    target = 25
    print(num_pairs_v1(arr, target))

    arr = [1, 3, 7, 9, 2]
    target = 11
    print(num_pairs_v1(arr, target))
