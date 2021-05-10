"""
Write code to remove duplicates from an unsorted linked list
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


def remove_duplicates(head):
    ll_set = set()
    temp = head
    prev = None
    while temp:
        if temp.data not in ll_set:
            ll_set.add(temp.data)

        else:
            next_node = temp.next_val
            temp.next_val = None
            prev.next_val = next_node
            temp = prev
        prev = temp
        temp = temp.next_val

    return head


if __name__ == "__main__":
    ll6 = LinkedList(4, None)
    ll5 = LinkedList(5, ll6)
    ll4 = LinkedList(4, ll5)
    ll3 = LinkedList(1, ll4)
    ll2 = LinkedList(2, ll3)
    ll1 = LinkedList(1, ll2)
    traverse(ll1)
    head = remove_duplicates(ll1)
    print("-------------")
    traverse(head)
    print("----Next----")
    ll6 = LinkedList(5, None)
    ll5 = LinkedList(5, ll6)
    ll4 = LinkedList(5, ll5)
    ll3 = LinkedList(5, ll4)
    ll2 = LinkedList(5, ll3)
    ll1 = LinkedList(1, ll2)
    traverse(ll1)
    head = remove_duplicates(ll1)
    print("-------------")
    traverse(head)
