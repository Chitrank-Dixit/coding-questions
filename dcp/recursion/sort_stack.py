"""
sort an array using recursion
"""


class Stack:
    def __init__(self):
        self.item = []
        self.top = 0

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

    def length_of_stack(self):
        return len(self.item)

    def is_full(self):
        pass


def insert(stack, temp):
    if stack.length_of_stack() == 0 or (stack.tos() and stack.tos() <= temp):
        stack.push(temp)
        return
    val = stack.tos()
    stack.pop()
    insert(stack, temp)
    stack.push(val)
    return


def sort(stack):
    if stack.length_of_stack() == 1:
        return
    temp = stack.tos()
    stack.pop()
    sort(stack)
    insert(stack, temp)


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(5)
    s.push(0)
    s.push(2)
    print(sort(stack=s))
    print(s.traverse())

    s = Stack()
    s.push(1)
    s.push(5)
    s.push(3)
    s.push(0)
    s.push(2)
    s.push(4)
    print(sort(stack=s))
    print(s.traverse())
