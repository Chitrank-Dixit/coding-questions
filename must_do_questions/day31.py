"""
Given a 2D array containing 0's (empty cell), 1's (fresh orange) and 2's (rotten orange). Every minute, all fresh orange
immediately adjacent (4 directions) to rotten oranges will not.

How many minutes must pass until all oranges are rotten ?
"""
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

ROTTEN = 2
FRESH = 1
EMPTY = 0


def oranges_rotting(matrix):
    if len(matrix) == 0:
        return 0
    queue = list()
    fresh_oranges = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == ROTTEN:
                queue.append([row, col])
            if matrix[row][col] == FRESH:
                fresh_oranges += 1

    current_queue_size = len(queue)
    minutes = 0
    while len(queue) > 0:
        if current_queue_size == 0:
            minutes += 1
            current_queue_size = len(queue)
        current_orange = queue.pop(0)
        current_queue_size -= 1
        row = current_orange[0]
        col = current_orange[1]

        for i in range(len(directions)):
            current_dir = directions[i]
            next_row = current_dir[0] + row
            next_col = current_dir[1] + col

            if (
                next_row < 0
                or next_row >= len(matrix)
                or next_col < 0
                or next_col >= len(matrix[0])
            ):
                continue
            if matrix[next_row][next_col] == FRESH:
                matrix[next_row][next_col] = 2
                fresh_oranges -= 1
                queue.append([next_row, next_col])

    if fresh_oranges > 0:
        return -1
    return minutes


if __name__ == "__main__":
    matrix = []
    print(oranges_rotting(matrix=matrix))

    matrix = [[], []]
    print(oranges_rotting(matrix=matrix))

    matrix = [
        [2, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 1, 0, 0, 1],
    ]
    print(oranges_rotting(matrix=matrix))

    matrix = [
        [1, 1, 0, 0, 0],
        [2, 1, 0, 0, 0],
        [0, 0, 0, 1, 2],
        [0, 1, 0, 0, 1],
    ]
    print(oranges_rotting(matrix=matrix))
