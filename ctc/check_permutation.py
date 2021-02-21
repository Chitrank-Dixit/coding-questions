"""
Given two strings, write a method to decide if one is a permutation of the other
"""


def is_permutation(input_string, string):
    if len(input_string) != len(string):
        return False

    count = 0
    for i in range(len(string)):
        for j in range(len(input_string)):
            if input_string[j] == string[i]:
                count += 1

    return count == len(string)


if __name__ == "__main__":
    input_string = "abcd"
    string = "acdb"
    print(is_permutation(input_string=input_string, string=string))
