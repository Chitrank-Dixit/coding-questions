class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.value}"


def preorder(root):
    if root:
        print(root)
        preorder(root.left)
        preorder(root.right)


if __name__ == "__main__":
    root = BinaryTree(value=1)
    root.left = BinaryTree(value=2)
    root.right = BinaryTree(value=3)

    root.left.left = BinaryTree(value=4)
    root.left.right = BinaryTree(value=5)

    root.right.left = BinaryTree(value=6)
    root.right.right = BinaryTree(value=7)
    preorder(root)
