"""
binary search
"""
import math


def binary_search(array, left, right, target):
    if left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return binary_search(array, left, mid - 1, target)
        elif array[mid] < target:
            return binary_search(array, mid + 1, right, target)
    return None


def binary_search_v1(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        found_val = array[mid]
        if found_val == target:
            return mid
        elif found_val < target:
            left = mid + 1
        elif found_val > target:
            right = mid - 1
    return None


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 8
    print(binary_search(array=array, left=0, right=9, target=target))

    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 8
    print(binary_search_v1(array=array, target=target))
