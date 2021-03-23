"""
Given an array of integers representing an elevation, map where the width of each bar is 1, return how much rain water
can be trapped
"""


def trapped_rain_water(arr):
    if len(arr) < 2:
        return 0
    fill = 0
    total_fill = 0
    left = 0
    right = 1
    while right < len(arr):
        if arr[left] > arr[right]:
            fill += arr[left] - arr[right]
        elif arr[left] <= arr[right]:
            total_fill += fill
            fill = 0
            left = right
        right += 1

    total_fill += fill

    if arr[left] > arr[right - 1]:
        for i in range(len(arr[left + 1 : right])):
            total_fill -= 1

    return total_fill


if __name__ == "__main__":
    arr = []
    print(trapped_rain_water(arr))

    arr = [2, 0, 2]
    print(trapped_rain_water(arr))

    arr = [2, 0, 2, 1, 2]
    print(trapped_rain_water(arr))

    arr = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
    print(trapped_rain_water(arr))
