def search(mat, n, x):
    if n == 0:
        return -1

    # Traverse through the matrix
    for i in range(n):
        for j in range(n):

            # If the element is found
            if mat[i][j] == x:
                print("Element found at (", i, ",", j, ")")
                return 1

    print(" Element not found")
    return 0


def search_v1(mat, n, x):
    i = 0

    # set indexes for top right element
    j = n - 1
    while i < n and j >= 0:

        if mat[i][j] == x:
            print("n Found at ", i, ", ", j)
            return 1

        if mat[i][j] > x:
            j -= 1

        # if mat[i][j] < x
        else:
            i += 1

    print("Element not found")
    return 0  # if (i == n || j == -1 )


def search_v2(mat, x, i, j):
    if mat[i][j] == x:
        return (i, j)

    if x > mat[i][j]:
        i = i + 1
    elif x < mat[i][j]:
        i = i - 1
    return search_v2(mat, x, i, j)


if __name__ == "__main__":
    mat = [
        [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50],
    ]
    search(mat, 4, 29)

    print("-----------")
    mat = [
        [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50],
    ]
    search_v1(mat, 4, 29)

    print("-----------")
    mat = [
        [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50],
    ]
    mid = (len(mat) // 2) - 1
    print(search_v2(mat, 29, mid, mid))
