"""
get kth largest element
"""


def quickselect(array, left, right, index_to_find):
    if left < right:
        partition_index = partition(array, left, right)
        if partition_index == index_to_find:
            return array[partition_index]
        elif index_to_find < partition_index:
            return quickselect(array, left, partition_index - 1, index_to_find)
        else:
            return quickselect(
                array, partition_index + 1, right, index_to_find
            )


def swap(array, partition_index, j):
    array[j], array[partition_index] = array[partition_index], array[j]


def partition(array, left, right):
    pivot_element = array[right]
    partition_index = left
    for j in range(left, right):
        if array[j] < pivot_element:
            swap(array, partition_index, j)
            partition_index += 1
    swap(array, partition_index, right)
    return partition_index


def get_kth_largest(array, k):
    index_to_find = len(array) - k
    quickselect(array, 0, len(array) - 1, index_to_find)
    return array[index_to_find]


if __name__ == "__main__":
    array = [2, 7, 8, 6, 4, 1, 9, 3, 5]
    print(get_kth_largest(array, 4))
