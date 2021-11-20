"""
print subsets
"""


def subsets(ip, op):
    if len(ip) == 0:
        print(op, end=" ")
    op1 = op
    op2 = op
    op = op.replace(ip[0], "")
    ip = ip.replace(ip[0], "")
    subsets(ip, op1)
    subsets(ip, op2)


if __name__ == "__main__":
    ip = "ab"
    op = ""
    print(subsets(ip, op))
