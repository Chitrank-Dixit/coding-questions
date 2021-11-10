"""
BFS
"""


def bfs(graph):
    queue = list()
    answer = list()

    queue.extend(graph[0])
    answer.append(0)
    while queue:
        element = queue.pop(0)
        if element not in answer:
            answer.append(element)
            for e in graph[element]:
                if e not in answer:
                    queue.append(e)
        elif element in queue:
            queue.remove(element)

    return answer


if __name__ == "__main__":
    graph = [[1, 3], [0], [3, 8], [0, 2, 5, 4], [3, 6], [3], [4, 7], [6], [2]]

    print(bfs(graph=graph))
