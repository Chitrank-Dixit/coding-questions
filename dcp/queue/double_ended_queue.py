class DoubleEndedQueue:
    def __init__(self):
        self.item = []

    def enqueue_rear(self, element):
        self.item.append(element)

    def dequeue_front(self):
        self.item.pop(0)

    def enqueue_front(self, element):
        self.item.insert(0, element)

    def dequeue_rear(self):
        self.item.pop(len(self.item) - 1)

    def current_queue_element(self):
        return self.item[0]

    def traverse(self):
        for element in self.item:
            print(element)


if __name__ == "__main__":
    q = DoubleEndedQueue()
    q.enqueue_rear(12)
    q.enqueue_rear(23)
    q.enqueue_rear(34)
    q.enqueue_front(67)
    q.dequeue_rear()
    q.traverse()
    print(f"Element at front of the queue: {q.current_queue_element()}")

    q.dequeue_front()
    q.traverse()
