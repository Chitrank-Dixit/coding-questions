"""
https://youtu.be/eaYX0Ee0Kcg
"""
import math


def k_closest_points(points, k):
    min_distances = dict()
    for point in points:
        min_distances[math.sqrt(point[0] ** 2 + point[1] ** 2)] = point

    min_distance_vals = sorted(min_distances)
    for vals in min_distance_vals[:k]:
        print(min_distances[vals])
    return None


if __name__ == "__main__":
    points = [(-2, 4), (0, -2), (-1, 0), (3, -5), (-2, -3), (3, 2)]
    k = 3
    print(k_closest_points(points, k))
