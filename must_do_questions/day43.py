"""
Given the following interface implement its methods

interface Monarchy {
    void birth(String child, String parent);
    void death(String name);
    List<String> getOrderOfSuccession();
}
"""


class Monarch(object):
    def __init__(self):
        self.name = None
        self.children = []
        self.is_alive = True


class Monarchy(object):
    def __init__(self):
        self.firstMonarch = None
        self.monarchs = {}

    def birth(self, child, parent):
        # create monarch
        monarch = Monarch()
        monarch.name = child
        # If it's the first monarch
        if parent is None and self.firstMonarch is None:
            self.firstMonarch = monarch
        else:
            # find parent and add child
            if not (parent in self.monarchs):
                print("Parent not found")
                return
            self.monarchs[parent].children.append(monarch)
        # Add the monarch to hash table
        self.monarchs[child] = monarch

    def death(self, name):
        self.monarchs[name].is_alive = False

    def pre_order(self, node):
        if node:
            if node.is_alive:
                # don't print dead people :'(
                print(node.name)
            for child in node.children:
                self.pre_order(child)

    def get_order_of_succession(self):
        self.pre_order(self.firstMonarch)


if __name__ == "__main__":
    m = Monarchy()
    m.birth("jake", None)
    m.birth("catherine", "jake")
    m.birth("jane", "catherine")
    m.birth("farah", "jane")
    m.birth("tom", "jake")
    m.birth("celine", "jake")
    m.birth("mark", "catherine")
    m.birth("peter", "celine")
    m.get_order_of_succession()
    m.death("jake")
    m.death("jane")
    print("---------------")
    m.get_order_of_succession()
