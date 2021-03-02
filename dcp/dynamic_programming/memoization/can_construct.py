"""
write a function can_construct(target, word_bank) that accepts a target string and an array of strings

the function should return a boolean indicating whether or not the target can be constructed by concatenating element of
word_bank array

you may reuse element of word_bank as many times as needed
"""


def can_construct(target, word_bank, memory={}):
    if target in memory:
        return memory[target]
    if target == "":
        return True
    for word in word_bank:
        try:
            is_prefix = target.index(word)
        except ValueError:
            is_prefix = -1

        if is_prefix == 0:
            suffix = target[len(word) :]
            if can_construct(suffix, word_bank, memory):
                memory[target] = True
                return True
    memory[target] = False
    return False


if __name__ == "__main__":
    print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))

    print(
        can_construct(
            "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
            ["ee", "eeeee", "eeeeee", "eeee"],
        )
    )
