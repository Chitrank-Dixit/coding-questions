"""
write a function all_construct(target, word_bank) that accepts a target string and an array of strings.

the function should return a 2D array containing all of the ways that the target can be constructed by concatenating
elements of the word_bank array. Each element of the 2D array should represent one combination that constructs the
target

you may reuse elements of word_bank as many times as needed.
"""


def all_construct(target, word_bank, memory={}):
    if target in memory:
        return memory[target]
    if target == "":
        return [[]]

    combination_list = []
    for word in word_bank:
        try:
            is_prefix = target.index(word)
        except ValueError:
            is_prefix = -1

        if is_prefix == 0:
            suffix = target[len(word) :]
            suffix_ways = all_construct(suffix, word_bank, memory)
            target_ways = list()
            for suf in suffix_ways:
                target_ways.append(word)
                target_ways.extend(suf)
            if target_ways != []:
                combination_list.append(target_ways)

    memory[target] = combination_list
    return combination_list


if __name__ == "__main__":
    print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))

    print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))

    print(
        all_construct(
            "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
            ["ee", "eeeee", "eeeeee", "eeee"],
        )
    )
