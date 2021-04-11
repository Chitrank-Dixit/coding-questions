class LinkedList:
    def __init__(self, data, next_val):
        self.data = data
        self.next_val = next_val


def traverse(head):
    while head:
        print(head.data)
        head = head.next_val


def reverse(head):
    current = head
    prev = None
    while current:
        next_node = current.next_val
        current.next_val = prev
        prev = current
        current = next_node
    head = prev
    return head


if __name__ == "__main__":
    ll4 = LinkedList("d", None)
    ll3 = LinkedList("c", ll4)
    ll2 = LinkedList("b", ll3)
    ll1 = LinkedList("a", ll2)
    traverse(ll1)
    head = reverse(ll1)
    traverse(head)
