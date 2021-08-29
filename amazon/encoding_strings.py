"""
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive
 characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely
of alphabetic characters. You can assume the string to be decoded is valid.
"""


def encoding_string(string):
    prev = 0
    prev_count = 0
    resultant_string = ""
    current = 1
    while current < len(string):
        if string[prev] == string[current]:
            prev_count += 1
        else:
            prev_count += 1
            resultant_string += f"{prev_count}{string[prev]}"
            prev_count = 0
        prev += 1
        current += 1

    if prev_count > 0:
        prev_count += 1
        resultant_string += f"{prev_count}{string[prev]}"
    return resultant_string


if __name__ == "__main__":
    string = "AAAABBBCCDAA"
    print(encoding_string(string))
