# Python program to implement the above approach

# Function to left rotate arr[] of size n by d


def rotate(arr, d, n):
    p = 1
    while(p <= d):
        last = arr[0]
        for i in range(n - 1):
            arr[i] = arr[i + 1]
        arr[n - 1] = last
        p = p + 1

# Function to print an array


def printArray(arr, size):
    for i in range(size):
        print(arr[i], end=" ")


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    n = len(arr)
    d = 2

    # Function calling
    rotate(arr, d, n)
    printArray(arr, n)
