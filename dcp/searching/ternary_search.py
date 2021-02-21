# A recursive ternary search function. It returns location of x in
# given array arr[l..r] is present, otherwise -1
def ternarySearch(arr, left, right, x):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = mid1 + (right - left) // 3

        # If x is present at the mid1
        if arr[mid1] == x:
            return mid1

        # If x is present at the mid2
        if arr[mid2] == x:
            return mid2

        # If x is present in left one-third
        if arr[mid1] > x:
            return ternarySearch(arr, left, mid1 - 1, x)

        # If x is present in right one-third
        if arr[mid2] < x:
            return ternarySearch(arr, mid2 + 1, right, x)

        # If x is present in middle one-third
        return ternarySearch(arr, mid1 + 1, mid2 - 1, x)

    # We reach here when element is not present in array
    return -1


if __name__ == "__main__":
    arr = [1, 3, 5, 2, 6, 4, 7, 9, 8]
    search_term = 4
    print(ternarySearch(arr=arr, left=0, right=len(arr) - 1, x=search_term))
