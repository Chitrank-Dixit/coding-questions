# Python3 program to count
# inversions in an array


def getInvCount(arr, n):
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv_count += 1

    return inv_count


if __name__ == "__main__":
    arr = [5, 1, 2, 3, 4]
    n = len(arr)
    print("Number of inversions are", getInvCount(arr, n))
