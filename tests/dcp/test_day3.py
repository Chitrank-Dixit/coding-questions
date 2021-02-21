from dcp.day3 import Node, serialize, deserialize


class TestDay3:
    def test_day1(self):
        node = Node("root", Node("left", Node("left.left")), Node("right"))
        assert deserialize(serialize(node)).left.left.val == "left.left"
