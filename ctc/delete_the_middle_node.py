"""
Delete the middle node: Implement an algorithm to delete a node in the middle (i.e. any node but the first and the
last node, not necessarily the exact middle) of singly linked list, given only access to that node
Example:
Input: the node c from the linked list a->b->c->d->e->f
result: nothing is returned, but the new linked list looks like a->b->d->e->f
"""


class LinkedList:
    def __init__(self, data, next_val):
        self.data = data
        self.next_val = next_val


def traverse(head):
    while head:
        print(head.data)
        head = head.next_val


def remove_node(head, index):
    temp = head
    count = 0
    while temp:
        if count == index - 1:
            temp1 = temp.next_val
            temp.next_val = temp1.next_val
            break

        temp = temp.next_val
        count += 1


if __name__ == "__main__":
    ll5 = LinkedList(5, None)
    ll4 = LinkedList(4, ll5)
    ll3 = LinkedList(3, ll4)
    ll2 = LinkedList(2, ll3)
    ll1 = LinkedList(1, ll2)
    traverse(ll1)
    mid = 5 // 2
    print("----------")
    remove_node(ll1, mid)
    traverse(ll1)
    print("------------------------")
    ll6 = LinkedList("f", None)
    ll5 = LinkedList("e", ll6)
    ll4 = LinkedList("d", ll5)
    ll3 = LinkedList("c", ll4)
    ll2 = LinkedList("b", ll3)
    ll1 = LinkedList("a", ll2)
    traverse(ll1)
    mid = (6 // 2) - 1
    print("----------")
    remove_node(ll1, mid)
    traverse(ll1)
