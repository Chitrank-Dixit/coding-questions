"""
Cycle detection in Linked List
"""


class LinkedList:
    def __init__(self, data, next_val=None):
        self.data = data
        self.next_val = next_val


def traverse(head):
    count = 0
    while head:
        print(head.data)
        head = head.next_val
        count += 1
    return count


def find_cycle(head):
    current = head
    seen_nodes = set()
    while current not in seen_nodes:
        if current.next_val is None:
            return False
        seen_nodes.add(current)
        current = current.next_val
    return current


if __name__ == "__main__":
    ll8 = LinkedList(8)
    ll7 = LinkedList(7, next_val=ll8)
    ll6 = LinkedList(6, next_val=ll7)
    ll5 = LinkedList(5, next_val=ll6)
    ll4 = LinkedList(4, next_val=ll5)
    ll3 = LinkedList(3, next_val=ll4)
    ll2 = LinkedList(2, next_val=ll3)
    ll1 = LinkedList(1, next_val=ll2)
    ll8.next_val = ll3

    print(find_cycle(ll1).data)
