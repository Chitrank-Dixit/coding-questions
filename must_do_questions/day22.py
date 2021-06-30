"""
Given a binary tree, find its maximum depth. Maximum depth is the number of nodes along the longest path from the root
node to the furthest leaf node.
"""


class Tree:
    def __init__(self, root, left=None, right=None):
        self.left = left
        self.root = root
        self.right = right


def depth(root):
    if not root:
        return 0
    if not (root.left or root.right):
        return 0
    return 1 + depth(root.left) + depth(root.right)


def depth_v1(root, count=0):
    if not root:
        return count
    count += 1
    return max(depth_v1(root.left, count), depth_v1(root.right, count))


if __name__ == "__main__":
    five_1 = Tree(root=51)
    four_1 = Tree(root=41, right=five_1)
    three_1 = Tree(root=31, right=four_1)
    three_2 = Tree(root=32)
    two_1 = Tree(root=21, left=three_1, right=three_2)
    two_2 = Tree(root=22)
    one_1 = Tree(root=11, left=two_1, right=two_2)

    print(depth(root=one_1) + 1)
    six_1 = Tree(root=61)
    five_1 = Tree(root=51, left=six_1)
    four_1 = Tree(root=41, right=five_1)
    three_1 = Tree(root=31, right=four_1)
    three_2 = Tree(root=32)
    two_1 = Tree(root=21, left=three_1, right=three_2)
    two_2 = Tree(root=22)
    one_1 = Tree(root=11, left=two_1, right=two_2)

    print(depth(root=one_1) + 1)

    five_1 = Tree(root=51)
    four_1 = Tree(root=41, right=five_1)
    three_1 = Tree(root=31, right=four_1)
    three_2 = Tree(root=32)
    two_1 = Tree(root=21, left=three_1, right=three_2)
    two_2 = Tree(root=22)
    one_1 = Tree(root=11, left=two_1, right=two_2)

    print(depth_v1(root=one_1))
    six_1 = Tree(root=61)
    five_1 = Tree(root=51, left=six_1)
    four_1 = Tree(root=41, right=five_1)
    three_1 = Tree(root=31, right=four_1)
    three_2 = Tree(root=32)
    two_1 = Tree(root=21, left=three_1, right=three_2)
    two_2 = Tree(root=22)
    one_1 = Tree(root=11, left=two_1, right=two_2)

    print(depth_v1(root=one_1))
