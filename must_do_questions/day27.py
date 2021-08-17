"""

"""
import math


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def parent(self, idx):
        return math.floor((idx - 1) / 2)

    def left_child(self, idx):
        return idx * 2 + 1

    def right_child(self, idx):
        return idx * 2 + 2

    def swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def compare(self, i, j):
        return self.heap[i] > self.heap[j]

    def push(self, value):
        self.heap.append(value)
        self.sift_up()
        return self.size()

    def sift_up(self):
        node_idx = self.size() - 1

        while node_idx > 0 and self.compare(node_idx, self.parent(node_idx)):
            self.swap(node_idx, self.parent(node_idx))
            node_idx = self.parent(node_idx)

    def pop(self):
        if self.size() > 1:
            self.swap(0, self.size() - 1)

        popped_value = self.heap.pop()
        self.sift_down()
        return popped_value

    def sift_down(self):
        node_idx = 0
        while (
            self.left_child(node_idx) < self.size()
            and self.compare(self.left_child(node_idx), node_idx)
        ) or (
            self.right_child(node_idx) < self.size()
            and self.compare(self.right_child(node_idx), node_idx)
        ):
            greater_node_idx = None
            if self.right_child(node_idx) < self.size() and self.compare(
                self.right_child(node_idx), self.left_child(node_idx)
            ):
                greater_node_idx = self.right_child(node_idx)
            else:
                greater_node_idx = self.left_child(node_idx)
            self.swap(greater_node_idx, node_idx)
            node_idx = greater_node_idx


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push(15)
    pq.push(12)
    pq.push(50)
    pq.push(7)
    pq.push(40)
    pq.push(22)

    while not pq.is_empty():
        print(pq.pop())
