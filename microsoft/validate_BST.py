"""
Check if Binary tree is a BST or not
"""
INT_MAX = 4294967296
INT_MIN = -4294967296


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validate_BST(root, mini=INT_MIN, maxi=INT_MAX):
    if root is None:
        return True
    if not (mini < root.value < maxi):
        return False
    return validate_BST(root.left, mini, root.value) and validate_BST(
        root.right, root.value, maxi
    )


if __name__ == "__main__":

    root = BST(value=10)
    root.left = BST(value=7)
    root.right = BST(value=15)
    root.left.left = BST(value=3)
    root.left.right = BST(value=8)
    root.right.left = BST(value=9)
    root.right.right = BST(value=17)
    print(validate_BST(root))

    root = BST(value=4)
    root.left = BST(value=2)
    root.right = BST(value=5)
    root.left.left = BST(value=1)
    root.left.right = BST(value=3)
    print(validate_BST(root))
