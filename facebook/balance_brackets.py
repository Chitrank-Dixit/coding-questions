"""
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.
"""


class Stack:
    def __init__(self):
        self.item = []
        self.top = -1

    def push(self, element):
        self.item.append(element)

    def pop(self):
        return self.item.pop()

    def tos(self):
        if len(self.item) > 0:
            self.top = self.item[-1]
        return self.top

    def traverse(self):
        for element in self.item[::-1]:
            print(element)

    def is_empty(self):
        if len(self.item) == 0:
            return True
        return False

    def is_full(self):
        pass


def is_balanced(string):
    stack = Stack()
    lookup = {"}": "{", "]": "[", ")": "("}
    for char in string:
        if char not in lookup:
            stack.push(char)
        else:
            stack.pop()
    if stack.is_empty():
        return True
    return False


if __name__ == "__main__":
    s = "{[()]}"
    print(is_balanced(s))

    s = "{[(]}"
    print(is_balanced(s))

    s = "{[()]"
    print(is_balanced(s))
