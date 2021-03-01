def sum_up(n):
    if n <= 1:
        return n
    return n + sum_up(n - 1)


if __name__ == "__main__":
    print(sum_up(5))
