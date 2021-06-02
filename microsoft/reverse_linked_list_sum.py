"""
Let's represent an integer in a linked list format by having each node represent a digit in the number.
The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5
is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

9 -> 9
5 -> 2
return 124 (99 + 25) as:

4 -> 2 -> 1
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


def form_digit(head, count):
    temp = head
    number = 0
    while temp:
        digit = (10 ** (count - 1)) * temp.data
        number += digit
        temp = temp.next_val
        count -= 1
    return number


if __name__ == "__main__":
    ll2 = LinkedList(9)
    ll1 = LinkedList(9, next_val=ll2)

    count_digit = traverse(ll1)

    rev_ll1 = reverse(ll1)

    digit_1 = form_digit(rev_ll1, count_digit)

    lll2 = LinkedList(2)
    lll1 = LinkedList(5, next_val=lll2)

    count_digit1 = traverse(lll1)
    rev_lll1 = reverse(lll1)

    digit_2 = form_digit(rev_lll1, count_digit1)
    new_num1 = digit_1 + digit_2
    count_digits = 0
    new_num = new_num1
    while new_num1 != 0:
        new_num1 = new_num1 // 10
        count_digits += 1

    print(digit_1, digit_2)
    print(new_num)

    prev = None
    new_head = None
    new_val = None
    while new_num != 0:

        di = new_num // (10 ** (count_digits - 1))
        new_node = LinkedList(di)
        new_node.next_val = prev

        new_num = new_num - (di * (10 ** (count_digits - 1)))
        prev = new_node
        count_digits -= 1

    print(prev)
    traverse(prev)
