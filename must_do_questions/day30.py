"""
Given a 2D array containing only 1's (land) and 0's(water) count the number of islands.
"""


def number_of_islands():
    pass


if __name__ == "__main__":
    mat = []
    print(number_of_islands(mat))

    mat = [[]]
    print(number_of_islands(mat))

    mat = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 1], [0, 0, 0, 1, 1]]

    print(number_of_islands(mat))

    mat = [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 0, 1]]
    print(number_of_islands(mat))
