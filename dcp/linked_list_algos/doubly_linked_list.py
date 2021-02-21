class DoublyLinkedList:
    def __init__(self, data, prev_node=None, next_node=None):
        self._data = data
        self._next_node = next_node
        self._prev_node = prev_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def prev_node(self):
        return self._prev_node

    @prev_node.setter
    def prev_node(self, prev_node):
        self._prev_node = prev_node

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, next_node):
        self._next_node = next_node

    def __str__(self):
        return self.data


def traverse_from_head(head):
    while head:
        print(head)
        head = head.next_node


def traverse_from_tail(tail):
    while tail:
        print(tail)
        tail = tail.prev_node


if __name__ == "__main__":
    ll4 = DoublyLinkedList(data="d", next_node=None)
    ll3 = DoublyLinkedList(data="c", next_node=ll4)
    ll2 = DoublyLinkedList(data="b", next_node=ll3)
    ll1 = DoublyLinkedList(data="a", next_node=ll2)

    ll2.prev_node = ll1
    ll3.prev_node = ll2
    ll4.prev_node = ll3

    traverse_from_head(ll1)

    traverse_from_tail(ll4)
