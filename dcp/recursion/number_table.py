"""
number table
"""


def table(n, i):
    if i > 10:
        return
    print(f"{n} X {i} : {n*i}")
    return table(n, i + 1)


def table_v1(n, i):
    if i > 10:
        return
    table(n, i + 1)
    if i > 0:
        print(f"{n} X {i} : {n*i}")
    return


if __name__ == "__main__":
    n = 5
    i = 1

    print(table(n, i))

    i = 0
    print(table_v1(n, i))
