

def mini_subset_sum(arr, n):
    if n == 0:
        return arr[0]

    return arr[n-1] + mini_subset_sum(arr, n-1) - mini_subset_sum(arr, n-1)


if __name__ == "__main__":
    arr = [1, 6, 11, 5]
    n = 4
    print(mini_subset_sum(arr, n))