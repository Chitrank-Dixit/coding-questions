def how_sum(target_sum, numbers):
    table = [None for i in range(target_sum + 1)]
    table[0] = []

    for i in range(target_sum):
        if table[i] is not None:
            for num in numbers:
                if (i + num) < len(table):
                    if table[i + num] is None:
                        table[i + num] = []
                    combination = table[i] + [num]
                    if table[i + num] == [] or len(table[i + num]) > len(
                        combination
                    ):
                        table[i + num] = combination

    return table[-1]


if __name__ == "__main__":
    print(how_sum(8, [2, 3, 5]))
    print(how_sum(7, [5, 3, 4, 7]))
    print(how_sum(100, [1, 2, 5, 25]))
