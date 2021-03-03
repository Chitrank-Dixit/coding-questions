def count_construct(target, word_bank):
    table = [[] for i in range(len(target) + 1)]
    table[0] = [[]]

    for i in range(len(target)):
        for word in word_bank:
            if word == target[i : i + len(word)]:
                new_combination = [
                    combination + [word] for combination in table[i]
                ]
                table[i + len(word)].extend(new_combination)

    return table[-1]


if __name__ == "__main__":
    print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
