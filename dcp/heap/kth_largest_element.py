import heapq


def kthLargest(arr, k):
    smallest = []
    for value in arr:
        if len(smallest) < k:
            heapq.heappush(smallest, value)
        else:
            heapq.heappushpop(smallest, value)
    if len(smallest) < k:
        return None
    return smallest[0]


if __name__ == "__main__":
    arr = [1, 5, 2, 6, 3, 8]
    k = 4
    print(kthLargest(arr, k))
