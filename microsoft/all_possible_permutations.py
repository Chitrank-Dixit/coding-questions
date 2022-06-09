"""
Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
"""

def permutations(elements):
    if len(elements) == 0:
        return [[]]
    first_element = elements[0]
    rest = elements[1:]
    permutations_without_first = permutations(rest)
    all_permutations = []
    for perm in permutations_without_first:
        i = 0
        while i <= len(perm):
            perm_with_first = perm[0:i]
            perm_with_first.append(first_element)
            perm_with_first.extend(perm[i:])
            all_permutations.append(perm_with_first)
            i += 1
    return all_permutations


if __name__ == "__main__":
    print(permutations([1, 2, 3]))
