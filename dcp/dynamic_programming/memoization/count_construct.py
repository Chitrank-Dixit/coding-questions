"""
write a function count_construct(target, word_bank) that accepts the target string and an array of strings.

the function should return the number of ways that the target can be constructed by concatenating elements of the
word_bank array
"""


def count_construct(target, word_bank, memory={}):
    if target in memory:
        return memory[target]

    if target == "":
        return 1

    total_count = 0
    for word in word_bank:
        try:
            is_prefix = target.index(word)
        except ValueError:
            is_prefix = -1

        if is_prefix == 0:
            suffix = target[len(word) :]
            num_ways = count_construct(suffix, word_bank, memory)
            if num_ways > 0:
                total_count += num_ways

    memory[target] = total_count
    return total_count


if __name__ == "__main__":
    print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))

    print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))

    print(
        count_construct(
            "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
            ["ee", "eeeee", "eeeeee", "eeee"],
        )
    )
