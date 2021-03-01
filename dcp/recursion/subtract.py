def subtract_up(n):
    if n <= 1:
        return n
    return n - subtract_up(n - 1)


if __name__ == "__main__":
    print(subtract_up(5))
