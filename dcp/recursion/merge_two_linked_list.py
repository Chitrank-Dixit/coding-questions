"""
reverse a linked list
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
        return self.data


class LinkedListOperations:
    def __init__(self, head=None):
        self.head = head

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data)
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


def sorted_merge(a, b):
    if not a:
        return b
    if not b:
        return a

    if a.data < b.data:
        a.next_node = sorted_merge(a.next_node, b)
        return a
    else:
        b.next_node = sorted_merge(a, b.next_node)
        return b


if __name__ == "__main__":
    ll4 = LinkedList(9)
    ll3 = LinkedList(8)
    ll2 = LinkedList(5)
    ll1 = LinkedList(3)
    ll4.next_node = None
    ll3.next_node = ll4
    ll2.next_node = ll3
    ll1.next_node = ll2

    lll4 = LinkedList(6)
    lll3 = LinkedList(4)
    lll2 = LinkedList(2)
    lll1 = LinkedList(1)
    lll4.next_node = None
    lll3.next_node = lll4
    lll2.next_node = lll3
    lll1.next_node = lll2

    print("---------------------------")
    merged_head = sorted_merge(ll1, lll1)
    lo = LinkedListOperations(head=merged_head)
    lo.traverse()
