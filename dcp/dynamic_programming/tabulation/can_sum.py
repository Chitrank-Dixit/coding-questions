def can_sum(target_sum, numbers):
    table = [False for i in range(target_sum + 1)]
    table[0] = True

    for i in range(target_sum):
        if table[i] is True:
            for num in numbers:
                if (i + num) < len(table):
                    table[i + num] = True

    return table[-1]


if __name__ == "__main__":
    print(can_sum(7, [5, 3, 4, 7]))
