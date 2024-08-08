# Python program to implement the above approach

# Function to left rotate arr[] of size n by d


def rotate(arr, d, n):
    p = 1
    while(p <= d):
        last = arr[len(arr) - 1]
        for i in range(n - 1, -1, -1):
            arr[i] = arr[i - 1]
        arr[0] = last
        p = p + 1

# Function to print an array


def printArray(arr, size):
    for i in range(size):
        print(arr[i], end=" ")


# Driver code
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
d = 2

# Function calling
rotate(arr, d, n)
printArray(arr, n)
