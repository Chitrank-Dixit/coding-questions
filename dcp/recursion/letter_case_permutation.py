"""
letter case permutation
"""


def letter_case_permutation(ip, op, v):
    if len(ip) == 0:
        v.append(op)
        return

    if ip[0].isalpha():
        op1 = op
        op2 = op
        op1 += ip[0].lower()
        op2 += ip[0].upper()
        ip = ip[1:]
        letter_case_permutation(ip, op1, v)
        letter_case_permutation(ip, op2, v)
    else:
        op1 = op
        op1 += ip[0]
        ip = ip[1:]
        letter_case_permutation(ip, op1, v)
    return


def main():
    ip = "a1B2"
    op = ""
    v = []
    letter_case_permutation(ip, op, v)
    return v


if __name__ == "__main__":
    print(main())
