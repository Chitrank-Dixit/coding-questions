class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.value}"

def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False

    return p.value == q.value and isSameTree(p.right, q.right) and isSameTree(p.left, q.left)


if __name__ == "__main__":
    root = BinaryTree(value=1)
    root.left = BinaryTree(value=2)
    root.right = BinaryTree(value=3)

    root.left.left = BinaryTree(value=4)
    root.left.right = BinaryTree(value=5)

    root.right.left = BinaryTree(value=6)
    root.right.right = BinaryTree(value=7)

    root1 = BinaryTree(value=1)
    root1.left = BinaryTree(value=2)
    root1.right = BinaryTree(value=3)

    root1.left.left = BinaryTree(value=4)
    root1.left.right = BinaryTree(value=5)

    root1.right.left = BinaryTree(value=6)
    root1.right.right = BinaryTree(value=7)

    print(isSameTree(root, root1))