"""
delete middle element from stack
"""


class Stack:
    def __init__(self):
        self.item = []
        self.top = 0

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

    def length_of_stack(self):
        return len(self.item)

    def is_full(self):
        pass


def reverse_stack_v0(stack, k, arr):
    if k == 0:
        # arr.pop()
        i = 0
        while i < len(arr):
            stack.push(arr[i])
            i += 1
    elif k > 0:
        arr.append(stack.pop())
        reverse_stack_v0(stack, k - 1, arr)

    return stack


def insert(stack, temp):
    if stack.length_of_stack() == 0:
        stack.push(temp)
        return
    val = stack.tos()
    stack.pop()
    insert(stack, temp)
    stack.push(val)
    return


def reverse(stack):
    if stack.length_of_stack() == 0:
        return
    temp = stack.tos()
    stack.pop()
    reverse(stack)
    insert(stack, temp)
    return stack


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(5)
    s.push(0)
    s.push(2)
    print(s.traverse())
    new_stack = reverse_stack_v0(stack=s, k=s.length_of_stack(), arr=[])
    print(new_stack.traverse())

    s = Stack()
    s.push(1)
    s.push(5)
    s.push(3)
    s.push(0)
    s.push(2)
    s.push(4)
    print(s.traverse())
    new_stack = reverse_stack_v0(stack=s, k=s.length_of_stack(), arr=[])
    print(new_stack.traverse())

    print("-------------------------------------------------")

    s = Stack()
    s.push(1)
    s.push(5)
    s.push(0)
    s.push(2)
    print(s.traverse())
    new_stack = reverse(stack=s)
    print(new_stack.traverse())

    s = Stack()
    s.push(1)
    s.push(5)
    s.push(3)
    s.push(0)
    s.push(2)
    s.push(4)
    print(s.traverse())
    new_stack = reverse(stack=s)
    print(new_stack.traverse())
