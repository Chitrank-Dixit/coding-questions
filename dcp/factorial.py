def factorial_v1(num):
    fact = 1
    for i in range(num):
        fact *= i + 1
    return fact


if __name__ == "__main__":
    print(factorial_v1(5))
