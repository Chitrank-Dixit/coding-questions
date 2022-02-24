
from dcp.dynamic_programming.tabulation.count_subset_sum import subset_sum


def count_with_diff(arr, n, diff):
    arr_sum = sum(arr)

    if (arr_sum + diff) %2 != 0:
        return 0
    else:
        return subset_sum(arr, n, (arr_sum + diff) // 2)


if __name__ == "__main__":
    arr = [1, 1, 2, 3]
    n = 4
    diff = 1
    print(count_with_diff(arr, n, diff))