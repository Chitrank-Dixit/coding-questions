"""
sort an array using recursion
"""


def insert(arr, temp):
    if len(arr) == 0 or arr[len(arr) - 1] <= temp:
        arr.append(temp)
        return
    val = arr[len(arr) - 1]
    arr.pop(len(arr) - 1)
    insert(arr, temp)
    arr.append(val)
    return


def sort(arr):
    if len(arr) == 1:
        return
    temp = arr[len(arr) - 1]
    arr.pop(len(arr) - 1)
    sort(arr)
    insert(arr, temp)


if __name__ == "__main__":
    arr = [1, 5, 0, 2]
    print(sort(arr=arr))
    print(arr)

    arr = [1, 5, 3, 0, 2, 4]
    print(sort(arr=arr))
    print(arr)
