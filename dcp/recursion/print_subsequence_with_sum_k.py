
def print_subsequences_sum_k(index, res_arr, k_sum):
    if index >= len(arr):
        if k_sum == k:
            print(res_arr)
        return
    res_arr.append(arr[index])
    k_sum += arr[index]
    print_subsequences_sum_k(index + 1, res_arr, k_sum)
    res_arr.remove(arr[index])
    k_sum -= arr[index]
    print_subsequences_sum_k(index + 1, res_arr, k_sum)



if __name__ == "__main__":
    arr = [1, 2, 1]
    k = 2
    print(print_subsequences_sum_k(index=0, res_arr=[], k_sum=0))
