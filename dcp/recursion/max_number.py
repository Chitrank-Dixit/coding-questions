def max_number(arr, max_num=0):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return max_num

    if arr[0] > max_num:
        max_num = arr[0]

    return max_number(arr[1:], max_num)


if __name__ == "__main__":
    arr = [1, 4, 25, 45, 4, 24, 6, 67, 4, 66, 5]
    print(max_number(arr, 0))
