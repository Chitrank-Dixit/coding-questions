"""
You are given an array of positive integers where each integer represents the height of a vertical line on a chart.
Find two lines which together with the x-axis forms a container that would hold the greatest amount of water. Return
the area of water it would hold.
"""


def greatest_area(arr):
    if len(arr) <= 1:
        return []
    max_area = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                min_val = 0
                breadth = 0
                if arr[i] > arr[j]:
                    min_val = arr[j]
                else:
                    min_val = arr[i]

                if i > j:
                    breadth = i - j
                else:
                    breadth = j - i

                area = min_val * breadth

                if area > max_area:
                    max_area = area
    return max_area


if __name__ == "__main__":
    print(greatest_area([]))

    print(greatest_area([7]))

    print(greatest_area([6, 9, 3, 4, 5, 8]))
