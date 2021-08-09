"""
Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.
"""


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
        return str(self.data)


class LinkedListOperations:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def is_palindrome_singly(self):
        stack = list()
        temp = self.head
        while temp:
            stack.append(temp.data)
            temp = temp.next_node

        temp = self.head
        while temp:
            tos = stack.pop()
            if temp.data != tos:
                return False
            temp = temp.next_node
        return True

    def is_palindrome(self):
        first = self.head
        last = self.tail

        while first and last:
            if first.data != last.data:
                return False
            first = first.next_node
            last = last.prev_node
        return True


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
        return str(self.data)


if __name__ == "__main__":
    # ll4 = LinkedList("d", None)
    # ll3 = LinkedList("c", ll4)
    # ll2 = LinkedList("b", ll3)
    # ll1 = LinkedList("a", ll2)

    # or
    ll5 = LinkedList(1)
    ll4 = LinkedList(4)
    ll3 = LinkedList(3)
    ll2 = LinkedList(4)
    ll1 = LinkedList(1)
    ll5.next_node = None
    ll4.next_node = ll5
    ll3.next_node = ll4
    ll2.next_node = ll3
    ll1.next_node = ll2

    lo = LinkedListOperations(head=ll1)
    print(lo.is_palindrome_singly())

    ll5 = DoublyLinkedList(data=1)
    ll4 = DoublyLinkedList(data=4, next_node=ll5)
    ll3 = DoublyLinkedList(data=3, next_node=ll4)
    ll2 = DoublyLinkedList(data=4, next_node=ll3)
    ll1 = DoublyLinkedList(data=1, next_node=ll2)

    ll2.prev_node = ll1
    ll3.prev_node = ll2
    ll4.prev_node = ll3
    ll5.prev_node = ll4
    l1 = LinkedListOperations(head=ll1, tail=ll5)
    print(l1.is_palindrome())
