# Python3 implementation of the approach

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Head of the list
head = None

# Tail of the list
tail = None


# Function to print the list
def display():
    if head is None:
        return

    temp = head

    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next

    print()


# Function to add node in the list
def push(data):
    global head, tail

    # Create new node
    nn = Node(data)

    # Linking at first positio
    if head is None:
        head = nn
    else:
        temp = head

        while temp.next is not None:
            temp = temp.next

        # Linking at last in list
        temp.next = nn


# Function to unfold the given link list
def unfold(node):
    global head, tail

    if node is None:
        return

    # This condition will reach if
    # the number of nodes is odd
    # head and tail is same i.e. last node
    if node.next is None:
        head = tail = node
        return

    # This base condition will reach if
    # the number of nodes is even
    # mark head to the second last node
    # and tail to the last node
    elif node.next.next is None:
        head = node
        tail = node.next
        return

    # Storing next node in temp pointer
    # before making the recursive call
    temp = node.next

    # Recursive call
    unfold(node.next.next)

    # Connecting first node to head
    # and mark it as a new head
    node.next = head
    head = node

    # Connecting tail to second node (temp)
    # and mark it as a new tail
    tail.next = temp
    tail = temp
    tail.next = None


# Driver code
if __name__ == "__main__":
    # Adding nodes to the list
    push(1)
    push(5)
    push(2)
    push(4)
    push(3)

    # Displaying the original nodes
    display()

    # Calling unfold function
    unfold(head)

    # Displaying the list
    # after modification
    display()
