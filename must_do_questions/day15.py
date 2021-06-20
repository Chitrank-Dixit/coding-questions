"""
Implement the class Queue using stacks. The queue methods you need to implement are enqueue, dequeue, peek and empty.
"""


class Queue:
    def __init__(self):
        self.in_ob = []
        self.out_ob = []

    def enqueue(self, element):
        self.in_ob.append(element)

    def dequeue(self):
        if len(self.out_ob) == 0:
            while len(self.in_ob) > 0:
                self.out_ob.append(self.in_ob.pop())
        return self.out_ob.pop()

    def peek(self):
        if len(self.out_ob) == 0:
            while len(self.in_ob) > 0:
                self.out_ob.append(self.in_ob.pop())
        return self.out_ob[len(self.out_ob) - 1]

    def empty(self):
        return len(self.in_ob) == 0 and len(self.out_ob) == 0


if __name__ == "__main__":
    q = Queue()
    q.enqueue(12)
    q.enqueue(23)
    q.enqueue(34)
    q.dequeue()
    print(f"Element at front of the queue: {q.peek()}")
    print(f"Queue empty or not: {q.empty()}")
