def max_min(arr):
    minimum = arr[0]
    maximum = arr[0]

    for i in range(len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
        if arr[i] > maximum:
            maximum = arr[i]
    return maximum, minimum


def maximum_element(arr, i):
    if i == len(arr) - 1:
        return arr[i]
    return max(arr[i], maximum_element(arr, i+1))


def minimum_element(arr, i):
    if i == len(arr) - 1:
        return arr[i]
    return min(arr[i], minimum_element(arr, i + 1))


def rec(arr):
    return maximum_element(arr, i=0), minimum_element(arr, i=0)


if __name__ == "__main__":
    arr = [9, 2, 8, 3,11, 8, 4, 1, 7, 5, 6]
    print(max_min(arr))

    print(rec(arr))