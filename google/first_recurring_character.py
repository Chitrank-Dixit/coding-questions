"""
Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
"""


def recurring_char(string):
    match_set = set()
    for char in string:
        if char not in match_set:
            match_set.add(char)
        else:
            return char
    return None


if __name__ == "__main__":
    string = "acbbac"
    print(recurring_char(string))

    string = "abcdef"
    print(recurring_char(string))
