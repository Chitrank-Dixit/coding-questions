"""
Given a Linked list and numbers m and n return it back with only position m to n in reverse
"""


class LinkedList:
    def __init__(self, data, next_val):
        self.data = data
        self.next_val = next_val


def traverse(head):
    while head:
        print(head.data)
        head = head.next_val


def reverse(head, m, n):
    current = head
    start = head
    current_pos = 1
    while current_pos < m:
        start = current
        current = current.next_val
        current_pos += 1

    new_list = None
    tail = current

    while current_pos >= m and current_pos <= n:
        next = current.next_val
        current.next_val = new_list
        new_list = current
        current = next
        current_pos += 1

    start.next_val = new_list
    tail.next_val = current

    if m > 1:
        return head
    return new_list


if __name__ == "__main__":
    ll5 = LinkedList(5, None)
    ll4 = LinkedList(4, ll5)
    ll3 = LinkedList(3, ll4)
    ll2 = LinkedList(2, ll3)
    ll1 = LinkedList(1, ll2)
    traverse(ll1)
    m = 2
    n = 4
    head = reverse(ll1, m, n)
    print("----------")
    traverse(head)
