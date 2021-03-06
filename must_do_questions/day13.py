"""
Given a string containing only parenthesis, determine if it is valid. The string is valid if all parentheses close.
"""


class Stack:
    def __init__(self):
        self.list = []

    def push(self, data):
        self.list.append(data)

    def pop(self):
        if self.tos():
            return self.list.pop()
        return None

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


def is_valid_string_v1(strings):
    if len(strings) == 0:
        return True

    validator = {"(": ")", "{": "}", "[": "]"}

    st = Stack()

    for char in strings:
        if char in validator:
            st.push(char)
        else:
            left_bracket = st.pop()
            correct_bracket = validator[left_bracket]
            if correct_bracket is not None and correct_bracket != char:
                return False
    return True


if __name__ == "__main__":
    strings = "{[()]}"
    print(is_valid_string(strings))

    strings = "{[()}"
    print(is_valid_string(strings))

    strings = "{[)]}"
    print(is_valid_string(strings))

    strings = "{[()]}"
    print(is_valid_string_v1(strings))

    strings = "{[()}"
    print(is_valid_string_v1(strings))

    strings = "{[)]}"
    print(is_valid_string_v1(strings))
