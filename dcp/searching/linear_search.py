def search(arr, search_term):
    index = None
    for count, element in enumerate(arr):
        if search_term == element:
            index = count
    if not index:
        return -1
    return index


def search_v1(arr, search_term):
    left = 0
    length = len(arr)
    position = None
    right = length - 1

    # run loop from 0 to right
    for left in range(0, right, 1):
        # If search_element is found
        # with left variable
        if arr[left] == search_term:
            position = left
            break

        # If search_element is found
        # with right variable
        if arr[right] == search_term:
            position = right
            break

        left += 1
        right -= 1

    # If element not found
    if not position:
        return -1
    return position


if __name__ == "__main__":
    arr = [1, 3, 5, 2, 6, 4, 7, 9, 8]
    search_term = 4
    print(search(arr=arr, search_term=search_term))

    arr = [1, 3, 5, 2, 6, 4, 7, 9, 8]
    search_term = 100
    print(search(arr=arr, search_term=search_term))

    arr = [1, 3, 5, 2, 6, 4, 7, 9, 8]
    search_term = 4
    print(search_v1(arr=arr, search_term=search_term))

    arr = [1, 3, 5, 2, 6, 4, 7, 9, 8]
    search_term = 100
    print(search_v1(arr=arr, search_term=search_term))
