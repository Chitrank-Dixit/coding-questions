def count_construct(target, word_bank):
    table = [0 for i in range(len(target) + 1)]
    table[0] = 1

    for i in range(len(target)):
        if table[i] > 0:
            for word in word_bank:
                if word == target[i : i + len(word)]:
                    table[i + len(word)] += table[i]

    return table[-1]


if __name__ == "__main__":
    print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
