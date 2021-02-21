# implementing merge sort algorithm
# p<=q<r
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


if __name__ == "__main__":
    lis = [6, 5, 4, 3, 2, 1]
    merge_lis = merge_sort(lis)
    print("Sorted list is: ", merge_lis)
