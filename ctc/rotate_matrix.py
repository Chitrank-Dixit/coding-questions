"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to
rotate the image by 90 degrees. Ca you do this in place
"""


def rotate_matrix(arr, n, m):
    zero_arr = []
    for i in range(n):
        inner_arr = []
        for j in range(m):
            inner_arr.append(0)
        zero_arr.append(inner_arr)

    last = len(arr) - 1
    for inner in arr:
        for count, element in enumerate(inner):
            zero_arr[count][last] = element
        last -= 1
    return zero_arr


def rotate_matrix_v1(arr, n, m):
    for i in range(m):
        for j in range(i, n):
            temp = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = temp

    for i in range(n):
        for j in range(n // 2):
            temp = arr[i][j]
            arr[i][j] = arr[i][n - 1 - j]
            arr[i][n - 1 - j] = temp
    return arr


if __name__ == "__main__":
    arr = [[1, 2], [3, 4]]
    print(rotate_matrix(arr, 2, 2))

    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotate_matrix(arr, 3, 3))

    arr = [[1, 2], [3, 4]]
    print(rotate_matrix_v1(arr, 2, 2))

    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotate_matrix_v1(arr, 3, 3))
