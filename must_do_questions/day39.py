"""
There are n network nodes labelled 1 to N.

Given a times array, containing edges represented by arrays [u. v. w] where is is the source node v is the target node,
and w is the time taken to travel from the source node to the target node.

Send a signal from node k, return how long it takes for all nodes to receive the signal. Return -1 if it's
impossible.
"""


def network_delay_time(times, N, k):
    distances = [float("inf") for i in range(N)]
    distances[k - 1] = 0

    for i in range(N):
        count = 0
        for j in range(len(times)):
            source = times[j][0]
            target = times[j][1]
            weight = times[j][2]

            if (distances[source - 1] + weight) < distances[target - 1]:
                distances[target - 1] = distances[source - 1] + weight
                count += 1
        if count == 0:
            break

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
