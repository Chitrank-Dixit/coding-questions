"""
String Rotation: Assume you have a method isSubstring which checks if one word is a substring of another. Given two
strings , s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring(e.g. "waterbottle
is a rotation of "erbottlewat")
"""


def is_rotation(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    j = len(s2) - 1
    count = 0
    while True:
        ele = s2.pop(j)
        s2.insert(0, ele)
        if s1 == s2:
            return True
        if count == len(s2):
            break
        count += 1
    return False


if __name__ == "__main__":
    s1 = "waterbottle"
    s2 = "erbottlewat"
    print(is_rotation(s1, s2))
