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


def floyds_tortoise_hare(head):
    current = head
    temp = head
    tortoise_node = current
    hare_node = current
    req_node = None
    same_node = None
    while (same_node is temp) or (same_node is None) and current:
        if tortoise_node == hare_node:
            same_node = tortoise_node
            if same_node is not temp:
                break

        tortoise_node = tortoise_node.next_val
        hare_node = hare_node.next_val.next_val

        current = current.next_val
    if same_node:
        current = head
        while current and same_node:
            current = current.next_val
            same_node = same_node.next_val
            if current == same_node:
                req_node = current
                break
        return req_node
    return False


def find_cycle(head):
    hare = head
    tortoise = head

    while True:
        hare = hare.next_val
        tortoise = tortoise.next_val
        if hare is None or hare.next_val is None:
            return False
        else:
            hare = hare.next_val

        if tortoise == hare:
            break

    p1 = head
    p2 = tortoise

    while p1 != p2:
        p1 = p1.next_val
        p2 = p2.next_val

    return p1


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

    req_node = floyds_tortoise_hare(ll1)
    if req_node:
        print(req_node.data)

    ll8 = LinkedList(8)
    ll7 = LinkedList(7, next_val=ll8)
    ll6 = LinkedList(6, next_val=ll7)
    ll5 = LinkedList(5, next_val=ll6)
    ll4 = LinkedList(4, next_val=ll5)
    ll3 = LinkedList(3, next_val=ll4)
    ll2 = LinkedList(2, next_val=ll3)
    ll1 = LinkedList(1, next_val=ll2)
    ll8.next_val = ll3

    req_node = find_cycle(ll1)
    if req_node:
        print(req_node.data)
