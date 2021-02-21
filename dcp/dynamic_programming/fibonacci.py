# dynamic programming with memoization


def fibonacci(num, memory={}):
    if num == 0:
        return 0

    if num == 1:
        return 1

    if num not in memory:
        memory[num] = fibonacci(num - 1) + fibonacci(num - 2)
    return memory[num]


if __name__ == "__main__":
    print(fibonacci(10))
