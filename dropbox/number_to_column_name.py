"""
Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ",
"AAA", "AAB", ....

Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA".
"""


def number_to_column_name(n):
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string


if __name__ == "__main__":
    num = 1
    print(number_to_column_name(num))

    num = 27
    print(number_to_column_name(num))

    num = 134
    print(number_to_column_name(num))

    num = 2756
    print(number_to_column_name(num))
