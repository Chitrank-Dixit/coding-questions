"""
Given an array of integers representing an elevation, map where the width of each bar is 1, return how much rain water
can be trapped
"""


def trapped_rain_water(arr):
    """
    missing some test cases not completely correct
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return 0
    fill = 0
    total_fill = 0
    left = 0
    right = 1
    while right < len(arr):
        if arr[left] > arr[right]:
            current = arr[left] - arr[right]
            if current > 0:
                fill += current
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


def trapped_rain_water_v1(arr):
    total_water = 0
    for p in range(len(arr)):
        left_p = p
        right_p = p
        max_left = 0
        max_right = 0
        while left_p >= 0:
            max_left = max(max_left, arr[left_p])
            left_p -= 1

        while right_p < len(arr):
            max_right = max(max_right, arr[right_p])
            right_p += 1

        current_water = min(max_left, max_right) - arr[p]

        if current_water >= 0:
            total_water += current_water
    return total_water


def trapped_rain_water_v2(arr):
    left = 0
    right = len(arr) - 1
    left_max = 0
    right_max = 0
    total = 0

    while left < right:
        if arr[left] <= arr[right]:
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                total += left_max - arr[left]

            left += 1
        else:
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                total += right_max - arr[right]

            right -= 1

    return total


if __name__ == "__main__":
    arr = []
    print(trapped_rain_water(arr))

    arr = [2, 0, 2]
    print(trapped_rain_water(arr))

    arr = [2, 0, 2, 1, 2]
    print(trapped_rain_water(arr))

    arr = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
    print(trapped_rain_water(arr))

    arr = [5, 0, 3, 0, 0, 0, 2, 3, 4, 2, 1]
    print(trapped_rain_water(arr))

    print("------------------------------------------")

    arr = []
    print(trapped_rain_water_v1(arr))

    arr = [2, 0, 2]
    print(trapped_rain_water_v1(arr))

    arr = [2, 0, 2, 1, 2]
    print(trapped_rain_water_v1(arr))

    arr = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
    print(trapped_rain_water_v1(arr))

    arr = [5, 0, 3, 0, 0, 0, 2, 3, 4, 2, 1]
    print(trapped_rain_water_v1(arr))

    print("-------------------------------------------")

    arr = []
    print(trapped_rain_water_v2(arr))

    arr = [2, 0, 2]
    print(trapped_rain_water_v2(arr))

    arr = [2, 0, 2, 1, 2]
    print(trapped_rain_water_v2(arr))

    arr = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
    print(trapped_rain_water_v2(arr))

    arr = [5, 0, 3, 0, 0, 0, 2, 3, 4, 2, 1]
    print(trapped_rain_water_v2(arr))
