"""
Given an array, write a recursive function to check if the elements of array are in sequence

I/P: [2, 3, 4, 5, 6, 7], O/P: true
I/P: [2, 4, 5, 6, 7], O/P: false
"""


def is_sequence(arr, index):
    return (
        index == len(arr) - 1
        or (arr[index] == arr[index + 1] - 1)
        and is_sequence(arr, index + 1)
    )


if __name__ == "__main__":
    arr = [2, 3, 4, 5, 6, 7]
    index = 0
    print(is_sequence(arr=arr, index=index))

    arr = [2, 4, 5, 6, 7]
    index = 0
    print(is_sequence(arr=arr, index=index))
