

def sort_without_sorting(arr):
    # dutch national flag algorithm
    lo = 0
    hi = len(arr) - 1
    mid = 0
    while mid <= hi:
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo = lo + 1
            mid = mid + 1
        elif arr[mid] == 1:
            mid = mid + 1
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi = hi - 1
    return arr


def sortArr(arr, n):
    # naive way of sorting this
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0

    # Count the number of 0s, 1s and 2s in the array
    for i in range(n):
        if arr[i] == 0:
            cnt0 += 1

        elif arr[i] == 1:
            cnt1 += 1

        elif arr[i] == 2:
            cnt2 += 1

    # Update the array
    i = 0

    # Store all the 0s in the beginning
    while (cnt0 > 0):
        arr[i] = 0
        i += 1
        cnt0 -= 1

    # Then all the 1s
    while (cnt1 > 0):
        arr[i] = 1
        i += 1
        cnt1 -= 1

    # Finally all the 2s
    while (cnt2 > 0):
        arr[i] = 2
        i += 1
        cnt2 -= 1

    return arr

if __name__ == "__main__":
    arr = [0, 2, 1, 0, 0, 2, 1, 2, 1, 2, 1, 0]
    print(sort_without_sorting(arr))

    arr = [0, 2, 1, 0, 0, 2, 1, 2, 1, 2, 1, 0]
    print(sortArr(arr, len(arr)))
