class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, element):
        self.items.append(element)

    def dequeue(self):
        self.items.pop(0)

    def current_queue_element(self):
        return self.items[0]

    def traverse(self):
        for element in self.items:
            print(element)

    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False


if __name__ == "__main__":
    q = Queue()
    q.enqueue(12)
    q.enqueue(23)
    q.enqueue(34)
    q.dequeue()
    print(f"Element at front of the queue: {q.current_queue_element()}")
    q.traverse()
