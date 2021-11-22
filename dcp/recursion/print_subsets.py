"""
print subsets
"""


def subsets(ip, op):
    if len(ip) == 0:
        print(op, end=" ")
        return
    op1 = op
    op2 = op
    op2 += ip[0]
    ip = ip[1:]
    subsets(ip, op1)
    subsets(ip, op2)


if __name__ == "__main__":
    ip = "ab"
    op = ""
    print(subsets(ip, op))

    ip = "abcde"
    op = ""
    print(subsets(ip, op))
