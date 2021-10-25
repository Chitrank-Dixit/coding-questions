"""
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater
than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than
x (see below). The partition element x can appear anywhere in the "right partition", it does not need to appear between
the left and right partitions.
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
        return f"{self.data}"


class LinkedListOperations:
    def __init__(self, head=None):
        self.head = head

    def traverse(self):
        temp = self.head
        while temp:
            print(temp)
            temp = temp.next_node

    def add_at_first(self, val):
        to_add = LinkedList(val)
        to_add.next_node = self.head
        self.head = to_add

    def add_at_last(self, val):
        temp = self.head
        while temp:
            if temp.next_node is None:
                break
            temp = temp.next_node
        add_last = LinkedList(val)
        temp.next_node = add_last

    def add_at_index(self, val, index):
        temp = self.head
        count = 0
        while temp:
            if count == index - 1:
                temp1 = temp.next_node
                add_index = LinkedList(val)
                temp.next_node = add_index
                add_index.next_node = temp1
                break

            temp = temp.next_node
            count += 1

    def delete_at_first(self):
        if self.head.next_node is not None:
            self.head = self.head.next_node

    def delete_at_last(self):
        temp = self.head
        while temp:
            if temp.next_node.next_node is None:
                break
            temp = temp.next_node
        temp.next_node = None

    def delete_at_index(self, index):
        temp = self.head
        count = 0
        while temp:
            if count == index - 1:
                temp1 = temp.next_node
                temp.next_node = temp1.next_node
                break

            temp = temp.next_node
            count += 1


if __name__ == "__main__":
    ll7 = LinkedList(1)
    ll6 = LinkedList(2)
    ll5 = LinkedList(10)
    ll4 = LinkedList(5)
    ll3 = LinkedList(8)
    ll2 = LinkedList(5)
    ll1 = LinkedList(3)
    ll7.next_node = None
    ll6.next_node = ll7
    ll5.next_node = ll6
    ll4.next_node = ll5
    ll3.next_node = ll4
    ll2.next_node = ll3
    ll1.next_node = ll2

    lo = LinkedListOperations(head=ll1)
    lo.traverse()
