"""
insert value into binary search tree
"""


class BinaryTree:
    def __init__(self, value=None, left=None, right=None):
        self._value = value
        self._left = left
        self._right = right

    def __str__(self):
        return f"{self.value}"

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right


def inorder(root):
    if root:
        inorder(root.left)

        print(root)

        inorder(root.right)


def insert_node(head, value):
    if not head:
        head = BinaryTree()
        head.value = value
        return head

    if head.value < value:
        head.right = insert_node(head.right, value)
    else:
        head.left = insert_node(head.left, value)

    return head


if __name__ == "__main__":
    root = BinaryTree()
    root.value = 100

    root.left = BinaryTree()
    root.left.value = 80
    root.right = BinaryTree()
    root.right.value = 120

    root.left.left = BinaryTree()
    root.left.left.value = 50
    root.left.right = BinaryTree()
    root.left.right.value = 90

    root.right.left = BinaryTree()
    root.right.left.value = 110
    root.right.right = BinaryTree()
    root.right.right.value = 140

    root.left.left.left = BinaryTree()
    root.left.left.left.value = 30
    root.left.left.right = BinaryTree()
    root.left.left.right.value = 60
    root.left.right.left = BinaryTree()
    root.left.right.left.value = 85
    root.left.right.right = BinaryTree()
    root.left.right.right.value = 95
    root.right.left.right = BinaryTree()
    root.right.left.right.value = 115
    root.right.right.right = BinaryTree()
    root.right.right.right.value = 150

    print("---------------------------")
    print(inorder(root))

    print("---------------------------")
    root = insert_node(root, 108)
    print(inorder(root))
