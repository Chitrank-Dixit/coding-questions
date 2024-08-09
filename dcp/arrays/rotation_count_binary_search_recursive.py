# Returns count of rotations for an array which
# is first sorted in ascending order, then rotated
def countRotations(arr, low, high):
    # This condition is needed to handle the case
    # when the array is not rotated at all
    if high < low:
        return 0

    # If there is only one element left
    if high == low:
        return low

    # Find mid
    mid = low + (high - low) // 2

    # Check if element (mid+1) is minimum element.
    # Consider the cases like {3, 4, 5, 1, 2}
    if mid < high and arr[mid + 1] < arr[mid]:
        return mid + 1

    # Check if mid itself is minimum element
    if mid > low and arr[mid] < arr[mid - 1]:
        return mid

    # Decide whether we need to go to left half or
    # right half
    if arr[high] > arr[mid]:
        return countRotations(arr, low, mid - 1)

    return countRotations(arr, mid + 1, high)

# Driver code
if __name__ == "__main__":
    arr = [15, 18, 2, 3, 6, 12]
    N = len(arr)
    print(countRotations(arr, 0, N - 1))
