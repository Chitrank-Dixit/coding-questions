
def reverse_array(arr):
    i = 0
    j = len(arr) - 1

    mid = len(arr) // 2
    while i < mid and j >= mid:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr

def rec_reverse_array(arr, start, end):
    if start < end:
        arr[start], arr[end] = arr[end], arr[start]

        return rec_reverse_array(arr, start+1, end-1)
    return arr


if __name__ == "__main__":
    arr = [1, 6, 2, 5, 3, 4]
    print(reverse_array(arr))

    arr = [1, 6, 2, 5, 3, 4]
    print(rec_reverse_array(arr, start=0, end=len(arr) - 1))