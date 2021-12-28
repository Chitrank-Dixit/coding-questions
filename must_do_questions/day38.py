"""
There are n network nodes labelled 1 to N.

Given a times array, containing edges represented by arrays [u. v. w] where is is the source node v is the target node,
and w is the time taken to travel from the source node to the target node.

Send a signal from node k, return how long it takes for all nodes to receive the signal. Return -1 if it's
impossible.
"""
from must_do_questions.day27 import PriorityQueue


def network_delay_time(times, N, k):
    distances = [float("inf") for i in range(N + 1)]
    adj_List = [[] for i in range(len(distances) + 1)]
    distances[k - 1] = 0
    heap = PriorityQueue()
    heap.push(k - 1)
    for i in range(len(times)):
        source = times[i][0]
        target = times[i][1]
        weight = times[i][2]
        adj_List[source - 1].append([target - 1, weight])

    while not heap.is_empty():
        current_vertex = heap.pop()
        adjacent = adj_List[current_vertex]

        for i in range(len(adjacent)):
            neighboring_vertex = adjacent[i][0]
            weight = adjacent[i][1]
            if (distances[current_vertex] + weight) < distances[
                neighboring_vertex
            ]:
                distances[neighboring_vertex] = (
                    distances[current_vertex] + weight
                )
                heap.push(distances[neighboring_vertex])

    ans = max(distances)
    if ans != float("inf"):
        return ans
    return -1


if __name__ == "__main__":
    k = 1
    N = 5
    times = [
        [1, 2, 9],
        [1, 4, 2],
        [2, 5, 1],
        [4, 2, 4],
        [4, 5, 6],
        [3, 2, 3],
        [5, 3, 7],
        [3, 1, 5],
    ]
    print(network_delay_time(times, N, k))
