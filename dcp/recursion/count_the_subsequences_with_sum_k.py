
def count_subsequences_sum_k(index, res_arr, k_sum):
    if k_sum > k:
        return 0
    if index >= len(arr):
        if k_sum == k:
            return 1
        return 0
    res_arr.append(arr[index])
    k_sum += arr[index]
    l = count_subsequences_sum_k(index + 1, res_arr, k_sum)
    res_arr.remove(arr[index])
    k_sum -= arr[index]
    r = count_subsequences_sum_k(index + 1, res_arr, k_sum)
    return l + r


if __name__ == "__main__":
    arr = [1, 2, 1]
    k = 2
    print(count_subsequences_sum_k(index=0, res_arr=[], k_sum=0))
