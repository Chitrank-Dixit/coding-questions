"""
There are a total of n courses to take, labeled from 0 to n-1. Some courses have prerequisite courses. This is
expressed as a pair i.e. [1, 0] which indicates you must take course 0 before taking course 1.

Given the total number of courses and an array of prerequisite pairs, return if it is possible to finish all courses.
"""


def can_finish(n, prerequisite):
    if n == 0:
        return False
    adj_list = [[] for i in range(n)]
    for i in range(len(prerequisite)):
        pair = prerequisite[i]
        adj_list[pair[1]].append(pair[0])

    for v in range(n):
        queue = []
        seen = {}
        for i in range(len(adj_list[v])):
            queue.append(adj_list[v][i])

        while len(queue) > 0:
            current = queue.pop(0)
            seen[current] = True

            if current == v:
                return False
            adjacent = adj_list[current]
            for i in range(len(adjacent)):
                next_v = adjacent[i]

                if next_v not in seen:
                    queue.append(next_v)
    return True


if __name__ == "__main__":
    prerequisite = [[1, 0], [2, 1], [2, 5], [0, 3], [4, 3], [3, 5], [4, 5]]
    n = 6
    print(can_finish(n, prerequisite))

    prerequisite = [[0, 3], [1, 0], [2, 1], [4, 5], [6, 4], [5, 6]]
    n = 7
    print(can_finish(n, prerequisite))

    prerequisite = [[]]
    n = 0
    print(can_finish(n, prerequisite))
