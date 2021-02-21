def no_of_digits(n):
    digits = 0
    while n != 0:
        digits += 1
        n = n // 10
    return digits


if __name__ == "__main__":
    n = 12644
    print(no_of_digits(n=n))
