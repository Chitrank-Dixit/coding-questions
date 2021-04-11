"""


"""


def median_v1(arr):
    median_index = 0
    arr = sorted(arr)
    if len(arr) % 2 == 0:
        median_index = len(arr) // 2
    elif len(arr) % 2 != 0:
        median_index = (((len(arr) - 1) / 2) + ((len(arr) + 1) / 2)) // 2
    return arr[int(median_index)]


if __name__ == "__main__":
    arr = [1, 5, 2, 6, 4, 7, 2, 8, 9]
    print(median_v1(arr=arr))

    arr = [1, 5, 2, 6, 4, 2, 8, 9]
    print(median_v1(arr=arr))
