"""
with arr = [1, 2, 3, 4, 5, 6]
return
[1, 3, 6, 10, 15, 21]
"""


def cumulative_sum(arr, index):
    if index == (len(arr)):
        return arr
    arr[index] = arr[index] + arr[index - 1]
    return cumulative_sum(arr, index + 1)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    index = 1
    print(cumulative_sum(arr, index))
