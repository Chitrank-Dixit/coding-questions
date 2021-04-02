class LinkedList:
    def __init__(self, data, next_node=None):
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, next_node):
        self._next_node = next_node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def front(self):
        return self.head.data

    def rear(self):
        return self.tail.data

    def insert(self, data):
        new_node = LinkedList(data=data)
        self.tail = new_node
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            inserted = False
            while temp:
                if temp.next_node is None and not inserted:
                    temp.next_node = new_node
                    inserted = True
                temp = temp.next_node

    def delete(self):
        temp = self.head.next_node
        self.head = temp


if __name__ == "__main__":
    q1 = Queue()

    q1.insert(1)
    q1.insert(2)
    q1.insert(3)

    print(q1.front())
    print(q1.rear())

    q1.delete()

    print(q1.front())
    print(q1.rear())
