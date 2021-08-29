"""
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
You may also use a list or array to represent a set.
"""


def power_set(simple_set, set_size):
    # set_size of power set of a set
    # with set_size n is (2**n -1)
    pow_set_size = 2 ** set_size
    resultant_set = list()
    # Run from counter 000..0 to 111..1
    for counter in range(0, pow_set_size):
        inner_set = set()
        for j in range(0, set_size):

            # Check if jth bit in the
            # counter is set If set then
            # print jth element from set
            if (counter & (1 << j)) > 0:
                inner_set.add(simple_set[j])
        resultant_set.append(inner_set)
    return resultant_set


if __name__ == "__main__":
    example_set = [1, 2, 3]
    print(power_set(example_set, 3))
