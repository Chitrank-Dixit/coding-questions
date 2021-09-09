"""
Matrix traversal using BFS
"""
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def traversal_BFS(matrix):
    seen = []
    for i in range(len(matrix)):
        current_arr = []
        for j in range(len(matrix[i])):
            current_arr.append(False)
        seen.append(current_arr)
    values = []
    queue = [[0, 0]]

    while len(queue):
        current_position = queue.pop(0)
        row = current_position[0]
        col = current_position[1]

        if (
            row < 0
            or row >= len(matrix)
            or col < 0
            or col >= len(matrix[0])
            or seen[row][col]
        ):
            continue
        seen[row][col] = True
        values.append(matrix[row][col])

        for i in range(len(directions)):
            current_dir = directions[i]
            queue.append([row + current_dir[0], col + current_dir[1]])
    return values


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
    ]
    print(traversal_BFS(matrix=matrix))
