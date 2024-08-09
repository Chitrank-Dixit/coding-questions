# Python code to implement the approach

# Returns count of rotations
# for an array which is first sorted
# in ascending order, then rotated
def countRotations(arr, n):
    pivot = findPivot(arr, n)
    return pivot + 1

# find the pivot
def findPivot(arr, n):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        if mid < high and arr[mid] > arr[mid + 1]:
            return mid
        if mid > low and arr[mid - 1] > arr[mid]:
            return mid - 1
        if arr[low] > arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# Driver Code
if __name__ == "__main__":
    arr = [15, 18, 2, 3, 6, 12]
    n = len(arr)
    print(countRotations(arr, n))
