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


def traversal_bfs(graph):
    queue = [0]
    values = list()
    seen = dict()
    while len(queue) > 0:
        vertex = queue.pop(0)
        values.append(vertex)
        seen[vertex] = True
        connections = graph[vertex]
        for i in range(len(connections)):
            connection = connections[i]
            if connection not in seen:
                queue.append(connection)
    return values


if __name__ == "__main__":
    graph = [[1, 3], [0], [3, 8], [0, 2, 5, 4], [3, 6], [3], [4, 7], [6], [2]]

    print(bfs(graph=graph))

    print(traversal_bfs(graph=graph))
