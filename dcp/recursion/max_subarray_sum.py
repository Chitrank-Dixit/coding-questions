maximum = 0


def subarray_sum(arr, n):
    global maximum
    if n <= 0:
        return arr[n]
    max_here = max(arr[n] + subarray_sum(arr, n - 1), arr[n])
    maximum = max(maximum, max_here)
    return max_here


if __name__ == "__main__":
    arr = [-2, 2, 5, -11, 6]
    subarray_sum(arr, len(arr) - 1)
    print(maximum)
