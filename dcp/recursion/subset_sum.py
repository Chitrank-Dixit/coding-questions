def subset_sum(arr, n, sum):
    if sum == 0:
        return True
    if n == 0:
        return False

    if arr[n - 1] > sum:
        return subset_sum(arr, n - 1, sum)

    return subset_sum(arr, n - 1, sum) or subset_sum(
        arr, n - 1, sum - arr[n - 1]
    )


if __name__ == "__main__":
    arr = [2, 4, 3, 9, 8]
    n = 5
    sum = 13

    print(subset_sum(arr, n, sum))
