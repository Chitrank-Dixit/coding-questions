"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return self.val


def serialize(node, s=""):
    if not node:
        s += "# "
        return s
    s += node.val + " "
    s = serialize(node.left, s=s)
    s = serialize(node.right, s=s)
    return s


i = 0


def deserialize(s):
    global i
    if s[i] == "#":
        if i < len(s) - 2:
            i += 2
        return None
    else:
        space = s[i:].find(" ")
        sp = space + i
        node = Node(s[i:sp])
        i = sp + 1
        node.left = deserialize(s)
        node.right = deserialize(s)
        return node


if __name__ == "__main__":
    node = Node("root", Node("left", Node("left.left")), Node("right"))
    print(deserialize(serialize(node)).left.left.val == "left.left")
