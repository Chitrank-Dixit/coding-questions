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

    def __str__(self):
        return self.data


def traverse(head):
    while head:
        print(head)
        head = head.next_node


if __name__ == "__main__":
    # ll4 = LinkedList("d", None)
    # ll3 = LinkedList("c", ll4)
    # ll2 = LinkedList("b", ll3)
    # ll1 = LinkedList("a", ll2)

    # or

    ll4 = LinkedList("d")
    ll3 = LinkedList("c")
    ll2 = LinkedList("b")
    ll1 = LinkedList("a")
    ll4.next_node = ll1
    ll3.next_node = ll4
    ll2.next_node = ll3
    ll1.next_node = ll2

    traverse(ll1)
