"""
Given a binary tree,return the level order traversal of the nodes values as an array.
"""


class Tree:
    def __init__(self, root, left=None, right=None):
        self.left = left
        self.root = root
        self.right = right


def level_order(root):
    if not root:
        return []
    result = []
    queue = [root]
    while len(queue) > 0:
        length = len(queue)
        count = 0
        current_level_values = []
        while count < length:
            current_node = queue.pop(0)
            current_level_values.append(current_node.root)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            count += 1
        result.append(current_level_values)
    return result


if __name__ == "__main__":
    five_1 = Tree(root=51)
    four_1 = Tree(root=41, right=five_1)
    three_1 = Tree(root=31, right=four_1)
    three_2 = Tree(root=32)
    two_1 = Tree(root=21, left=three_1, right=three_2)
    two_2 = Tree(root=22)
    one_1 = Tree(root=11, left=two_1, right=two_2)
    print(level_order(one_1))

    five_1 = Tree(root=51)
    five_2 = Tree(root=52)
    four_1 = Tree(root=41, right=five_2, left=five_1)
    three_1 = Tree(root=31, right=four_1)
    three_2 = Tree(root=32)
    two_1 = Tree(root=21, left=three_1, right=three_2)
    two_2 = Tree(root=22)
    one_1 = Tree(root=11, left=two_1, right=two_2)
    print(level_order(one_1))
