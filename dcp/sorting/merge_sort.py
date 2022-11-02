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


def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Code to print the list


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


if __name__ == "__main__":
    lis = [6, 5, 4, 3, 2, 1]
    merge_lis = merge_sort(lis)
    print("Sorted list is: ", merge_lis)

    lis = [12, 11, 13, 5, 6, 7]
    merge_lis = merge_sort(lis)
    print("Sorted list is: ", merge_lis)

    lis = [2,0,2,1,1,0]
    merge_lis = merge_sort(lis)
    print(merge_lis)

    print("Other implementation")
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
