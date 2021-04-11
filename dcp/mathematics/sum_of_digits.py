def sum_of_digits(n):
    digit_sum = 0
    while n != 0:
        x = n % 10
        digit_sum = digit_sum + x
        n = n // 10

    return digit_sum


if __name__ == "__main__":
    n = 12644
    print(sum_of_digits(n=n))
