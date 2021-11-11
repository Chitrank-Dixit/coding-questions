"""
DFS
"""


def dfs(graph):
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
                    queue.insert(0, e)
        elif element in queue:
            queue.remove(element)

    return answer


def traversal_dfs_v0(graph):
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
                queue.insert(0, connection)
    return values


def traversal_dfs(vertex, graph, values, seen):
    values.append(vertex)
    seen[vertex] = True
    connections = graph[vertex]
    for i in range(len(connections)):
        connection = connections[i]
        if connection not in seen:
            traversal_dfs(connection, graph, values, seen)

    return values


if __name__ == "__main__":
    graph = [[1, 3], [0], [3, 8], [0, 2, 5, 4], [3, 6], [3], [4, 7], [6], [2]]

    print(dfs(graph=graph))

    print(traversal_dfs_v0(graph=graph))

    print(traversal_dfs(vertex=0, graph=graph, values=[], seen={}))
