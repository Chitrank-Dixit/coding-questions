# Python program of above implementation Divide and Conquer
def get_min_max(low, high, arr):
    arr_max = arr[low]
    arr_min = arr[low]

    # If there is only one element
    if low == high:
        arr_max = arr[low]
        arr_min = arr[low]
        return arr_max, arr_min

    # If there is only two element
    elif high == low + 1:
        if arr[low] > arr[high]:
            arr_max = arr[low]
            arr_min = arr[high]
        else:
            arr_max = arr[high]
            arr_min = arr[low]
        return arr_max, arr_min
    else:
        # If there are more than 2 elements
        mid = int((low + high) / 2)
        arr_max1, arr_min1 = get_min_max(low, mid, arr)
        arr_max2, arr_min2 = get_min_max(mid + 1, high, arr)

    return max(arr_max1, arr_max2), min(arr_min1, arr_min2)


if __name__ == "__main__":
    arr = [1000, 11, 445, 1, 330, 3000]
    high = len(arr) - 1
    low = 0
    arr_max, arr_min = get_min_max(low, high, arr)
    print('Minimum element is ', arr_min)
    print('Maximum element is ', arr_max)
