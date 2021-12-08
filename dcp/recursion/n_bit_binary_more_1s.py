"""
n bit binary more 1s
"""


def n_bit(one, zero, n, op):
    if n == 0:
        print(op, end=" ")
        return

    op1 = op
    op1 += "1"
    n_bit(one + 1, zero, n - 1, op1)

    if one > zero:
        op2 = op
        op2 += "0"
        n_bit(one, zero + 1, n - 1, op2)

    return


def main():
    n = 3
    one = 0
    zero = 0
    op = ""
    n_bit(one, zero, n, op)
    return


if __name__ == "__main__":
    print(main())
