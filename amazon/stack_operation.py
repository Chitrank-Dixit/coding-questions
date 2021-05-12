"""
This problem was asked by Amazon.

Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack,
then it should throw an error or return null. max(), which returns the maximum value in the stack currently.
If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
"""


class Stack:
    def __init__(self):
        self.item = []
        self.top = -1
        self.max_elements = []

    def push(self, element):
        max_ele = self.get_max_element()
        if not max_ele or element > max_ele:
            self.max_elements.append(element)
        self.item.append(element)

    def pop(self):
        max_ele = self.get_max_element()
        if self.tos() == max_ele:
            self.max_elements.pop()
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

    def get_max_element(self):
        if len(self.max_elements) == 0:
            return None
        return self.max_elements[-1]


if __name__ == "__main__":
    s = Stack()
    s.push(12)
    print("Max element", s.get_max_element())
    s.push(23)
    s.push(34)
    print("Max element", s.get_max_element())
    s.pop()
    print("Max element", s.get_max_element())

    print(f"Top of Stack: {s.tos()}")
    s.traverse()
