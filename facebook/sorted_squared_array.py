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


def sorted_squared_array(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] * arr[i]

    return merge_sort(arr)


def sorted_squared_array_v1(arr):

    result = [0 for i in range(len(arr))]
    left = 0
    right = len(arr) - 1
    i = len(arr) - 1
    while i >= 0:
        if abs(arr[left]) > arr[right]:
            result[i] = arr[left] * arr[left]
            left += 1
        else:
            result[i] = arr[right] * arr[right]
            right -= 1
        i -= 1
    return result


if __name__ == "__main__":
    arr = [-6, -5, -4, 1, 2, 3, 4]
    print(sorted_squared_array(arr))

    arr = [-6, -7, -4, 7, 6, 4]
    print(sorted_squared_array(arr))

    arr = [-6, -5, -4, 1, 2, 3, 4]
    print(sorted_squared_array_v1(arr))

    arr = [-6, -7, -4, 7, 6, 4]
    print(sorted_squared_array_v1(arr))
