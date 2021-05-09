"""
https://www.geeksforgeeks.org/rearrange-a-given-linked-list-in-place/
"""


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


def reorder(head):
    slow = head
    fast = slow.next_val

    # finding the middle to split the linked list in two halves
    while fast and fast.next_val:
        slow = slow.next_val
        fast = fast.next_val.next_val

    # splitting the linked list in two halves
    head1 = head
    head2 = slow.next_val
    slow.next_val = None

    head2 = reverse(head2)

    head = LinkedList(0, None)
    curr = head

    while head1 or head2:
        if head1:
            curr.next_val = head1
            curr = curr.next_val
            head1 = head1.next_val

        if head2:
            curr.next_val = head2
            curr = curr.next_val
            head2 = head2.next_val
    head = head.next_val
    return head


# def reorder(head):
#     current = head
#     prev = None
#     temp = None
#     while current:
#         if not temp:
#             temp = current
#         if current.next_val == prev:
#             temp1 = temp.next_val
#             temp.next_val = current
#             current.next_val = temp1
#             prev = temp1
#             current = prev
#             temp = temp1.next_val
#         current = current.next_val
#     head = prev
#     return head


if __name__ == "__main__":
    ll6 = LinkedList(6, None)
    ll5 = LinkedList(5, ll6)
    ll4 = LinkedList(4, ll5)
    ll3 = LinkedList(3, ll4)
    ll2 = LinkedList(2, ll3)
    ll1 = LinkedList(1, ll2)
    traverse(ll1)
    head = reorder(ll1)
    print("-------------")
    traverse(head)
