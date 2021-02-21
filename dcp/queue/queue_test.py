class Queue:
    def __init__(self):
        self.item = []

    def enqueue(self, element):
        self.item.append(element)

    def dequeue(self):
        self.item.pop(0)

    def current_queue_element(self):
        return self.item[0]

    def traverse(self):
        for element in self.item:
            print(element)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(12)
    q.enqueue(23)
    q.enqueue(34)
    q.dequeue()
    print(f"Element at front of the queue: {q.current_queue_element()}")
    q.traverse()
