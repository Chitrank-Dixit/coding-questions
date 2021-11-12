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


def delete_middle_element(stack, k, arr):
    if k == 0:
        arr.pop()
        i = len(arr) - 1
        while i >= 0:
            stack.push(arr[i])
            i -= 1
    elif k > 0:
        arr.append(stack.pop())
        delete_middle_element(stack, k - 1, arr)

    return stack


def solve(stack, k):
    if k == 1:
        stack.pop()
        return
    temp = stack.tos()
    stack.pop()
    solve(stack, k - 1)
    stack.push(temp)
    return


def middle_element(stack, size):
    if size == 0:
        return s

    k = 0
    if size % 2 == 0:
        k = (size // 2) + 1
    else:
        k = size // 2

    solve(s, k)
    return s


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(5)
    s.push(0)
    s.push(2)
    new_stack = delete_middle_element(
        stack=s, k=int((s.length_of_stack() / 2) + 1), arr=[]
    )
    print(new_stack.traverse())

    s = Stack()
    s.push(1)
    s.push(5)
    s.push(3)
    s.push(0)
    s.push(2)
    s.push(4)
    new_stack = delete_middle_element(
        stack=s, k=int((s.length_of_stack() / 2) + 1), arr=[]
    )
    print(new_stack.traverse())

    s = Stack()
    s.push(1)
    s.push(5)
    s.push(0)
    s.push(2)
    new_stack = middle_element(stack=s, size=s.length_of_stack())
    print(new_stack.traverse())

    s = Stack()
    s.push(1)
    s.push(5)
    s.push(3)
    s.push(0)
    s.push(2)
    s.push(4)
    new_stack = middle_element(stack=s, size=s.length_of_stack())
    print(new_stack.traverse())
