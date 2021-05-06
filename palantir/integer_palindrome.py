"""
Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888.
678 is not a palindrome. Do not convert the integer into a string.
"""


class Stack:
    def __init__(self):
        self.item = []
        self.top = -1

    def push(self, element):
        self.item.append(element)

    def pop(self):
        self.item.pop()

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


def integer_palindrome(num):
    digits = 0
    number = num
    while number != 0:
        digits += 1
        number = number // 10
    mid = digits // 2
    number = num
    count = 0
    st = Stack()
    while number != 0:
        if digits % 2 == 0:
            if count < mid:
                st.push(number % 10)
            elif count >= mid:
                if number % 10 == st.tos():
                    st.pop()
        else:
            if count < mid:
                st.push(number % 10)
            elif count > mid:
                if number % 10 == st.tos():
                    st.pop()
        count += 1
        number = number // 10

    if st.item is []:
        return True
    return False


if __name__ == "__main__":
    num = 121
    print(integer_palindrome(num))

    num = 1469641
    print(integer_palindrome(num))

    num = 1212
    print(integer_palindrome(num))

    num = 1221
    print(integer_palindrome(num))

    num = 12112
    print(integer_palindrome(num))
