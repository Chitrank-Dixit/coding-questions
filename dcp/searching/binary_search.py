def binary_search(arr, left, right, search_term):
    if len(arr) == 0:
        return -1

    if arr[left] == search_term:
        return left

    elif arr[right] == search_term:
        return right

    return binary_search(
        arr, left=left + 1, right=right - 1, search_term=search_term
    )


def binary_search_v1(arr, left, right, search_term):
    if right >= left:
        mid = left + (right - left) // 2

        if arr[mid] == search_term:
            return mid

        if arr[mid] > search_term:
            return binary_search_v1(arr, left, mid - 1, search_term)

        else:
            return binary_search_v1(arr, mid + 1, right, search_term)
    else:
        return -1


def binary_search_v2(arr, search_term):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == search_term:
            return mid
        if guess > search_term:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    arr = [1, 4, 2, 3, 5, 8, 6, 7]
    print(binary_search_v1(arr=arr, left=0, right=len(arr) - 1, search_term=8))

    arr = [1, 4, 2, 3, 5, 8, 6, 7]
    print(binary_search_v2(arr=arr, search_term=8))
