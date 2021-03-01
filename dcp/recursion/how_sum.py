"""
write a function how_sum(target_sum, numbers) that takes in a target_sum and an array of numbers as arguments.

the function should return an array containing any combination of elements that add up to exactly the targetSum. If there
is no combination that adds up to the targetSum, then return null.
"""


def how_sum(target_sum, numbers):
    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    for num in numbers:
        remainder = target_sum - num
        remainder_result = how_sum(remainder, numbers)
        if remainder_result is not None:
            remainder_result.append(num)
            return remainder_result
    return None


if __name__ == "__main__":
    print(how_sum(7, [5, 3, 4, 7]))
    print(how_sum(8, [2, 3, 5]))
