def find_longet_subarray_by_sum(arr, s):
    result = [-1]
    sums = 0
    left = 0
    right = 0

    while right < len(arr):
        sums += arr[right]
        while left < right and sums > s:
            left += 1
            sums -= arr[left]

        if sums == s and (
            len(result) == 1 or (result[1] - result[0]) < (right - left)
        ):
            result = [left + 1, right + 1]

        right += 1
    return result


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    s = 15
    print(find_longet_subarray_by_sum(arr, s))
