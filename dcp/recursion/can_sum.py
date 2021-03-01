"""
write a function can_sum(target_sum, numbers) that takes in a target_sum and an array of numbers as arguments.

this function should return a boolean indicating whether ot not it is possible to generate the target_sum using numbers
from the array
"""


def can_sum(target_sum, numbers):
    if target_sum == 0:
        return True

    if target_sum < 0:
        return False

    for num in numbers:
        remainder = target_sum - num
        if can_sum(remainder, numbers):
            return True
    return False


if __name__ == "__main__":
    print(can_sum(7, [5, 3, 4, 7]))
