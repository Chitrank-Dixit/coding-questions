def multi_up(n):
    if n <= 1:
        return n
    return n * multi_up(n - 1)


if __name__ == "__main__":
    print(multi_up(5))
