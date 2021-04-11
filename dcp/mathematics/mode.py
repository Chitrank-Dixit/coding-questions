"""


"""


def mode(arr):
    mode = 0
    count = 0
    arr = sorted(arr)
    for e in arr:
        if arr.count(e) > count:
            count = arr.count((e))
            mode = e
    return mode


if __name__ == "__main__":
    arr = [1, 5, 2, 6, 4, 7, 2, 8, 9]
    print(mode(arr=arr))

    arr = [1, 5, 2, 6, 4, 2, 8, 9]
    print(mode(arr=arr))
