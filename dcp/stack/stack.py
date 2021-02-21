class Stack:
    def __init__(self):
        self.item = []

    def push(self, element):
        self.item.append(element)

    def pop(self):
        self.item.pop()

    def tos(self):
        return self.item[-1]

    def traverse(self):
        for element in self.item[::-1]:
            print(element)


if __name__ == "__main__":
    s = Stack()
    s.push(12)
    s.push(23)
    s.push(34)
    s.pop()
    print(f"Top of Stack: {s.tos()}")
    s.traverse()
