"""
Implement an algorithm to find the kth to last element of a singly linked list.
"""


class LinkedList:
    def __init__(self, data, next_val):
        self.data = data
        self.next_val = next_val


class Queue:
    def __init__(self, list_count):
        self.list = []
        self.list_count = list_count

    def enqueue(self, item):
        if len(self.list) == self.list_count:
            self.dequeue()
        self.list.append(item)

    def dequeue(self):
        if len(self.list) > 0:
            self.list.pop(0)

    def get_kth(self):
        return self.list[0]


def traverse(head):
    list_length = 0
    while head:
        # print(head.data)
        list_length += 1
        head = head.next_val
    return list_length


def find_kth_to_last(root, k):
    temp = root
    index = 0
    result = None
    while temp:
        if index == k:
            result = temp.data
            break
        index += 1
        temp = temp.next_val
    return result


def find_kth_to_last_v1(root, k):
    temp = root
    queue = Queue(list_count=k)
    while temp:
        queue.enqueue(temp.data)
        temp = temp.next_val

    return queue.get_kth()


if __name__ == "__main__":
    ll6 = LinkedList(4, None)
    ll5 = LinkedList(5, ll6)
    ll4 = LinkedList(4, ll5)
    ll3 = LinkedList(1, ll4)
    ll2 = LinkedList(2, ll3)
    ll1 = LinkedList(1, ll2)
    length = traverse(ll1)
    print("Kth from last", find_kth_to_last(ll1, k=length - 3))
    print("-------------")
    print("----Next----")
    ll6 = LinkedList(5, None)
    ll5 = LinkedList(5, ll6)
    ll4 = LinkedList(5, ll5)
    ll3 = LinkedList(5, ll4)
    ll2 = LinkedList(5, ll3)
    ll1 = LinkedList(1, ll2)
    length = traverse(ll1)
    print("Kth from last", find_kth_to_last(ll1, k=length - 4))
    print("-------------")
    print("v1 approach")
    ll6 = LinkedList(4, None)
    ll5 = LinkedList(5, ll6)
    ll4 = LinkedList(4, ll5)
    ll3 = LinkedList(1, ll4)
    ll2 = LinkedList(2, ll3)
    ll1 = LinkedList(1, ll2)
    print("Kth from last", find_kth_to_last_v1(ll1, k=3))
    print("-------------")
    print("----Next----")
    ll6 = LinkedList(5, None)
    ll5 = LinkedList(5, ll6)
    ll4 = LinkedList(5, ll5)
    ll3 = LinkedList(5, ll4)
    ll2 = LinkedList(5, ll3)
    ll1 = LinkedList(1, ll2)
    print("Kth from last", find_kth_to_last_v1(ll1, k=4))
    print("-------------")
