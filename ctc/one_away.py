"""
One Away: There are three types of edits that can be performed on strings. insert a character, remove a character, or
replace a character. Given two strings,write a function to check if they are one edit (or zero edits) away
"""


def one_away(str1, str2):
    # identify operation
    changes = 0
    if len(str2) < len(str1):
        # remove operation
        lookup = set()
        for ch in str2:
            lookup.add(ch)

        for ch in str1:
            if ch not in lookup:
                changes += 1

    if len(str1) < len(str2):
        # insert operation
        lookup = set()
        for ch in str1:
            lookup.add(ch)

        for ch in str2:
            if ch not in lookup:
                changes += 1

    if len(str1) == len(str2):
        # replace operation
        changes = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                changes += 1

    if changes > 1:
        return False

    return True


if __name__ == "__main__":
    str1 = "pale"
    str2 = "ple"
    print(one_away(str1, str2))

    str1 = "pales"
    str2 = "pale"
    print(one_away(str1, str2))

    str1 = "pale"
    str2 = "bale"
    print(one_away(str1, str2))

    str1 = "pale"
    str2 = "bake"
    print(one_away(str1, str2))
