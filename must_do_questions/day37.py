"""
Topological sort
"""


def can_finish(n, prerequisite):
    in_degree = [0 for i in range(n)]
    adj_list = [[] for i in range(n)]

    for i in range(len(prerequisite)):
        pair = prerequisite[i]
        in_degree[pair[0]] += 1
        adj_list[pair[1]].append(pair[0])

    stack = []
    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            stack.append(i)

    count = 0
    while len(stack) > 0:
        current = stack.pop(0)
        count += 1

        adjacent = adj_list[current]
        for i in range(len(adjacent)):
            next_val = adjacent[i]
            in_degree[next_val] -= 1

            if in_degree[next_val] == 0:
                stack.append(next_val)

    return count == n


if __name__ == "__main__":
    n = 6
    prerequisite = [[1, 0], [2, 1], [2, 5], [0, 3], [4, 3], [3, 5], [4, 5]]
    print(can_finish(n, prerequisite))
