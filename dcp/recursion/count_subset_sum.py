def subset_sum(arr, n, sum):
    if sum == 0:
        return 1
    if n == 0:
        return 0

    if arr[n - 1] > sum:
        return subset_sum(arr, n - 1, sum)

    return subset_sum(arr, n - 1, sum) + subset_sum(
        arr, n - 1, sum - arr[n - 1]
    )


if __name__ == "__main__":
    arr = [2, 4, 3, 9, 8]
    n = 5
    sum = 13

    print(subset_sum(arr, n, sum))

    arr = [2, 3, 5, 6, 8, 10]
    n = 6
    sum = 10

    print(subset_sum(arr, n, sum))