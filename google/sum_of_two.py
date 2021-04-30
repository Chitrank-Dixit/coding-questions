def sum_of_two(a, b, target):
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] + b[j] == target:
                return True
    return False


def sum_of_two_v1(a, b, target):
    needed_val = set()
    for i in range(len(a)):
        needed_val.add(a[i])

    for j in range(len(b)):
        if target - b[j] in needed_val:
            return True
    return False


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [10, 20, 30, 40]
    target = 42
    print(sum_of_two(a, b, target))

    a = [0, 0, -5, 30212]
    b = [-10, 40, -3, 9]
    target = -8
    print(sum_of_two(a, b, target))

    a = [1, 2, 3]
    b = [10, 20, 30, 40]
    target = 42
    print(sum_of_two_v1(a, b, target))

    a = [0, 0, -5, 30212]
    b = [-10, 40, -3, 9]
    target = -8
    print(sum_of_two_v1(a, b, target))
