"""
print unique subsets
"""

s = set()


def subsets(ip, op):
    if len(ip) == 0:
        s.add(op)
        return

    op1 = op
    op2 = op
    op1 += ip[0]
    ip = ip[1:]
    subsets(ip, op1)
    subsets(ip, op2)


if __name__ == "__main__":
    ip = "ABC"
    op = ""
    subsets(ip, op)
    print(s)
