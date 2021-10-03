"""
Count palindromic substrings
"""


def get_palindromic_substrings(strings):
    count = 0

    # odd palindrome
    for axis in range(len(strings)):
        orbit = 0
        while (axis - orbit) >= 0 and (axis + orbit) < len(strings):
            if strings[axis - orbit] == strings[axis + orbit]:
                count += 1
            else:
                break
            orbit += 1

    # even palindrome
    axis = 0.5
    while axis < len(strings):
        orbit = 0.5
        while (axis - orbit) >= 0 and (axis + orbit) < len(strings):
            if strings[int(axis - orbit)] == strings[int(axis + orbit)]:
                count += 1
            else:
                break
            orbit += 1
        axis += 1

    return count


if __name__ == "__main__":
    strings = "madam"
    print(get_palindromic_substrings(strings=strings))

    strings = "acbbca"
    print(get_palindromic_substrings(strings=strings))
    # a
    # c
    # b
    # acbbca
    # bb
