"""
Implement an algorithm to determine if a string has all unique characters. What if you cannot user additional data structures ?
"""


def is_uniqe(string):
    unique = set()
    for char in string:
        if char in unique:
            return False
        unique.add(char)
    return True


if __name__ == "__main__":
    string = "chitrank"
    print(is_uniqe(string))
    string = "dixit"
    print(is_uniqe(string))
