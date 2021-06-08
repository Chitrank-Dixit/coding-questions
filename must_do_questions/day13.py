"""
Given a string containing only parenthesis, determine if it is valid. The string is valid if all parentheses close.
"""


class Stack:
    def __init__(self):
        self.list = []

    def push(self, data):
        self.list.append(data)

    def pop(self):
        self.list.pop()

    def tos(self):
        if len(self.list) > 0:
            return self.list[-1]
        return None


def is_valid_string(strings):
    validator = {")": "(", "}": "{", "]": "["}

    st = Stack()
    for char in strings:
        if char in validator.values():
            st.push(char)
        elif char in validator and validator[char] == st.tos():
            st.pop()
        else:
            return False
    if not st.tos():
        return True
    return False


if __name__ == "__main__":
    strings = "{[()]}"
    print(is_valid_string(strings))

    strings = "{[()}"
    print(is_valid_string(strings))

    strings = "{[)]}"
    print(is_valid_string(strings))
