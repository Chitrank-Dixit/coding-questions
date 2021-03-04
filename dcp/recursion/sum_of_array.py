def sum_up(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_up(arr[1:])


def sum_up_v1(arr):
    return _sum_up_v1(arr, 0)


def _sum_up_v1(arr, idx):
    if idx == len(arr):
        return 0
    return arr[idx] + _sum_up_v1(arr, idx + 1)


if __name__ == "__main__":
    print(sum_up([1, 5, 2, -9, 4, 3]))

    print(sum_up_v1([1, 5, 2, -9, 4, 3]))
