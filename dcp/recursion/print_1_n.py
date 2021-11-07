"""
Write a program to print numbers from 1 to n
"""


def print_1_n(num):
    if num == 0:
        return 0
    print_1_n(num=num - 1)
    print(num, end=" ")


if __name__ == "__main__":
    num = 10
    print_1_n(num=num)
