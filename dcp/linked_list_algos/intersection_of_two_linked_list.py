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


def intersection(head1, head2):
    lookup = dict()
    temp1 = head1

    while temp1:
        lookup[temp1.data] = temp1.next_val
        temp1 = temp1.next_val

    temp2 = head2

    intersection_point = None
    while temp2:
        if temp2.data in lookup and lookup[temp2.data] == temp2.next_val:
            intersection_point = temp2
            break
        temp2 = temp2.next_val
    return intersection_point.data, intersection_point.next_val


if __name__ == "__main__":
    ll6 = LinkedList(6, None)
    ll5 = LinkedList(5, ll6)
    ll4 = LinkedList(4, ll5)
    ll3 = LinkedList(3, ll4)
    ll2 = LinkedList(2, ll3)
    ll1 = LinkedList(1, ll2)
    traverse(ll1)

    lll3 = LinkedList(2, ll4)
    lll2 = LinkedList(1, lll3)
    lll1 = LinkedList(3, lll2)

    print("-------------")
    traverse(lll1)

    print(intersection(ll1, lll1))
