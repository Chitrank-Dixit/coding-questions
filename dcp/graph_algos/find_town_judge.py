# arrays, hash_tables, graphs
def findJudge(N: int, trust):
    in_degree = [0] * (N + 1)
    out_degree = [0] * (N + 1)
    for a in trust:
        out_degree[a[0]] += 1
        in_degree[a[1]] += 1
    # print(in_degree, out_degree)
    for i in range(1, N + 1):
        if in_degree[i] == N - 1 and out_degree[i] == 0:
            return i
    return -1


if __name__ == "__main__":
    n = 2
    trust = [[1,2]]
    print(findJudge(n, trust))

    n = 3
    trust = [[1, 3], [2, 3]]
    print(findJudge(n, trust))

    n = 3
    trust = [[1, 3], [2, 3], [3, 1]]
    print(findJudge(n, trust))