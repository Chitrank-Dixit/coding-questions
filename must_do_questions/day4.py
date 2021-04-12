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


def regenerate_string_V2(s, t):
    p1 = len(s) - 1
    p2 = len(t) - 1
    while p1 >= 0 or p2 >= 0:
        if s[p1] == "#" or t[p2] == "#":
            if s[p1] == "#":
                backcount = 2
                while backcount > 0:
                    p1 -= 1
                    backcount -= 1
                    if s[p1] == "#":
                        backcount = backcount + 2

            if t[p2] == "#":
                backcount = 2
                while backcount > 0:
                    p2 -= 1
                    backcount -= 1
                    if t[p2] == "#":
                        backcount = backcount + 2
        else:
            if s[p1] != t[p2]:
                return False
            else:
                p1 -= 1
                p2 -= 1
    return True


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

    print("------")

    s = "ab#c"
    t = "az#c"

    print(regenerate_string_V2(s, t))

    s = "ab#c"
    t = "azk##c"

    print(regenerate_string_V2(s, t))

    s = "ab#c"
    t = "Ab#c"

    print(regenerate_string_V2(s, t))

    s = "abcd###qwer"
    t = "azxy###qwer"
    print(regenerate_string_V2(s, t))
