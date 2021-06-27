"""

"""


def quicksort(array, left, right):
    if left < right:
        partition_index = partition(array, left, right)
        quicksort(array, left, partition_index - 1)
        quicksort(array, partition_index + 1, right)


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


if __name__ == "__main__":
    array = [2, 7, 8, 6, 4, 1, 9, 3, 5]
    quicksort(array, 0, 8)
    print(array)
