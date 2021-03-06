class BinaryTree:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


def max_path_sum(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return root.val

    return root.val + max(max_path_sum(root.left), max_path_sum(root.right))


if __name__ == "__main__":
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)

    print(max_path_sum(root))
