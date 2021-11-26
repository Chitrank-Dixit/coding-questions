"""
Permutations with spaces
"""


def permutations_with_spaces(ip, op):
    if len(ip) == 0:
        print(op)
        return
    op1 = op
    op2 = op
    op1 += " "
    op1 += ip[0]
    op2 += ip[0]
    ip = ip[1:]
    permutations_with_spaces(ip, op1)
    permutations_with_spaces(ip, op2)
    return


if __name__ == "__main__":
    ip = "ABC"
    op = ""
    op += ip[0]
    ip = ip[1:]
    permutations_with_spaces(ip, op)
