"""
Zero Matrix: Write an algorithm such that if an element is an MxM matrix is 0, its entire row and column are set to 0.
"""


def zero_matrix(arr):
    indexes = set()
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                indexes.add((i, j))

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (i, j) in indexes:
                # fill row to zero
                row = 0
                col = 0
                while col < len(arr[i]):
                    arr[row][col] = 0
                    col += 1

                # fill col to zero
                col = j
                row = 0
                while row < len(arr):
                    arr[row][col] = 0
                    row += 1

    return arr


if __name__ == "__main__":
    arr = [[0, 1, 2, 3], [1, 5, 8, 9], [9, 7, 6, 4]]
    print(zero_matrix(arr))

    arr = [[0, 1, 2, 3], [1, 5, 0, 9], [9, 7, 6, 4]]
    print(zero_matrix(arr))
