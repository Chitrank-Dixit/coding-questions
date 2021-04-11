def fibonacci_v1(num):
    fibo1 = 0
    fibo2 = 1
    fibo3 = 0
    for i in range(num):
        fibo1 = fibo2
        fibo2 = fibo3
        fibo3 = fibo1 + fibo2

    return fibo3


if __name__ == "__main__":
    print(fibonacci_v1(10))
