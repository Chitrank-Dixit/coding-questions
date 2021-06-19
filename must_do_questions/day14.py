"""
Given a string containing only containing round brackets '(' and ')' and lowercase characters,remove the least amount
of brackets so the string is valid.
A string is considered valid if it is empty or if there are brackets, they all close.
"""


class Stack:
    def __init__(self):
        self.list = []

    def push(self, data):
        self.list.append(data)

    def pop(self):
        if self.tos() is not None:
            return self.list.pop()
        return None

    def tos(self):
        if len(self.list) > 0:
            return self.list[-1]
        return None


def validated_string(strings):
    stack_accepted = ["(", ")"]
    stack = Stack()
    invalid_index = []
    for index, char in enumerate(strings):
        if char == stack_accepted[0]:
            stack.push(char)
        elif char == stack_accepted[1]:
            if stack.tos() == stack_accepted[0]:
                stack.pop()
            elif not stack.tos() or stack.tos() != stack_accepted[0]:
                invalid_index.append(index)

    new_string = ""
    for index, char in enumerate(strings):
        if char == stack.tos():
            stack.pop()
        elif index not in invalid_index:
            new_string += char
    return new_string


def validated_string_v1(strings):
    res = [string for string in strings]
    stack = Stack()

    for i in range(len(res)):
        if res[i] == "(":
            stack.push(i)
        elif res[i] == ")" and stack.tos():
            stack.pop()
        elif res[i] == ")":
            res[i] = ""

    while stack.tos() is not None:
        curr_index = stack.pop()
        res[curr_index] = ""

    return "".join(res)


if __name__ == "__main__":
    strings = "This is test () string"
    print(validated_string(strings))

    strings = "This is test () string"
    print(validated_string(strings))

    strings = "This is test ) string"
    print(validated_string(strings))

    strings = "))(("
    print(validated_string(strings))

    strings = "a)bc(d)"
    print(validated_string(strings))

    strings = "(ab(c)d"
    print(validated_string(strings))

    print("------------------------")

    strings = "This is test () string"
    print(validated_string_v1(strings))

    strings = "This is test () string"
    print(validated_string_v1(strings))

    strings = "This is test ) string"
    print(validated_string_v1(strings))

    strings = "))(("
    print(validated_string_v1(strings))

    strings = "a)bc(d)"
    print(validated_string_v1(strings))

    strings = "(ab(c)d"
    print(validated_string_v1(strings))
