def combinations(elements):
    if len(elements) == 0:
        return [[]]
    first_element = elements[0]
    rest = elements[1:]
    combinations_without_first = combinations(rest)
    combinations_with_first = []
    for comb in combinations_without_first:
        combination_with_first = [comb + [first_element]]
        combinations_with_first.extend(combination_with_first)

    res = []
    res.extend(combinations_without_first)
    res.extend(combinations_with_first)
    return res


if __name__ == "__main__":
    print(combinations(["a", "b"]))

    print(combinations(["a", "b", "c"]))
