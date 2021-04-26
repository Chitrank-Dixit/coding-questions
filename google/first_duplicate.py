def first_duplicate(arr):
    element_set = set()

    first_duplicate_num = None
    for element in arr:
        if element not in element_set:
            element_set.add(element)
        else:
            first_duplicate_num = element
            break

    return first_duplicate_num


def first_duplicate_v1(arr):
    for i in range(len(arr)):
        if arr[abs(arr[i]) - 1] < 0:
            return abs(arr[i])
        else:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
    return None


if __name__ == "__main__":
    arr = [-2, -1, -3, 5, -3, 2]
    print(first_duplicate(arr))

    arr = [2, -1, -3, 5, -3, 2]
    print(first_duplicate(arr))

    arr = [1, 2, 1, 2, 3, 3]
    print(first_duplicate(arr))

    arr = [1, 2, 3, 4, 5]
    print(first_duplicate(arr))

    print("-------------")

    arr = [-2, -1, -3, 5, -3, 2]
    print(first_duplicate(arr))

    # Failing at this input
    arr = [2, -1, -3, 5, -3, 2]
    print(first_duplicate_v1(arr))

    arr = [1, 2, 1, 2, 3, 3]
    print(first_duplicate_v1(arr))

    arr = [1, 2, 3, 4, 5]
    print(first_duplicate_v1(arr))
