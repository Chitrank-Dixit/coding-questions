"""
Matrix traversal using DFS
"""
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def dfs(matrix, row, col, seen, values):
    if (
        row < 0
        or col < 0
        or row >= len(matrix)
        or col >= len(matrix[0])
        or seen[row][col]
    ):
        return
    values.append(matrix[row][col])
    seen[row][col] = True

    for i in range(len(directions)):
        current_dir = directions[i]
        dfs(matrix, row + current_dir[0], col + current_dir[1], seen, values)


def traversal_DFS(matrix):
    seen = []
    for i in range(len(matrix)):
        current_arr = []
        for j in range(len(matrix[i])):
            current_arr.append(False)
        seen.append(current_arr)
    values = []
    dfs(matrix, 0, 0, seen, values)
    return values


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
    ]
    print(traversal_DFS(matrix=matrix))
