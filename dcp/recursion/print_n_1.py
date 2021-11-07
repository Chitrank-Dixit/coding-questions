"""
Write a program to print numbers from n to 1
"""


def print_n_1(num):
    if num == 0:
        return 0
    print(num, end=" ")
    print_n_1(num=num - 1)


if __name__ == "__main__":
    num = 10
    print_n_1(num=num)
