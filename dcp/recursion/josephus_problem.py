"""
josephus problem: https://www.scaler.in/josephus-problem/
"""


def josephus(v, k, index, ans):
    if len(v) == 1:
        print(v[0])
        return

    index = (index + k) % (len(v))
    v.pop(index)
    josephus(v, k, index, ans)
    return


def main():
    n = 40
    k = 7
    index = 0
    ans = -1
    v = []
    for i in range(1, n + 1):
        v.append(i)
    k -= 1
    josephus(v, k, index, ans)
    return


if __name__ == "__main__":
    print(main())
