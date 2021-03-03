def can_construct(target, word_bank):
    table = [False for i in range(len(target) + 1)]
    table[0] = True

    for i in range(len(target)):
        if table[i] is True:
            for word in word_bank:
                if word == target[i : i + len(word)]:
                    table[i + len(word)] = True

    return table[-1]


if __name__ == "__main__":
    print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
