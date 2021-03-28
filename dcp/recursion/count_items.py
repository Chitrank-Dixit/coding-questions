def count_items(arr):
    if len(arr) == 1:
        return 1
    if len(arr) == 0:
        return 0
    return 1 + count_items(arr[1:])


if __name__ == "__main__":
    arr = [1, 4, 2, 3, 5, 3, 5]
    print(count_items(arr))
