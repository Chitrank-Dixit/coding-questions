"""
Given an integer, write recursive function to return the sum of its digits
I/P: 123456, O/P: 21
"""


def digit_sum(num):
    if num == 0:
        return 0
    return (num % 10) + digit_sum(num=num // 10)


if __name__ == "__main__":
    num = 123456
    print(digit_sum(num))
