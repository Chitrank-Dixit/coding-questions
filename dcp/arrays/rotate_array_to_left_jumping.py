# Python code to implement the above approach


# Function to rotate the array left by d positions
def leftRotate(arr, d, n):
    d = d % n
    g_c_d = gcd(d, n)
    for i in range(g_c_d):

        # move i-th values of blocks
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp


# function to print an array
def printArray(arr, size):
    for i in range(size):
        print(arr[i], end=" ")


# Function to get gcd of a and b
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# Driver code
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    n = len(arr)
    d = 2
    leftRotate(arr, d, n)
    printArray(arr, n)
