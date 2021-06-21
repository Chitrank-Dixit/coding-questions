"""
Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""


def merge_list(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    result = result + left[i:]
    result = result + right[j:]
    return result


def merge_sort(lis):
    if len(lis) < 2:
        return lis
    middle = len(lis) // 2
    left = merge_sort(lis[:middle])
    right = merge_sort(lis[middle:])
    return merge_list(left, right)


def sorted_list_of_squares(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] ** 2

    return merge_sort(arr)


if __name__ == "__main__":
    arr = [-9, -2, 0, 2, 3]
    print(sorted_list_of_squares(arr))
