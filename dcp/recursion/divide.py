def divide_up(n):
    if n <= 1.0:
        return n
    return n / divide_up(n - 1.0)


if __name__ == "__main__":
    print(divide_up(5.0))
