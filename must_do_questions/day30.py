"""
Given a 2D array containing only 1's (land) and 0's(water) count the number of islands.
"""

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def number_of_islands(matrix):
    if len(matrix) == 0:
        return 0

    island_count = 0
    queue = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                island_count += 1
                queue.append([row, col])
                while len(queue) > 0:
                    current_pos = queue.pop(0)
                    current_row = current_pos[0]
                    current_col = current_pos[1]

                    matrix[current_row][current_col] = 0
                    for i in range(len(directions)):
                        current_dir = directions[i]
                        next_row = current_row + current_dir[0]
                        next_col = current_col + current_dir[1]

                        if (
                            next_row < 0
                            or next_row >= len(matrix)
                            or next_col < 0
                            or next_col >= len(matrix[0])
                        ):
                            continue

                        if matrix[next_row][next_col] == 1:
                            queue.append([next_row, next_col])

    return island_count


if __name__ == "__main__":
    mat = []
    print(number_of_islands(mat))

    mat = [[]]
    print(number_of_islands(mat))

    mat = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 1], [0, 0, 0, 1, 1]]

    print(number_of_islands(mat))

    mat = [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 0, 1]]
    print(number_of_islands(mat))
