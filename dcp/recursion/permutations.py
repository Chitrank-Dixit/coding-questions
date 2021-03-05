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
            perm_with_first.extend(first_element)
            perm_with_first.extend(perm[i:])
            all_permutations.append(perm_with_first)
            i += 1
    return all_permutations


if __name__ == "__main__":
    print(permutations(["a", "b"]))
    print(permutations(["a", "b", "c"]))
