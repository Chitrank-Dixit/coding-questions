"""
Given a doubly linked list, list nodes also have a child property that can point to separate doubly linked list.
These child lists can also have one or more child doubly linked lists of their own, and so on.

Return the list as a single level flattened doubly linked list.
"""


class ListNode:
    def __init__(self, value, prev_node=None, next_node=None, child_node=None):
        self._value = value
        self._prev_node = prev_node
        self._next_node = next_node
        self._child_node = child_node

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def prev_node(self):
        return self._prev_node

    @prev_node.setter
    def prev_node(self, prev_node):
        self._prev_node = prev_node

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, next_node):
        self._next_node = next_node

    @property
    def child_node(self):
        return self._child_node

    @child_node.setter
    def child_node(self, child_node):
        self._child_node = child_node


def single_level_flattened_doubly_linked_list(head):
    current = head
    while current:
        # check if child node exists
        if current.child_node:
            temp_current_next = current.next_node
            current.next_node = current.child_node
            temp_current_child = current.child_node
            while temp_current_child:
                if temp_current_child.next_node is None:
                    temp_current_next.prev_node = temp_current_child
                    temp_current_child.next_node = temp_current_next
                    break
                temp_current_child = temp_current_child.next_node
            current.child_node = None
        current = current.next_node
    return head


def single_level_flattened_doubly_linked_list_v1(head):
    if not head:
        return head
    current_node = head
    while current_node:
        if current_node.child_node is None:
            current_node = current_node.next_node
        else:
            tail = current_node.child_node
            while tail.next_node is not None:
                tail = tail.next_node
            tail.next_node = current_node.next_node
            if tail.next_node is not None:
                tail.next_node.prev_node = tail
            current_node.next_node = current_node.child_node
            current_node.next_node.prev_node = current_node
            current_node.child_node = None
    return head


def traverse(head):
    temp = head
    while temp:
        print(temp.value)
        temp = temp.next_node


def get_head():
    ll4_2 = ListNode(11)
    ll4_1 = ListNode(10, next_node=ll4_2)
    ll4_2.prev_node = ll4_1

    ll3_2 = ListNode(13)
    ll3_1 = ListNode(12, next_node=ll3_2)
    ll3_2.prev_node = ll3_1

    ll2_3 = ListNode(9)
    ll2_2 = ListNode(8, next_node=ll2_3)
    ll2_1 = ListNode(7, next_node=ll2_2)
    ll2_2.prev_node = ll2_1
    ll2_2.child_node = ll4_1

    ll1_6 = ListNode(6, next_node=None)
    ll1_5 = ListNode(5, next_node=ll1_6)
    ll1_4 = ListNode(4, next_node=ll1_5)
    ll1_3 = ListNode(3, next_node=ll1_4)
    ll1_2 = ListNode(2, next_node=ll1_3)
    ll1_1 = ListNode(1, next_node=ll1_2)

    ll1_6.prev_node = ll1_5
    ll1_5.prev_node = ll1_4
    ll1_4.prev_node = ll1_3
    ll1_3.prev_node = ll1_2
    ll1_2.prev_node = ll1_1

    ll1_5.child_node = ll3_1
    ll1_2.child_node = ll2_1
    return ll1_1


if __name__ == "__main__":

    target_node = get_head()
    traverse(target_node)
    head = single_level_flattened_doubly_linked_list(target_node)

    print("-----------")
    traverse(head)

    print("V1 implementations")

    target_node = get_head()
    traverse(target_node)
    head1 = single_level_flattened_doubly_linked_list_v1(target_node)

    print("-----------")
    traverse(head1)
