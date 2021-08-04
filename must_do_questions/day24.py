"""
Given a binary tree, imagine you're standing to the right of the tree. Return an array of the values of the nodes you can
see ordered from top to bottom.
"""


class Tree:
    def __init__(self, root, left=None, right=None):
        self.left = left
        self.root = root
        self.right = right


def order_nodes(root, level, right_most):
    if root:
        if root.right:
            if not right_most[level]:
                if root.right and root.right.root:
                    right_most[level] = root.right.root
                    level += 1
        else:
            if not right_most[level]:
                if root.left and root.left.root:
                    right_most[level] = root.left.root
                    level += 1
        right_most[level] = None
        left = order_nodes(root.left, level=level, right_most=right_most)
        right = order_nodes(root.right, level=level, right_most=right_most)
        combined = right.copy()
        combined.update(left)
        return combined
    return right_most


def dfs(root, current_level, result):
    if not root:
        return result
    if current_level >= len(result):
        result.append(root.root)
    if root.right:
        dfs(root.right, current_level + 1, result)
    if root.left:
        dfs(root.left, current_level + 1, result)


def right_side_view(root):
    result = list()
    dfs(root, 0, result)
    return result


if __name__ == "__main__":
    five_1 = Tree(root=51)
    four_1 = Tree(root=41, right=five_1)
    three_1 = Tree(root=31, right=four_1)
    three_2 = Tree(root=32)
    two_1 = Tree(root=21, left=three_1, right=three_2)
    two_2 = Tree(root=22)
    one_1 = Tree(root=11, left=two_1, right=two_2)
    print(order_nodes(one_1, level=1, right_most={0: one_1.root, 1: None}))

    five_1 = Tree(root=51)
    four_1 = Tree(root=41, right=five_1)
    three_1 = Tree(root=31, right=four_1)
    three_2 = Tree(root=32)
    two_1 = Tree(root=21, left=three_1, right=three_2)
    two_2 = Tree(root=22)
    one_1 = Tree(root=11, left=two_1, right=two_2)
    print(right_side_view(one_1))
