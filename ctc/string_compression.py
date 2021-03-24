"""
String Compression: Implement a method to perform basic string compression using the counts of repeated characters,
for example the stirng aabcccccaaa become a2b1c5a3. If the "compressed" string would not become smaller than the
original string, your method should return the original string. You can assume the string has only uppercase and
lowercase (a-z).
"""


def string_compression(str):
    prev = 0
    current = 1
    encoded = ""
    ch_count = 1
    for index in range(1, len(str)):
        if str[prev] == str[current]:
            ch_count += 1
            current += 1
        elif str[prev] != str[current] or current == len(str) - 1:
            encoded += f"{str[prev]}{ch_count}"
            ch_count = 1
            prev = current
            current += 1

    encoded += f"{str[prev]}{ch_count}"

    return encoded


if __name__ == "__main__":
    str = "aabcccccaaa"
    print(string_compression(str))

    str = "aallfiiee"
    print(string_compression(str))
