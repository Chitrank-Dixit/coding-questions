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


if __name__ == "__main__":
    s = Stack()
    s.push(12)
    s.push(23)
    s.push(34)
    s.pop()
    print(f"Top of Stack: {s.tos()}")
    s.traverse()
