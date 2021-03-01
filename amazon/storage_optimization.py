"""
Amazon storage optimization question
https://leetcode.com/discuss/interview-question/1021429/Amazon-OA-or-storage-optimization
"""


def solve(n, m, h, v):
    rowSet = set(i for i in range(n + 2))
    colSet = set(i for i in range(m + 2))
    for r in h:
        rowSet.remove(r)
    for c in v:
        colSet.remove(c)
    rowList = sorted(list(rowSet))
    colList = sorted(list(colSet))
    rowMaxDiff, colMaxDiff = 0, 0
    for i in range(1, len(rowList)):
        rowMaxDiff = max(rowMaxDiff, rowList[i] - rowList[i - 1])
    for i in range(1, len(colList)):
        colMaxDiff = max(colMaxDiff, colList[i] - colList[i - 1])
    return rowMaxDiff * colMaxDiff


if __name__ == "__main__":
    n = 6
    m = 6
    h = [4]
    v = [2]
    print(solve(n=n, m=m, h=h, v=v))
