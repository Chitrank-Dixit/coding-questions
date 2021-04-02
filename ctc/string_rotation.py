"""
String Rotation: Assume you have a method isSubstring which checks if one word is a substring of another. Given two
strings , s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring(e.g. "waterbottle
is a rotation of "erbottlewat")
"""


def is_rotation(s1, s2):
    i = 0
    j = len(s2) - 1
    match_count = 0
    while i < len(s1) and j >= 0:
        if s1[i] == s2[j]:
            match_count += 1
        i += 1
        j -= 1
    if match_count > 0:
        return True
    return False


if __name__ == "__main__":
    s1 = "waterbottle"
    s2 = "erbottlewat"
    print(is_rotation(s1, s2))
