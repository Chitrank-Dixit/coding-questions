def factorial(n, memory={}):
    if n <= 1:
        return 1

    if n not in memory:
        memory[n] = n * factorial(n - 1)
    return memory[n]


if __name__ == "__main__":
    print(factorial(6, {}))
