"""
Given a binary tree, determine if it is a valid binary search tree.
"""


class BST:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.val = val
        self.right = right


def is_valid_bst(root):
    if not root:
        return True
    if not root.left or not root.right:
        return root.val
    if root.left.val < root.val < root.right.val:
        left = is_valid_bst(root.left)
        right = is_valid_bst(root.right)
        if left and right and left < root.val < right:
            return root.val
    return False


def dfs(node, min, max):
    if node.val < min or node.val >= max:
        return False
    if node.left:
        if not dfs(node.left, min, node.val):
            return False

    if node.right:
        if not dfs(node.right, node.val, max):
            return False
    return True


def is_valid_bst_v1(root):
    if not root:
        return True
    INT_MAX = 4294967296
    INT_MIN = -4294967296
    return dfs(root, INT_MIN, INT_MAX)


if __name__ == "__main__":
    three_3 = BST(val=16)
    three_4 = BST(val=25)
    three_1 = BST(val=5)
    three_2 = BST(val=9)
    two_1 = BST(val=7, left=three_1, right=three_2)
    two_2 = BST(val=18, left=three_3, right=three_4)
    one_1 = BST(val=12, left=two_1, right=two_2)
    print(is_valid_bst(one_1) == one_1.val)

    print(is_valid_bst_v1(one_1))
