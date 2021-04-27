def maximum_sum_kadane(arr):
    max_sum = arr[0]
    current_sum = max_sum
    for i in range(len(arr)):
        current_sum = max(arr[i] + current_sum, arr[i])
        max_sum = max(current_sum, max_sum)

    return max_sum


if __name__ == "__main__":
    arr = [-2, 2, 5, -11, 6]
    print(maximum_sum_kadane(arr))
