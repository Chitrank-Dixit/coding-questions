"""
Write a function best_sum(target_sum, numbers) that takes in a target_sum and an array of numbers as arguments.

the function should return an array containing the shortest combination of numbers that add up to exactly the
target_sum.

If there is a tie for the shortest combination, you may return any one of the shortest.
"""


def best_sum(target_sum, numbers, memory={}):
    if target_sum in memory:
        return memory[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        remainder_combination = best_sum(remainder, numbers)
        if remainder_combination is not None:
            combination = remainder_combination + [num]
            if shortest_combination is None or len(
                remainder_combination
            ) < len(shortest_combination):
                shortest_combination = combination

    memory[target_sum] = shortest_combination
    return shortest_combination


if __name__ == "__main__":
    print(best_sum(7, [5, 3, 4, 7]))
    print(best_sum(8, [2, 3, 5]))
    print(best_sum(8, [1, 4, 5]))
    print(best_sum(100, [1, 2, 5, 25]))
