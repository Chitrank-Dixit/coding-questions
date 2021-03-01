"""
write a function can_sum(target_sum, numbers) that takes in a target_sum and an array of numbers as arguments.

this function should return a boolean indicating whether ot not it is possible to generate the target_sum using numbers
from the array
"""


def can_sum(target_sum, numbers, memory={}):
    if target_sum in memory:
        return memory[target_sum]
    if target_sum == 0:
        return True

    if target_sum < 0:
        return False

    for num in numbers:
        remainder = target_sum - num
        if can_sum(remainder, numbers, memory):
            memory[target_sum] = True
            return True
    memory[target_sum] = False
    return False


if __name__ == "__main__":
    print(can_sum(7, [5, 3, 4, 7], {}))
    print(can_sum(300, [7, 14], {}))
