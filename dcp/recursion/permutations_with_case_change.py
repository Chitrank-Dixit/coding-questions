"""
Permutations with spaces
"""


def permutations_with_case_change(ip, op):
    if len(ip) == 0:
        print(op)
        return
    op1 = op
    op2 = op
    op1 += ip[0]
    op2 += ip[0].upper()
    ip = ip[1:]
    permutations_with_case_change(ip, op1)
    permutations_with_case_change(ip, op2)
    return


if __name__ == "__main__":
    ip = "abc"
    op = ""
    op += ip[0]
    ip = ip[1:]
    permutations_with_case_change(ip, op)
