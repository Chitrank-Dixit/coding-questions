"""
generate all balanced parenthesis
"""


def generate_all_balanced_parenthesis(open_var, close_var, op, v):
    if open_var == 0 and close_var == 0:
        v.append(op)
        return

    if open_var != 0:
        op1 = op
        op1 += "("
        generate_all_balanced_parenthesis(open_var - 1, close_var, op1, v)

    if close_var > open_var:
        op2 = op
        op2 += ")"
        generate_all_balanced_parenthesis(open_var, close_var - 1, op2, v)

    return


def main():
    n = 3
    close_var = n
    open_var = n
    op = ""
    v = []
    generate_all_balanced_parenthesis(open_var, close_var, op, v)
    return v


if __name__ == "__main__":
    print(main())
