def print_subsequences(index, res_arr):
    # power set
    if index >= len(arr):
        print(res_arr)
        return;
    res_arr.append(arr[index])
    print_subsequences(index + 1, res_arr)
    res_arr.remove(arr[index])
    print_subsequences(index + 1, res_arr)



if __name__ == "__main__":
    arr = [3, 1, 2]
    print(print_subsequences(index=0, res_arr=[]))
