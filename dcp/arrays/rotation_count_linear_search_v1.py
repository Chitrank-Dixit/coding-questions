def countRotations(arr, n):
    # Check is array is rotated
    if (arr[0] > arr[n - 1]):

        # Traverse the array
        for i in range(0, n):

            # Index where element is greater
            # than the next element
            if (arr[i] > arr[i + 1]):
                return i + 1

    # Array is not rotated
    return 0

if __name__ == '__main__':
    arr = [15, 18, 2, 3, 6, 12]
    n = len(arr)
    print(countRotations(arr, n))
