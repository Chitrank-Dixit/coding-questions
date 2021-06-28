"""
Given an array of integers sorted in ascending order, return the starting and ending index of given target value in an
array, i.e. [x, y]

Your solution should run in O(logN) time
"""


def binary_search(array, target):
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


def search_range(array, target):
    index_found = binary_search(array, target)
    result = []
    if index_found:
        result.append(index_found)
        i = index_found - 1
        j = index_found + 1
        while i >= 0 and j < len(array):
            if array[i] == target:
                result.insert(0, i)

            if array[j] == target:
                result.append(j)
            i -= 1
            j += 1

    return result


def binary_search_v1(array, left, right, target):
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


def search_range_v1(array, target):
    if len(array) == 0:
        return []
    first_pos = binary_search_v1(array, 0, len(array) - 1, target)
    if not first_pos:
        return []

    start_pos = first_pos
    end_pos = first_pos
    temp1 = None
    temp2 = None

    while start_pos is not None:
        temp1 = start_pos
        start_pos = binary_search_v1(array, 0, start_pos - 1, target)

    start_pos = temp1

    while end_pos is not None:
        temp2 = end_pos
        end_pos = binary_search_v1(array, end_pos + 1, len(array) - 1, target)

    end_pos = temp2

    return [start_pos, end_pos]


if __name__ == "__main__":

    array = [1, 3, 3, 5, 5, 5, 8, 9]
    target = 5
    print(search_range(array=array, target=target))

    array = [1, 2, 3, 4, 5, 6]
    target = 4
    print(search_range(array=array, target=target))

    array = [1, 2, 3, 4, 5]
    target = 9
    print(search_range(array=array, target=target))

    array = []
    target = None
    print(search_range(array=array, target=target))

    array = [1, 3, 3, 5, 5, 5, 8, 9]
    target = 5
    print(search_range_v1(array=array, target=target))

    array = [1, 2, 3, 4, 5, 6]
    target = 4
    print(search_range_v1(array=array, target=target))

    array = [1, 2, 3, 4, 5]
    target = 9
    print(search_range_v1(array=array, target=target))

    array = []
    target = None
    print(search_range_v1(array=array, target=target))
