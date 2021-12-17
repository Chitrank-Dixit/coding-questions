"""
decimal to binary conversion
"""


def decimal_to_binary(num, string):
    if num == 0:
        return string

    string = str(num % 2) + string
    return decimal_to_binary(num // 2, string)


if __name__ == "__main__":
    num = 123
    string = ""
    print(decimal_to_binary(num, string))
