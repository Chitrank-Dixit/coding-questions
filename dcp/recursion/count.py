def count_up(n, s):
    if n <= 1:
        return s
    s += count_up(n - 1, s)
    return s


if __name__ == "__main__":
    print(count_up(5, 1))
