"""
This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the
list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
"""
from dcp.sorting.merge_sort import merge_sort


def median_find(arr):
    sorted_list = merge_sort(arr)
    median = 0.0
    if len(sorted_list) == 1:
        return arr[0]
    if len(sorted_list) % 2 == 0:
        if (
            sorted_list[(len(sorted_list) // 2) - 1]
            + sorted_list[len(sorted_list) // 2]
        ) % 2 == 0:
            median = (
                sorted_list[(len(sorted_list) // 2) - 1]
                + sorted_list[len(sorted_list) // 2]
            ) // 2
        else:
            median = (
                sorted_list[(len(sorted_list) // 2) - 1]
                + sorted_list[len(sorted_list) // 2]
            ) / 2
    elif len(sorted_list) % 2 != 0:
        median = sorted_list[(len(sorted_list) // 2)]

    return median


def print_current_median(arr):
    results = []
    if len(arr) == 1:
        return arr[0]
    for i in range(len(arr)):
        results.append(median_find(arr[: i + 1]))
    return results


def print_current_median_v1(arr, length, index=0):
    if len(arr) == 1:
        return arr[0]
    median_found = []
    if index < length:
        medians = [median_find(arr[: index + 1])] + print_current_median_v1(
            arr=arr, length=length, index=index + 1
        )
        median_found.extend(medians)
    return median_found


if __name__ == "__main__":
    arr = [2, 1, 5, 7, 2, 0, 5]
    # sorted_arr = merge_sort(arr)
    print(print_current_median(arr))  # , index=0, length=len(arr)))

    print(print_current_median_v1(arr, index=0, length=len(arr)))
