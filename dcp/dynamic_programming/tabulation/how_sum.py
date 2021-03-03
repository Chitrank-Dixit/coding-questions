def how_sum(target_sum, numbers):
    table = [None for i in range(target_sum + 1)]
    table[0] = []

    for i in range(target_sum):
        if table[i] is not None:
            for num in numbers:
                if (i + num) < len(table):
                    if table[i + num] is None:
                        table[i + num] = []
                    table[i + num] = table[i] + [num]

    return table[-1]


if __name__ == "__main__":
    print(how_sum(7, [5, 3, 4, 7]))
