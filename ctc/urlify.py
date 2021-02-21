"""
Write a method to replace all spaces in a string with "%20". You may assume that the string has sufficient space at
the end to hold the additional characters, and that you are given the "true" length of the string. (Note if implementing
in java,please use character array so that you can perform this operation in place)
"""


def urlify(string):
    string = string.strip()
    list_of_chars = ["%20" if stri == " " else stri for stri in string]
    return "".join(list_of_chars)


if __name__ == "__main__":
    string = "   Mr Chitrank Dixit  "
    print(urlify(string=string))
