"""
Given a 2D array containing -1'a (walls), 0's (gates) and INF's (empty room). Fill each empty room with the number of
steps to the nearest gate.

If it is impossible to reach a gate, leave INF as the value. INF is equal to 2147483647.
"""

WALL = -1
GATE = 0
EMPTY = 2147483647
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def dfs(matrix, row, col, current_step):
    if (
        row < 0
        or row >= len(matrix)
        or col < 0
        or col >= len(matrix[0])
        or current_step > matrix[row][col]
    ):
        return
    matrix[row][col] = current_step
    for i in range(len(directions)):
        current_dir = directions[i]
        dfs(
            matrix,
            row + current_dir[0],
            col + current_dir[1],
            current_step + 1,
        )


def walls_and_gates(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == GATE:
                dfs(matrix, row, col, 0)
    return matrix


if __name__ == "__main__":
    matrix = []
    print(walls_and_gates(matrix=matrix))

    matrix = [[]]
    print(walls_and_gates(matrix=matrix))

    matrix = [
        [float("inf"), -1, 0, float("inf")],
        [float("inf"), float("inf"), float("inf"), -1],
        [float("inf"), -1, float("inf"), -1],
        [0, -1, float("inf"), float("inf")],
    ]
    print(walls_and_gates(matrix=matrix))
