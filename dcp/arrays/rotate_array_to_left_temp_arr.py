# Python code to implement the above approach
def rotate(L, d, n):
    new_lis = []
    new_lis =  L[d:]+L[0:d]
    return new_lis


if __name__ == '__main__':
    arr = [1, 7, 3, 4, 5, 6]
    d = 2
    N = len(arr)

    # Function call
    arr = rotate(arr, d, N)
    for i in arr:
        print(i, end=" ")
