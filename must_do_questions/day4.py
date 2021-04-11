"""
Given two strings S and T, return if they equal when both are typed out. Any '#' that appears in the string counts
as a backspace.
"""


def regenerate_string(s):
    new_s = []
    i = 0
    while i < len(s):
        if s[i] != "#":
            new_s.append(s[i])
        else:
            new_s.pop()
        i += 1

    return new_s


def regenerate_string_v1(s):
    new_s = []
    i = len(s) - 1
    move = 0
    while i >= 0:
        if s[i] == "#":
            move += 1
        else:
            if move > 0:
                i -= move
            new_s.insert(0, s[i])
        i -= 1
    return new_s


def string_match(s, t):
    new_s = regenerate_string(s)
    new_t = regenerate_string(t)
    if len(new_s) != len(new_t):
        return False
    return "".join(new_s) == "".join(new_t)


if __name__ == "__main__":
    s = "ab#c"
    t = "az#c"

    print(string_match(s, t))

    s = "ab#c"
    t = "azk##c"

    print(string_match(s, t))

    s = "ab#c"
    t = "Ab#c"

    print(string_match(s, t))

    s = "abcd###qwer"
    t = "azxy###qwer"
    print(string_match(s, t))
