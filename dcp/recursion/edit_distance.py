"""
The words COMPUTER and COMMUTER are very similar, and a update of just one letter, P->M will change the first world into
second. Similarly, word SPORT can be changed into SORT by deleting one character, p or equivalent, SORT can be changed
into SPORT by inserting p.
"""


def edit_distance(s1, s2):
    # If one of the string is empty then the edit distance will be equal to the length of the other because in that case we just have to
    # insert all the letters in that string to duplicate it or remove all from the other to make it empty like the other
    if len(s1) == 0:
        return len(s2)
    elif len(s2) == 0:
        return len(s1)
    elif s1[0] == s2[0]:
        # The Edit Distance of two string with the same last alphabet will be the same the distance of the two strings without the last alphabet
        # This is cause the last alphabet being same won't provide any input, as they are already same
        return edit_distance(s1[1:], s2[1:])
    else:
        # If last letter isn't the same then we have to perform one of the three operations i.e. insertion, deletion or replacing letter.
        # Remember we are looking for the minimum number of changes, hence after computing the cost of all the three operations we take
        # just the minimum between the three
        return 1 + min(
            edit_distance(s1, s2[1:]),  # Insertion
            edit_distance(s1[1:], s2[1:]),  # Replacing letter
            edit_distance(s1[1:], s2),  # Deletion
        )


def edit_distance_dp(s1, s2):
    m = len(s1) + 1
    n = len(s2) + 1

    tbl = {}
    for i in range(m):
        tbl[i, 0] = i
    for j in range(n):
        tbl[0, j] = j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            tbl[i, j] = min(
                tbl[i, j - 1] + 1, tbl[i - 1, j] + 1, tbl[i - 1, j - 1] + cost
            )

    return tbl[i, j]


if __name__ == "__main__":
    str1 = "COMPUTER"
    str2 = "COMMUTER"
    print(edit_distance(str1, str2))
    print(edit_distance_dp(str1, str2))

    str1 = "SPORT"
    str2 = "SORT"
    print(edit_distance(str1, str2))
    print(edit_distance_dp(str1, str2))

    str1 = "SUNDAY"
    str2 = "SATURDAY"
    print(edit_distance(str1, str2))
    print(edit_distance_dp(str1, str2))
