# Python code to implement the above approach


# Function to reverse start to end of array
def reverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end-1


# Function to left rotate arr[] of size n by d
def leftRotate(arr, d):

    if d == 0:
        return
    n = len(arr)
    # in case the rotating factor is
    # greater than array length
    d = d % n
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)


# Function to print an array
def printArray(arr):
    for i in range(0, len(arr)):
        print(arr[i], end=' ')


# Driver code
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    n = len(arr)
    d = 2
    leftRotate(arr, d)
    printArray(arr)
