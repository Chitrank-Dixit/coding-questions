from stack import Stack


def valid_parenthesis(str):
    s = Stack()
    for i in range(len(str)):
        ch = str[i]
        if ch == "(" or ch == "[" or ch == "{":
            s.push(ch)
        else:
            if s.is_empty():
                return False
            p = s.tos()

            # check for all the false conditions
            if ch == ")" and p != "(":
                return False
            elif ch == "]" and p != "[":
                return False
            elif ch == "}" and p != "{":
                return False
            else:
                s.pop()
    # return true if the stack is empty otherwise false
    return s.is_empty()


if __name__ == "__main__":
    str = "["
    print(valid_parenthesis(str))

    str = "[]"
    print(valid_parenthesis(str))

    str = "{}"
    print(valid_parenthesis(str))

    str = "()"
    print(valid_parenthesis(str))

    str = "[({})]"
    print(valid_parenthesis(str))

    str = "[(])]"
    print(valid_parenthesis(str))

    str = "{[ [] {} ]}"
    print(valid_parenthesis(str))
