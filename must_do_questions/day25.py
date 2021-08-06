"""
Given a complete binary tree, count the number of nodes
"""
import math


class Tree:
    def __init__(self, root, left=None, right=None):
        self.left = left
        self.root = root
        self.right = right


def no_of_nodes(root):
    # This is the solution to count number of nodes for any tree
    if not root:
        return 1
    left = no_of_nodes(root.left)
    right = no_of_nodes(root.right)
    return left + right


def get_tree_height(root):
    height = 0
    while root.left is not None:
        height += 1
        root = root.left

    return height


def node_exists(index_to_find, height, node):
    left = 0
    right = (2 ** height) - 1
    count = 0

    while count < height:
        mid_of_node = math.ceil((left + right) / 2)
        if index_to_find >= mid_of_node:
            node = node.right
            left = mid_of_node
        else:
            node = node.left
            right = mid_of_node - 1
        count += 1
    return node is not None


def count_nodes(root):
    if not root:
        return 0
    height = get_tree_height(root)
    if height == 0:
        return 1
    upper_count = (2 ** height) - 1
    left = 0
    right = upper_count
    while left < right:
        index_to_find = math.ceil((left + right) / 2)
        if node_exists(index_to_find, height, root):
            left = index_to_find
        else:
            right = index_to_find - 1
    return upper_count + left + 1


if __name__ == "__main__":
    five_1 = Tree(root=51)
    four_1 = Tree(root=41, right=five_1)
    three_1 = Tree(root=31, right=four_1)
    three_2 = Tree(root=32)
    two_1 = Tree(root=21, left=three_1, right=three_2)
    two_2 = Tree(root=22)
    one_1 = Tree(root=11, left=two_1, right=two_2)
    print(no_of_nodes(one_1) - 1)

    four_1 = Tree(root=41)
    three_1 = Tree(root=31, left=four_1)
    three_2 = Tree(root=32)
    three_3 = Tree(root=33)
    three_4 = Tree(root=34)
    two_1 = Tree(root=21, left=three_1, right=three_2)
    two_2 = Tree(root=22, left=three_3, right=three_4)
    one_1 = Tree(root=11, left=two_1, right=two_2)
    print(count_nodes(one_1))
